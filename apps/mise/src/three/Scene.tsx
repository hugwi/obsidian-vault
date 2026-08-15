/* The room the glass sits in front of. */

import { Component, Suspense, type ReactNode } from 'react';
import { Canvas } from '@react-three/fiber';
import { Environment, Lightformer } from '@react-three/drei';
import type { Recipe } from '../data/recipes';
import { Carousel } from './Carousel';

class GLBoundary extends Component<{ children: ReactNode; fallback: ReactNode }, { failed: boolean }> {
  state = { failed: false };
  static getDerivedStateFromError() {
    return { failed: true };
  }
  render() {
    return this.state.failed ? this.props.fallback : this.props.children;
  }
}

export interface SceneProps {
  recipes: Recipe[];
  activeIndex: number;
  cooking: boolean;
  onPick: (index: number) => void;
  onScrub: (index: number) => void;
}

export function Scene(props: SceneProps) {
  return (
    <div className="scene" aria-hidden="true">
      <GLBoundary
        fallback={
          /* No WebGL: the room goes dark and the glass shell keeps working. The
             app is a recipe app before it is a 3D one. */
          <div className="scene__fallback" />
        }
      >
        <Canvas
          shadows
          dpr={[1, 2]}
          gl={{ antialias: true, powerPreference: 'high-performance' }}
          camera={{ position: [0, 1.98, 3.62], fov: 37 }}
        >
          <fog attach="fog" args={['#0a0907', 6.5, 15]} />

          {/* Studio light, built in-scene: three emitters rendered into an
              environment map, so the lighting ships with the app instead of
              fetching an HDR. It lives here rather than inside the carousel —
              parented to the group that re-mounts whenever the shelf is
              filtered, drei's portal lost its virtual scene and the emitter
              quads leaked into the render as giant beige planes. */}
          <Environment resolution={256}>
            <Lightformer intensity={2.6} color="#ffd7b0" position={[-3, 4, 2]} scale={[8, 8, 1]} />
            <Lightformer intensity={1.1} color="#9fb8d8" position={[4, 2, -3]} scale={[6, 6, 1]} />
            <Lightformer intensity={0.5} color="#ffffff" position={[0, -3, 2]} scale={[10, 4, 1]} />
          </Environment>

          <ambientLight intensity={0.35} />
          <spotLight
            position={[-3.4, 6.2, 3.4]}
            angle={0.52}
            penumbra={0.9}
            intensity={68}
            color="#ffe0c0"
            castShadow
            shadow-mapSize={[1024, 1024]}
            shadow-bias={-0.0006}
          />
          <directionalLight position={[4, 3, -4]} intensity={1.5} color="#8fb0d8" />

          <Suspense fallback={null}>
            <Carousel {...props} />
          </Suspense>
        </Canvas>
      </GLBoundary>
    </div>
  );
}
