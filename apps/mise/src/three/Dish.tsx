/* One plated dish: the vessel, then every layer instanced onto it. */

import { useMemo } from 'react';
import * as THREE from 'three';
import { Instance, Instances } from '@react-three/drei';
import type { Recipe } from '../data/recipes';
import { plateRecipe, vesselProfile, type PlacedLayer } from './plating';

const GROUND = new THREE.Color('#0a0907');

/** How wide the flat floor of each vessel actually is. */
const WELL_RADIUS: Record<Recipe['vessel'], number> = {
  plate: 0.84,
  pan: 0.74,
  bowl: 0.3,
  board: 0,
};

/** Distant plates read as the same dish in lower light, not a greyed-out copy. */
function tint(hex: string, dim: number): THREE.Color {
  const c = new THREE.Color(hex);
  return dim > 0 ? c.lerp(GROUND, dim) : c;
}

function LayerGeometry({ form, size }: { form: PlacedLayer['form']; size: number }) {
  switch (form) {
    case 'sauce':
      return <circleGeometry args={[size, 64]} />;
    case 'dome':
      return <sphereGeometry args={[size, 32, 20, 0, Math.PI * 2, 0, Math.PI / 2]} />;
    case 'disc':
      return <cylinderGeometry args={[size, size * 0.96, size * 0.24, 28]} />;
    case 'sphere':
      return <sphereGeometry args={[size, 18, 14]} />;
    case 'torus':
      return <torusGeometry args={[size, size * 0.34, 10, 24]} />;
    case 'strand':
      /* A noodle is a coil seen from above: a fat, low-segment torus arc reads
         as one strand folded back on itself and costs almost nothing. */
      return <torusGeometry args={[size * 0.42, size * 0.085, 8, 20, Math.PI * 1.55]} />;
    case 'shard':
      return <capsuleGeometry args={[size * 0.3, size * 0.9, 4, 12]} />;
    case 'cube':
      return <boxGeometry args={[size, size * 0.82, size]} />;
    case 'crumb':
    default:
      return <dodecahedronGeometry args={[size, 0]} />;
  }
}

function Layer({ layer, dim }: { layer: PlacedLayer; dim: number }) {
  const color = useMemo(() => tint(layer.color, dim), [layer.color, dim]);
  const flat = layer.form === 'sauce';

  return (
    <Instances limit={layer.placements.length} castShadow={!flat} receiveShadow>
      <LayerGeometry form={layer.form} size={layer.size} />
      <meshPhysicalMaterial
        color={color}
        roughness={layer.roughness}
        clearcoat={Math.min(1, layer.sheen * 2.6)}
        clearcoatRoughness={0.28}
        sheen={layer.sheen > 0.2 ? 0.4 : 0}
        sheenColor="#ffd9b0"
      />
      {layer.placements.map((p, i) => (
        <Instance
          key={i}
          position={p.position}
          rotation={flat ? [-Math.PI / 2, 0, p.rotation[1]] : p.rotation}
          scale={p.scale}
        />
      ))}
    </Instances>
  );
}

function Vessel({ recipe, dim }: { recipe: Recipe; dim: number }) {
  const geometry = useMemo(() => {
    if (recipe.vessel === 'board') {
      return new THREE.BoxGeometry(2.05, 0.075, 1.5);
    }
    const points = vesselProfile(recipe.vessel).map(([x, y]) => new THREE.Vector2(x, y));
    return new THREE.LatheGeometry(points, 72);
  }, [recipe.vessel]);

  const rim = useMemo(() => tint(recipe.vesselColor.rim, dim), [recipe.vesselColor.rim, dim]);
  const well = useMemo(() => tint(recipe.vesselColor.well, dim), [recipe.vesselColor.well, dim]);

  return (
    <group>
      <mesh geometry={geometry} castShadow receiveShadow position={[0, recipe.vessel === 'board' ? 0.037 : 0, 0]}>
        <meshPhysicalMaterial
          color={rim}
          roughness={recipe.vessel === 'board' ? 0.78 : 0.32}
          clearcoat={recipe.vessel === 'board' ? 0 : 0.65}
          clearcoatRoughness={0.22}
          side={THREE.DoubleSide}
        />
      </mesh>
      {recipe.vessel !== 'board' && (
        /* The well is the flat pool of glaze at the bottom of the vessel, so its
           radius has to follow the silhouette — a plate-sized disc inside a bowl
           punches straight out through the curved wall. */
        <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, 0.006, 0]} receiveShadow>
          <circleGeometry args={[WELL_RADIUS[recipe.vessel], 64]} />
          <meshPhysicalMaterial color={well} roughness={0.38} clearcoat={0.5} />
        </mesh>
      )}
      {recipe.vessel === 'pan' && (
        /* The handle is what tells you at a glance that this one comes to the
           table in the thing it cooked in. */
        <mesh position={[1.24, 0.19, 0]} rotation={[0, 0, Math.PI / 2 - 0.08]} castShadow>
          <cylinderGeometry args={[0.055, 0.048, 0.78, 16]} />
          <meshPhysicalMaterial color={rim} roughness={0.5} />
        </mesh>
      )}
    </group>
  );
}

export function Dish({
  recipe,
  detail = 1,
  dim = 0,
}: {
  recipe: Recipe;
  detail?: number;
  dim?: number;
}) {
  const layers = useMemo(() => plateRecipe(recipe, detail), [recipe, detail]);

  return (
    <group>
      <Vessel recipe={recipe} dim={dim} />
      {layers.map((layer, i) => (
        <Layer key={`${recipe.id}-${i}`} layer={layer} dim={dim} />
      ))}
    </group>
  );
}
