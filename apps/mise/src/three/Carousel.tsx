/* The shelf, as a shallow arc of plates.

   The arc is the continuity device: when the companion narrows the shelf, dishes
   are not swapped out underneath you — the arc re-forms, and the dishes that
   survived the filter travel to their new seats. You can watch where your dish
   went, which is the whole reason this is 3D and not a grid. */

import { useEffect, useMemo, useRef, useState } from 'react';
import { useFrame, useThree } from '@react-three/fiber';
import { ContactShadows } from '@react-three/drei';
import * as THREE from 'three';
import type { Recipe } from '../data/recipes';
import { Dish } from './Dish';

const RADIUS = 4.35;
const ARC = 0.46;
/** Beyond this many seats from focus a dish is not worth drawing. */
const VISIBLE = 3;

const prefersReducedMotion = () =>
  typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;

interface SeatProps {
  recipe: Recipe;
  offset: number;
  focused: boolean;
  cooking: boolean;
  onPick: () => void;
}

function Seat({ recipe, offset, focused, cooking, onPick }: SeatProps) {
  const group = useRef<THREE.Group>(null);
  const [hovered, setHovered] = useState(false);
  const reduced = useMemo(prefersReducedMotion, []);

  useFrame((_, delta) => {
    const g = group.current;
    if (!g) return;

    const spread = cooking ? ARC * 1.5 : ARC;
    const angle = offset * spread;
    const distance = Math.abs(offset);

    const targetX = Math.sin(angle) * RADIUS;
    const targetZ = Math.cos(angle) * RADIUS - RADIUS;
    const lift = focused ? (cooking ? 0.34 : 0.12) : 0;
    const targetY = -distance * 0.05 + lift + (hovered && !focused ? 0.05 : 0);

    /* damp, not lerp: frame-rate independent, and it eases out exponentially,
       which is the same curve the CSS side uses. */
    const rate = reduced ? 24 : 5.2;
    g.position.x = THREE.MathUtils.damp(g.position.x, targetX, rate, delta);
    g.position.y = THREE.MathUtils.damp(g.position.y, targetY, rate, delta);
    g.position.z = THREE.MathUtils.damp(g.position.z, targetZ, rate, delta);

    const targetScale = focused ? (cooking ? 0.78 : 1) : Math.max(0.52, 0.84 - distance * 0.12);
    const s = THREE.MathUtils.damp(g.scale.x, targetScale, rate, delta);
    g.scale.setScalar(s);

    // Plates turn with the arc so the near rim always faces the viewer.
    g.rotation.y = THREE.MathUtils.damp(g.rotation.y, -angle * 0.5, rate, delta);

    // In cook mode the dish is the subject, so it turns slowly on its stand.
    if (cooking && focused && !reduced) {
      g.rotation.y += delta * 0.09;
    }

    // A tilt toward the camera on focus: you get to look into the bowl.
    const targetTilt = focused && !cooking ? -0.06 : 0;
    g.rotation.x = THREE.MathUtils.damp(g.rotation.x, targetTilt, rate, delta);
  });

  const distance = Math.abs(offset);
  const detail = distance < 0.7 ? 1 : distance < 1.8 ? 0.55 : 0.3;
  const dim = focused ? 0 : Math.min(0.66, distance * 0.26);

  return (
    <group
      ref={group}
      onClick={(e) => {
        e.stopPropagation();
        onPick();
      }}
      onPointerOver={(e) => {
        e.stopPropagation();
        setHovered(true);
        document.body.style.cursor = 'pointer';
      }}
      onPointerOut={() => {
        setHovered(false);
        document.body.style.cursor = '';
      }}
    >
      <Dish recipe={recipe} detail={detail} dim={dim} />
    </group>
  );
}

export interface CarouselProps {
  recipes: Recipe[];
  activeIndex: number;
  cooking: boolean;
  onPick: (index: number) => void;
  onScrub: (index: number) => void;
}

export function Carousel({ recipes, activeIndex, cooking, onPick, onScrub }: CarouselProps) {
  const spin = useRef(activeIndex);
  const drag = useRef<{ startX: number; startSpin: number } | null>(null);
  const [, force] = useState(0);
  const { size } = useThree();
  const reduced = useMemo(prefersReducedMotion, []);

  // Re-seat when the shelf itself changes length under us.
  useEffect(() => {
    if (spin.current > recipes.length - 1) spin.current = Math.max(0, recipes.length - 1);
  }, [recipes.length]);

  useFrame((_, delta) => {
    if (drag.current) return;
    const next = THREE.MathUtils.damp(spin.current, activeIndex, reduced ? 24 : 4.6, delta);
    if (Math.abs(next - spin.current) > 0.0004) {
      spin.current = next;
      force((n) => n + 1);
    } else if (spin.current !== activeIndex) {
      spin.current = activeIndex;
      force((n) => n + 1);
    }
  });

  return (
    <group
      position={[0, cooking ? 0.34 : -0.24, 0]}
      onPointerDown={(e) => {
        if (cooking) return;
        (e.target as Element).setPointerCapture?.(e.pointerId);
        drag.current = { startX: e.clientX, startSpin: spin.current };
      }}
      onPointerMove={(e) => {
        if (!drag.current) return;
        const travelled = (e.clientX - drag.current.startX) / (size.width * 0.22);
        const next = THREE.MathUtils.clamp(
          drag.current.startSpin - travelled,
          0,
          recipes.length - 1,
        );
        spin.current = next;
        onScrub(Math.round(next));
        force((n) => n + 1);
      }}
      onPointerUp={() => {
        if (!drag.current) return;
        drag.current = null;
        onPick(Math.round(THREE.MathUtils.clamp(spin.current, 0, recipes.length - 1)));
      }}
    >
      {recipes.map((recipe, i) => {
        const offset = i - spin.current;
        if (Math.abs(offset) > VISIBLE) return null;
        return (
          <Seat
            key={recipe.id}
            recipe={recipe}
            offset={offset}
            focused={Math.round(spin.current) === i}
            cooking={cooking}
            onPick={() => onPick(i)}
          />
        );
      })}

      <ContactShadows
        position={[0, -0.32, 0]}
        opacity={0.62}
        scale={16}
        blur={2.6}
        far={4}
        resolution={512}
        color="#000000"
      />
    </group>
  );
}
