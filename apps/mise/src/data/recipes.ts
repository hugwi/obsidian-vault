/* The catalogue.

   Every dish carries a `plate`: an ordered list of edible forms that the 3D
   plating system builds into an actual composition. No photography — the dish
   you see on the carousel is geometry, lit in a studio, assembled from the same
   description a cook would give ("a bed of noodles, chilli oil pooled under,
   sesame scattered over"). It means a new recipe arrives plated, not waiting on
   a photo shoot. */

export type PlateForm =
  | 'sauce' /* a thin pool under everything */
  | 'dome' /* a mound: rice, mash, whipped anything */
  | 'disc' /* rounds: citrus, tortilla, seared scallop */
  | 'sphere' /* meatballs, tomatoes, olives, capers */
  | 'torus' /* rings: onion, calamari, bucatini coils */
  | 'strand' /* noodles, ribbons, shreds */
  | 'shard' /* leaves, chips, blistered peppers, crackling */
  | 'cube' /* tofu, roast potato, feta */
  | 'crumb'; /* dust: za'atar, sesame, chilli flake, cocoa */

export interface PlateLayer {
  form: PlateForm;
  /** hex, read straight into the material */
  color: string;
  count: number;
  /** how far across the vessel this layer spreads, 0–1 */
  spread: number;
  /** base scale of one element */
  size: number;
  /** how high above the vessel floor this layer sits */
  rise: number;
  roughness?: number;
  /** 0 matte, up to ~0.35 for anything glossed or oiled */
  sheen?: number;
}

export interface Ingredient {
  item: string;
  /** per the recipe's base serving count; scaled live in cook mode */
  qty: number | null;
  unit: string;
  note?: string;
}

export interface Step {
  title: string;
  body: string;
  /** drives the reel's timing ring and the step clock */
  minutes?: number;
  heat?: 'none' | 'low' | 'medium' | 'high';
}

export interface Recipe {
  id: string;
  name: string;
  /** one line, the cook's reason to make it */
  line: string;
  minutes: number;
  servings: number;
  effort: 'easy' | 'steady' | 'involved';
  diet: Array<'vegan' | 'vegetarian' | 'pescatarian' | 'meat' | 'gluten-free' | 'dairy-free'>;
  tags: string[];
  vessel: 'plate' | 'bowl' | 'board' | 'pan';
  /** rim and interior of the vessel itself */
  vesselColor: { rim: string; well: string };
  plate: PlateLayer[];
  ingredients: Ingredient[];
  steps: Step[];
  /** shown in cook mode as the companion's closing note */
  pairing: string;
}

export const RECIPES: Recipe[] = [
  {
    id: 'charred-cabbage',
    name: 'Charred Cabbage, Brown Butter, Capers',
    line: 'A whole wedge, blackened at the edges, drowned in nutty butter.',
    minutes: 35,
    servings: 2,
    effort: 'easy',
    diet: ['vegetarian', 'gluten-free'],
    tags: ['weeknight', 'one-pan', 'side-or-main'],
    vessel: 'plate',
    vesselColor: { rim: '#6f665e', well: '#585049' },
    plate: [
      { form: 'sauce', color: '#c98b3f', count: 1, spread: 0.72, size: 1, rise: 0.01, sheen: 0.34 },
      { form: 'shard', color: '#b7c39a', count: 5, spread: 0.34, size: 0.42, rise: 0.1, roughness: 0.72 },
      { form: 'shard', color: '#4a3a26', count: 6, spread: 0.36, size: 0.3, rise: 0.16, roughness: 0.55 },
      { form: 'sphere', color: '#6b7a4a', count: 14, spread: 0.5, size: 0.055, rise: 0.19, sheen: 0.3 },
      { form: 'crumb', color: '#e8dcc0', count: 26, spread: 0.56, size: 0.03, rise: 0.2 },
    ],
    ingredients: [
      { item: 'Savoy cabbage', qty: 1, unit: 'small head', note: 'cut into 4 wedges, core intact' },
      { item: 'Unsalted butter', qty: 90, unit: 'g' },
      { item: 'Capers in brine', qty: 2, unit: 'tbsp', note: 'drained, patted dry' },
      { item: 'Lemon', qty: 1, unit: '', note: 'half juiced, half to serve' },
      { item: 'Flat-leaf parsley', qty: 15, unit: 'g' },
      { item: 'Flaky salt', qty: null, unit: 'to taste' },
    ],
    steps: [
      {
        title: 'Dry the wedges',
        body: 'Pat the cut faces completely dry. Water is what stops a cabbage from charring — it steams instead.',
        minutes: 2,
        heat: 'none',
      },
      {
        title: 'Char hard, one side',
        body: 'Cast iron over high heat, a film of neutral oil, wedges cut-side down. Do not move them. You want black, not golden — the bitterness is the point.',
        minutes: 7,
        heat: 'high',
      },
      {
        title: 'Turn and soften',
        body: 'Flip to the second cut face, drop to medium, add a splash of water and cover. The wedge should give to a knife tip at the core.',
        minutes: 12,
        heat: 'medium',
      },
      {
        title: 'Brown the butter',
        body: 'Separate pan, butter over medium. It will foam, quiet down, then smell of hazelnut. The moment the solids go amber, kill the heat.',
        minutes: 5,
        heat: 'medium',
      },
      {
        title: 'Crisp the capers, finish',
        body: 'Capers into the hot butter for 30 seconds until they bloom open. Lemon juice off the heat. Pour over the wedges, parsley, flaky salt.',
        minutes: 3,
        heat: 'low',
      },
    ],
    pairing: 'A cold, bone-dry riesling. The butter needs the acid.',
  },
  {
    id: 'sesame-noodles',
    name: 'Cold Sesame Noodles, Chilli Crisp',
    line: 'Twenty minutes, no heat past boiling water, better cold the next day.',
    minutes: 20,
    servings: 2,
    effort: 'easy',
    diet: ['vegan', 'dairy-free'],
    tags: ['weeknight', 'no-cook-sauce', 'make-ahead', 'spicy'],
    vessel: 'bowl',
    vesselColor: { rim: '#5f5d69', well: '#4a4954' },
    plate: [
      { form: 'sauce', color: '#8a3a17', count: 1, spread: 0.66, size: 1, rise: 0.01, sheen: 0.35 },
      { form: 'strand', color: '#e2c98c', count: 18, spread: 0.44, size: 0.5, rise: 0.12, roughness: 0.42 },
      { form: 'strand', color: '#7fa05a', count: 7, spread: 0.4, size: 0.3, rise: 0.22, roughness: 0.5 },
      { form: 'sphere', color: '#c4442a', count: 10, spread: 0.42, size: 0.045, rise: 0.24, sheen: 0.32 },
      { form: 'crumb', color: '#f0e2c2', count: 34, spread: 0.46, size: 0.028, rise: 0.25 },
    ],
    ingredients: [
      { item: 'Wheat noodles', qty: 200, unit: 'g', note: 'thin, straight' },
      { item: 'Chinese sesame paste', qty: 3, unit: 'tbsp', note: 'tahini works, add a pinch more sugar' },
      { item: 'Light soy sauce', qty: 2, unit: 'tbsp' },
      { item: 'Chinkiang black vinegar', qty: 1, unit: 'tbsp' },
      { item: 'Chilli crisp', qty: 2, unit: 'tbsp' },
      { item: 'Garlic', qty: 2, unit: 'cloves', note: 'grated to a paste' },
      { item: 'Cucumber', qty: 1, unit: '', note: 'julienned' },
      { item: 'Spring onion', qty: 3, unit: '' },
    ],
    steps: [
      {
        title: 'Loosen the paste',
        body: 'Sesame paste in a bowl. Add warm water a tablespoon at a time, whisking. It will seize and look broken before it turns glossy — keep going.',
        minutes: 3,
        heat: 'none',
      },
      {
        title: 'Build the sauce',
        body: 'Soy, vinegar, garlic, half the chilli crisp. Taste. It should be louder than you think — the noodles will mute it.',
        minutes: 2,
        heat: 'none',
      },
      {
        title: 'Boil and shock',
        body: 'Noodles to package time, then straight into cold water. Drain hard. Wet noodles dilute the sauce into nothing.',
        minutes: 6,
        heat: 'high',
      },
      {
        title: 'Toss and top',
        body: 'Noodles through the sauce with your hands, not tongs. Cucumber, spring onion, the rest of the chilli crisp on top.',
        minutes: 3,
        heat: 'none',
      },
    ],
    pairing: 'Cold lager, or barley tea if you are eating this at 11pm.',
  },
  {
    id: 'shakshuka',
    name: 'Shakshuka, Feta and Za’atar',
    line: 'One pan, eggs set in a spiced tomato, torn bread mandatory.',
    minutes: 30,
    servings: 3,
    effort: 'easy',
    diet: ['vegetarian'],
    tags: ['brunch', 'one-pan', 'weeknight'],
    vessel: 'pan',
    vesselColor: { rim: '#4a4139', well: '#332a23' },
    plate: [
      { form: 'sauce', color: '#a8321c', count: 1, spread: 0.82, size: 1, rise: 0.01, sheen: 0.28 },
      { form: 'disc', color: '#f2c14a', count: 3, spread: 0.4, size: 0.16, rise: 0.06, sheen: 0.33 },
      { form: 'cube', color: '#f4efe4', count: 11, spread: 0.56, size: 0.07, rise: 0.09, roughness: 0.85 },
      { form: 'shard', color: '#5e8a3f', count: 9, spread: 0.6, size: 0.14, rise: 0.11, roughness: 0.7 },
      { form: 'crumb', color: '#7d6a2e', count: 30, spread: 0.62, size: 0.03, rise: 0.12 },
    ],
    ingredients: [
      { item: 'Plum tomatoes', qty: 800, unit: 'g', note: 'tinned, crushed by hand' },
      { item: 'Red peppers', qty: 2, unit: '', note: 'sliced thin' },
      { item: 'Onion', qty: 1, unit: 'large' },
      { item: 'Garlic', qty: 4, unit: 'cloves' },
      { item: 'Ground cumin', qty: 2, unit: 'tsp' },
      { item: 'Sweet paprika', qty: 1, unit: 'tbsp' },
      { item: 'Eggs', qty: 6, unit: '' },
      { item: 'Feta', qty: 120, unit: 'g' },
      { item: "Za'atar", qty: 1, unit: 'tbsp' },
    ],
    steps: [
      {
        title: 'Sweat, do not colour',
        body: 'Onion and peppers in olive oil over medium-low with a good pinch of salt. Fifteen minutes, until collapsed and sweet.',
        minutes: 15,
        heat: 'low',
      },
      {
        title: 'Bloom the spice',
        body: 'Garlic, cumin and paprika into the empty side of the pan for 40 seconds. Dry spice in oil is what makes this taste cooked rather than assembled.',
        minutes: 1,
        heat: 'medium',
      },
      {
        title: 'Reduce',
        body: 'Tomatoes in, crushed by hand. Simmer until a spoon dragged through leaves a channel that holds for two seconds.',
        minutes: 10,
        heat: 'medium',
      },
      {
        title: 'Set the eggs',
        body: 'Make wells, crack an egg into each, cover. Pull the pan the moment the whites go opaque — carryover heat finishes the yolks.',
        minutes: 6,
        heat: 'low',
      },
      {
        title: 'Finish cold',
        body: 'Off the heat: crumbled feta, za’atar, olive oil, torn herbs. The cold toppings against the hot pan is the whole trick.',
        minutes: 1,
        heat: 'none',
      },
    ],
    pairing: 'Strong coffee if it is morning, orange wine if it is not.',
  },
  {
    id: 'cacio-e-pepe',
    name: 'Cacio e Pepe',
    line: 'Four ingredients and nowhere to hide.',
    minutes: 15,
    servings: 2,
    effort: 'involved',
    diet: ['vegetarian'],
    tags: ['weeknight', 'fast', 'technique'],
    vessel: 'bowl',
    vesselColor: { rim: '#6b6459', well: '#544e45' },
    plate: [
      { form: 'sauce', color: '#e8dfc6', count: 1, spread: 0.6, size: 1, rise: 0.01, sheen: 0.3 },
      { form: 'torus', color: '#e6cf95', count: 9, spread: 0.34, size: 0.15, rise: 0.13, roughness: 0.45 },
      { form: 'strand', color: '#eed9a4', count: 12, spread: 0.36, size: 0.42, rise: 0.18, roughness: 0.44 },
      { form: 'crumb', color: '#2a2622', count: 40, spread: 0.4, size: 0.025, rise: 0.24 },
    ],
    ingredients: [
      { item: 'Tonnarelli or spaghetti', qty: 200, unit: 'g' },
      { item: 'Pecorino Romano', qty: 120, unit: 'g', note: 'grated to a powder, not shavings' },
      { item: 'Black peppercorns', qty: 2, unit: 'tsp', note: 'coarsely cracked' },
      { item: 'Salt', qty: null, unit: 'for the water' },
    ],
    steps: [
      {
        title: 'Toast the pepper',
        body: 'Cracked pepper in a dry wide pan over medium until it smells sharp. This is half the dish and the step everyone skips.',
        minutes: 2,
        heat: 'medium',
      },
      {
        title: 'Undercook the pasta',
        body: 'Salt the water less than usual — pecorino brings plenty. Pull the pasta two minutes shy. Save two cups of water.',
        minutes: 7,
        heat: 'high',
      },
      {
        title: 'Make the cream',
        body: 'Pecorino with a few tablespoons of cooled pasta water into a paste. Cooled matters: boiling water on cheese gives you a stringy clump.',
        minutes: 2,
        heat: 'none',
      },
      {
        title: 'Emulsify off the heat',
        body: 'Pasta into the pepper pan with a ladle of water, toss hard, then off the heat entirely before the cheese goes in. Agitate until it turns glossy.',
        minutes: 3,
        heat: 'none',
      },
    ],
    pairing: 'Whatever red is open. This dish does not care.',
  },
  {
    id: 'miso-chicken',
    name: 'Miso Butter Roast Chicken',
    line: 'Lacquered skin, a bird you can hear from the next room.',
    minutes: 95,
    servings: 4,
    effort: 'steady',
    diet: ['meat', 'gluten-free'],
    tags: ['sunday', 'roast', 'leftovers'],
    vessel: 'board',
    vesselColor: { rim: '#7a5a3c', well: '#63472e' },
    plate: [
      { form: 'dome', color: '#b06a2a', count: 1, spread: 0.3, size: 0.46, rise: 0.06, sheen: 0.35 },
      { form: 'disc', color: '#c98f45', count: 6, spread: 0.5, size: 0.11, rise: 0.06, sheen: 0.3 },
      { form: 'shard', color: '#7d9a4e', count: 7, spread: 0.56, size: 0.16, rise: 0.1, roughness: 0.68 },
      { form: 'sauce', color: '#7a4a1e', count: 1, spread: 0.7, size: 1, rise: 0.005, sheen: 0.36 },
      { form: 'crumb', color: '#efe4cc', count: 18, spread: 0.5, size: 0.03, rise: 0.14 },
    ],
    ingredients: [
      { item: 'Whole chicken', qty: 1.6, unit: 'kg' },
      { item: 'White miso', qty: 3, unit: 'tbsp' },
      { item: 'Softened butter', qty: 80, unit: 'g' },
      { item: 'Garlic', qty: 3, unit: 'cloves', note: 'grated' },
      { item: 'Lemon', qty: 1, unit: '' },
      { item: 'Waxy potatoes', qty: 600, unit: 'g', note: 'halved' },
      { item: 'Thyme', qty: 6, unit: 'sprigs' },
    ],
    steps: [
      {
        title: 'Dry-brine, uncovered',
        body: 'Salt the bird generously and leave it uncovered in the fridge. Overnight is best, an hour is worth it. Dry skin is crisp skin.',
        minutes: 60,
        heat: 'none',
      },
      {
        title: 'Miso butter under the skin',
        body: 'Mash miso, butter and garlic. Work your fingers between skin and breast and push two-thirds of it in there. The rest goes on top.',
        minutes: 8,
        heat: 'none',
      },
      {
        title: 'High, then moderate',
        body: '220°C for 20 minutes to set the skin, then down to 180°C. Potatoes and thyme into the fat around the bird when you drop the heat.',
        minutes: 55,
        heat: 'high',
      },
      {
        title: 'Rest, properly',
        body: '65°C at the thickest part of the thigh. Rest 20 minutes on the board — the juices need somewhere to go that is not your carving board.',
        minutes: 20,
        heat: 'none',
      },
    ],
    pairing: 'The pan juices, spooned over everything. Nothing else required.',
  },
  {
    id: 'shishito-tofu',
    name: 'Blistered Shishito, Whipped Tofu',
    line: 'One in ten peppers is hot. That is the game.',
    minutes: 18,
    servings: 2,
    effort: 'easy',
    diet: ['vegan', 'dairy-free', 'gluten-free'],
    tags: ['fast', 'snack', 'high-heat'],
    vessel: 'plate',
    vesselColor: { rim: '#5c6357', well: '#474d44' },
    plate: [
      { form: 'dome', color: '#f2ece0', count: 1, spread: 0.2, size: 0.4, rise: 0.03, roughness: 0.9 },
      { form: 'shard', color: '#4f7a33', count: 11, spread: 0.46, size: 0.26, rise: 0.12, sheen: 0.32 },
      { form: 'shard', color: '#2c3d1e', count: 5, spread: 0.42, size: 0.2, rise: 0.16, sheen: 0.3 },
      { form: 'crumb', color: '#d8b34a', count: 22, spread: 0.5, size: 0.028, rise: 0.18 },
      { form: 'sauce', color: '#caa53c', count: 1, spread: 0.54, size: 1, rise: 0.008, sheen: 0.36 },
    ],
    ingredients: [
      { item: 'Shishito peppers', qty: 250, unit: 'g' },
      { item: 'Silken tofu', qty: 300, unit: 'g' },
      { item: 'Tahini', qty: 2, unit: 'tbsp' },
      { item: 'Lemon', qty: 1, unit: '' },
      { item: 'Rice vinegar', qty: 2, unit: 'tsp' },
      { item: 'Toasted sesame oil', qty: 1, unit: 'tbsp' },
      { item: 'Flaky salt', qty: null, unit: 'to finish' },
    ],
    steps: [
      {
        title: 'Whip the tofu',
        body: 'Silken tofu, tahini, lemon, vinegar and a good pinch of salt in a blender until it is genuinely aerated — a full minute, not ten seconds.',
        minutes: 4,
        heat: 'none',
      },
      {
        title: 'Get the pan too hot',
        body: 'Dry cast iron until it is just short of smoking. Peppers in a single layer, no oil yet. You want blisters, not a sauté.',
        minutes: 5,
        heat: 'high',
      },
      {
        title: 'Toss and blister',
        body: 'Move them only when the skins bubble and blacken. Four minutes total. A splash of sesame oil in the last thirty seconds.',
        minutes: 4,
        heat: 'high',
      },
      {
        title: 'Spoon, pile, salt',
        body: 'Tofu spread across the plate with the back of a spoon. Peppers piled on. Flaky salt from a height.',
        minutes: 2,
        heat: 'none',
      },
    ],
    pairing: 'Something cold and carbonated. The heat arrives late.',
  },
  {
    id: 'fish-tacos',
    name: 'Fish Tacos, Charred Pineapple',
    line: 'Sweet, smoke and acid, folded into a warm tortilla.',
    minutes: 40,
    servings: 4,
    effort: 'steady',
    diet: ['pescatarian', 'dairy-free'],
    tags: ['weekend', 'grill', 'crowd'],
    vessel: 'board',
    vesselColor: { rim: '#78573a', well: '#5f422a' },
    plate: [
      { form: 'disc', color: '#e9d9b0', count: 3, spread: 0.44, size: 0.28, rise: 0.03, roughness: 0.8 },
      { form: 'cube', color: '#e8e2d4', count: 12, spread: 0.4, size: 0.075, rise: 0.1, roughness: 0.6 },
      { form: 'cube', color: '#e0a92c', count: 10, spread: 0.42, size: 0.06, rise: 0.14, sheen: 0.31 },
      { form: 'strand', color: '#8fae55', count: 9, spread: 0.4, size: 0.24, rise: 0.17, roughness: 0.6 },
      { form: 'sphere', color: '#b8342a', count: 8, spread: 0.46, size: 0.04, rise: 0.19, sheen: 0.33 },
      { form: 'crumb', color: '#3f6a34', count: 24, spread: 0.48, size: 0.026, rise: 0.2 },
    ],
    ingredients: [
      { item: 'Firm white fish', qty: 600, unit: 'g', note: 'cod, hake or halibut' },
      { item: 'Pineapple', qty: 0.5, unit: '', note: 'thick rings' },
      { item: 'Corn tortillas', qty: 12, unit: '' },
      { item: 'Red cabbage', qty: 200, unit: 'g', note: 'shredded fine' },
      { item: 'Lime', qty: 3, unit: '' },
      { item: 'Chipotle in adobo', qty: 2, unit: 'tbsp' },
      { item: 'Coriander', qty: 20, unit: 'g' },
      { item: 'Red onion', qty: 1, unit: 'small' },
    ],
    steps: [
      {
        title: 'Quick-pickle the onion',
        body: 'Sliced onion, juice of a lime, a pinch of salt and sugar. Twenty minutes turns it pink and takes the raw edge off.',
        minutes: 3,
        heat: 'none',
      },
      {
        title: 'Marinate briefly',
        body: 'Fish with chipotle, lime and oil. Fifteen minutes, no longer — citrus will start cooking the flesh and it goes chalky.',
        minutes: 15,
        heat: 'none',
      },
      {
        title: 'Char the pineapple first',
        body: 'Pineapple rings on the hottest part of the grill until properly caught. Off, chop, keep the juice that pools.',
        minutes: 8,
        heat: 'high',
      },
      {
        title: 'Grill the fish, then flake',
        body: 'Three minutes a side, no fussing. Flake into rough pieces — smaller than a fillet, bigger than a shred.',
        minutes: 7,
        heat: 'high',
      },
      {
        title: 'Warm the tortillas',
        body: 'Straight on the flame, ten seconds a side, into a folded towel. A cold tortilla ruins a good taco more reliably than bad fish.',
        minutes: 5,
        heat: 'high',
      },
    ],
    pairing: 'A margarita with more lime than the recipe says.',
  },
  {
    id: 'olive-oil-cake',
    name: 'Dark Chocolate Olive Oil Cake',
    line: 'One bowl, no mixer, better on the second day.',
    minutes: 55,
    servings: 8,
    effort: 'easy',
    diet: ['vegetarian', 'dairy-free'],
    tags: ['baking', 'make-ahead', 'crowd'],
    vessel: 'plate',
    vesselColor: { rim: '#67605a', well: '#514b46' },
    plate: [
      { form: 'dome', color: '#3a231a', count: 1, spread: 0.26, size: 0.5, rise: 0.05, roughness: 0.82 },
      { form: 'sauce', color: '#20120d', count: 1, spread: 0.5, size: 1, rise: 0.01, sheen: 0.34 },
      { form: 'sphere', color: '#8e2f3f', count: 9, spread: 0.44, size: 0.05, rise: 0.16, sheen: 0.33 },
      { form: 'crumb', color: '#d9c9ad', count: 30, spread: 0.46, size: 0.03, rise: 0.2 },
    ],
    ingredients: [
      { item: 'Dark chocolate', qty: 200, unit: 'g', note: '70%, chopped' },
      { item: 'Extra virgin olive oil', qty: 180, unit: 'ml', note: 'a fruity one, not the harsh stuff' },
      { item: 'Caster sugar', qty: 200, unit: 'g' },
      { item: 'Eggs', qty: 3, unit: '' },
      { item: 'Plain flour', qty: 120, unit: 'g' },
      { item: 'Cocoa powder', qty: 30, unit: 'g' },
      { item: 'Flaky salt', qty: 1, unit: 'tsp' },
    ],
    steps: [
      {
        title: 'Melt into the oil',
        body: 'Chocolate and olive oil together over a bain-marie. The oil keeps it fluid — no seizing, no tempering to worry about.',
        minutes: 6,
        heat: 'low',
      },
      {
        title: 'Whisk sugar and eggs to ribbon',
        body: 'Three full minutes by hand. When the whisk leaves a trail that sits on the surface for a count of three, stop.',
        minutes: 4,
        heat: 'none',
      },
      {
        title: 'Fold, do not beat',
        body: 'Chocolate into eggs, then the sifted dry in two additions. Stop the moment the last streak disappears.',
        minutes: 4,
        heat: 'none',
      },
      {
        title: 'Bake and underdo it',
        body: '170°C for 32 minutes. A skewer should come out with damp crumbs. Fully clean means you have gone too far.',
        minutes: 32,
        heat: 'medium',
      },
      {
        title: 'Salt while warm',
        body: 'Flaky salt over the top as it cools so it sticks. Then leave it alone until tomorrow if you can manage it.',
        minutes: 5,
        heat: 'none',
      },
    ],
    pairing: 'Black coffee, or a spoonful of crème fraîche if you have it.',
  },
  {
    id: 'saffron-risotto',
    name: 'Saffron Risotto',
    line: 'Eighteen minutes of stirring for something the colour of late sun.',
    minutes: 45,
    servings: 3,
    effort: 'involved',
    diet: ['vegetarian', 'gluten-free'],
    tags: ['technique', 'dinner-party', 'stovetop'],
    vessel: 'bowl',
    vesselColor: { rim: '#6d6459', well: '#544c43' },
    plate: [
      { form: 'sauce', color: '#e0a92c', count: 1, spread: 0.68, size: 1, rise: 0.01, sheen: 0.3 },
      { form: 'dome', color: '#eec24f', count: 1, spread: 0.22, size: 0.42, rise: 0.04, roughness: 0.78 },
      { form: 'crumb', color: '#f6efdc', count: 26, spread: 0.4, size: 0.03, rise: 0.16 },
      { form: 'shard', color: '#6e8f45', count: 5, spread: 0.36, size: 0.12, rise: 0.18, roughness: 0.65 },
    ],
    ingredients: [
      { item: 'Carnaroli rice', qty: 300, unit: 'g' },
      { item: 'Saffron', qty: 1, unit: 'large pinch' },
      { item: 'Vegetable stock', qty: 1.2, unit: 'l', note: 'kept at a bare simmer' },
      { item: 'Shallots', qty: 2, unit: '' },
      { item: 'Dry white wine', qty: 120, unit: 'ml' },
      { item: 'Parmesan', qty: 80, unit: 'g' },
      { item: 'Cold butter', qty: 60, unit: 'g', note: 'cubed, for the mantecatura' },
    ],
    steps: [
      {
        title: 'Bloom the saffron',
        body: 'Saffron into a ladle of warm stock. Give it ten minutes. Threads dropped in dry at the end give you colour but no perfume.',
        minutes: 10,
        heat: 'none',
      },
      {
        title: 'Toast the rice',
        body: 'Shallots soft in butter, then rice for two minutes until the grains turn translucent at the edge and chalky at the centre.',
        minutes: 4,
        heat: 'medium',
      },
      {
        title: 'Wine, then stock by the ladle',
        body: 'Wine until it disappears. Then stock one ladle at a time, stirring, adding the next only when the last is nearly gone.',
        minutes: 18,
        heat: 'medium',
      },
      {
        title: 'Mantecare off the heat',
        body: 'Off the heat. Cold butter and parmesan beaten in hard. This is where risotto becomes creamy — not from cream, from agitation.',
        minutes: 3,
        heat: 'none',
      },
      {
        title: "All'onda",
        body: 'Shake the pan. It should move in a slow wave. Too stiff, a splash of stock. Serve immediately — risotto does not wait.',
        minutes: 2,
        heat: 'none',
      },
    ],
    pairing: 'The rest of the white you opened for the pan.',
  },
];

export const byId = (id: string): Recipe | undefined => RECIPES.find((r) => r.id === id);
