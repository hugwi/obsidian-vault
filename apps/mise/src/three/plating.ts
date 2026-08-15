/* Generative plating.

   A chef plates on a spiral: sauce down first, the mass slightly off-centre,
   garnish scattered wide with a bias toward the near edge. Phyllotaxis — the
   golden-angle spiral leaves use to avoid shading each other — produces exactly
   that distribution, so it is what places every element here.

   Everything is derived from a seed on the recipe id, so a dish plates the same
   way on every load and across the carousel, the reel and the cook view. */

import type { PlateForm, PlateLayer, Recipe } from '../data/recipes';

const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5));

/* Tuned against the render, not the spreadsheet: at the camera distance the
   carousel actually uses, the recipe-authored sizes plate a dish that reads as
   scattered dots rather than food. One gain here keeps every recipe's relative
   proportions intact. */
const SIZE_GAIN = 1.34;

/** mulberry32 — small, fast, and good enough for jitter. */
function rng(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function seedFrom(text: string): number {
  let h = 2166136261;
  for (let i = 0; i < text.length; i++) {
    h ^= text.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

export interface Placement {
  position: [number, number, number];
  rotation: [number, number, number];
  scale: [number, number, number];
}

export interface PlacedLayer {
  form: PlateForm;
  color: string;
  roughness: number;
  sheen: number;
  size: number;
  placements: Placement[];
}

/**
 * A single element's own footprint, so a layer of 40 sesame seeds and a layer of
 * 5 cabbage leaves both sit inside the vessel instead of one of them hanging
 * over the rim.
 */
const FOOTPRINT: Record<PlateForm, number> = {
  sauce: 1,
  dome: 1,
  disc: 1.05,
  sphere: 1,
  torus: 1.3,
  strand: 1.5,
  shard: 1.25,
  cube: 1.05,
  crumb: 1,
};

/** Half-height of one element, so it rests on the surface rather than in it. */
const REST: Record<PlateForm, number> = {
  sauce: 0,
  dome: 0,
  disc: 0.14,
  sphere: 1,
  torus: 0.34,
  strand: 0.09,
  shard: 0.32,
  cube: 0.42,
  crumb: 0.6,
};

export function plateLayer(layer: PlateLayer, seed: number, detail = 1): PlacedLayer {
  const rand = rng(seed);
  const count = Math.max(1, Math.round(layer.count * detail));
  const placements: Placement[] = [];
  const size = layer.form === 'sauce' ? layer.spread : layer.size * SIZE_GAIN;
  const rise = layer.rise * 1.18;

  // A pool and a mound are one element each: they sit, they do not scatter.
  if (layer.form === 'sauce' || layer.form === 'dome') {
    const drift = layer.form === 'dome' ? 0.06 : 0.02;
    placements.push({
      position: [(rand() - 0.5) * drift, rise, (rand() - 0.5) * drift],
      rotation: [0, rand() * Math.PI * 2, 0],
      scale: [1, 1, 1],
    });
    return {
      form: layer.form,
      color: layer.color,
      roughness: layer.roughness ?? 0.6,
      sheen: layer.sheen ?? 0,
      size,
      placements,
    };
  }

  const reach = Math.max(0.04, layer.spread - size * FOOTPRINT[layer.form] * 0.5);

  for (let i = 0; i < count; i++) {
    // sqrt keeps the spiral area-uniform instead of crowding the centre
    const r = reach * Math.sqrt((i + 0.6) / count);
    const theta = i * GOLDEN_ANGLE + rand() * 0.28;

    const x = Math.cos(theta) * r;
    const z = Math.sin(theta) * r;

    // Elements toward the rim sit slightly lower — food slumps outward, but
    // never through the plate: without a floor a laid-down wedge hangs below
    // the vessel and reads as a bug rather than as plating.
    const slump = (r / Math.max(reach, 0.001)) ** 2 * size * 0.35;
    const y = Math.max(REST[layer.form] * size, rise - slump + (rand() - 0.5) * size * 0.18);

    const variance = 0.78 + rand() * 0.44;

    /* Wedges, leaves and blistered peppers are laid down pointing away from the
       centre — that is how a cook fans them, and it is the difference between a
       plated dish and a pile. Everything else tumbles. */
    const rotation: [number, number, number] =
      layer.form === 'shard'
        ? [Math.PI / 2 + (rand() - 0.5) * 0.5, -theta + (rand() - 0.5) * 0.4, (rand() - 0.5) * 0.3]
        : [
            (rand() - 0.5) * (layer.form === 'crumb' ? Math.PI : 0.9),
            rand() * Math.PI * 2,
            (rand() - 0.5) * (layer.form === 'crumb' ? Math.PI : 0.9),
          ];

    placements.push({
      position: [x, y, z],
      rotation,
      scale: [variance, variance, variance],
    });
  }

  return {
    form: layer.form,
    color: layer.color,
    roughness: layer.roughness ?? 0.6,
    sheen: layer.sheen ?? 0,
    size,
    placements,
  };
}

/**
 * `detail` thins out scatter layers for plates far from focus. The dish keeps
 * its silhouette and colour; it just stops paying for 40 sesame seeds nobody
 * can resolve at that distance.
 */
export function plateRecipe(recipe: Recipe, detail = 1): PlacedLayer[] {
  const base = seedFrom(recipe.id);
  return recipe.plate.map((layer, i) => plateLayer(layer, base + i * 7919, detail));
}

/** Vessel silhouettes, as lathe profiles in the XY plane (x = radius). */
export function vesselProfile(vessel: Recipe['vessel']): Array<[number, number]> {
  switch (vessel) {
    case 'bowl':
      return [
        [0, 0],
        [0.28, 0.012],
        [0.52, 0.06],
        [0.7, 0.15],
        [0.82, 0.27],
        [0.88, 0.38],
        [0.9, 0.4],
        [0.87, 0.39],
        [0.8, 0.28],
        [0.67, 0.16],
        [0.48, 0.075],
        [0.24, 0.03],
        [0, 0.018],
      ];
    case 'pan':
      return [
        [0, 0],
        [0.5, 0.004],
        [0.78, 0.02],
        [0.86, 0.1],
        [0.88, 0.24],
        [0.9, 0.26],
        [0.86, 0.25],
        [0.84, 0.1],
        [0.76, 0.045],
        [0.46, 0.028],
        [0, 0.024],
      ];
    case 'plate':
    default:
      return [
        [0, 0],
        [0.36, 0.008],
        [0.6, 0.028],
        [0.76, 0.07],
        [0.88, 0.115],
        [0.94, 0.128],
        [0.92, 0.122],
        [0.8, 0.082],
        [0.62, 0.045],
        [0.34, 0.026],
        [0, 0.02],
      ];
  }
}
