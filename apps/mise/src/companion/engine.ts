/* The companion.

   This is a deterministic, offline engine: it reads the catalogue, not a model.
   That is a deliberate choice for a shipped demo — it never stalls, never needs
   a key, and never invents a step that would ruin someone's dinner.

   THE SEAM: everything below implements `CompanionEngine`. To put a real model
   behind the panel, write a second implementation of that one interface and pass
   it to `<ChatPanel engine={...} />`. The reply shape is what the UI animates
   against, so a model-backed engine must return the same `moves` — that is what
   keeps "something vegetarian, twenty minutes" driving the carousel instead of
   just printing a paragraph. */

import type { Recipe } from '../data/recipes';

export type Move =
  | { kind: 'shelf'; ids: string[]; label: string }
  | { kind: 'focus'; id: string }
  | { kind: 'cook'; id: string }
  | { kind: 'step'; delta: number }
  | { kind: 'servings'; count: number }
  | { kind: 'browse' };

export interface CompanionContext {
  /** the full catalogue, never the filtered shelf */
  catalogue: Recipe[];
  /** what the shelf is showing right now */
  shelfIds: string[];
  focused: Recipe | null;
  cooking: boolean;
  stepIndex: number;
  servings: number;
}

export interface CompanionReply {
  say: string;
  moves: Move[];
  /** offered as tappable follow-ups under the reply */
  suggestions?: string[];
}

export interface CompanionEngine {
  respond(input: string, ctx: CompanionContext): Promise<CompanionReply>;
  greeting(ctx: CompanionContext): CompanionReply;
}

/* ---- Reading the request ------------------------------------------------- */

const NUMBER_WORDS: Record<string, number> = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  eight: 8,
  ten: 10,
  twelve: 12,
  fifteen: 15,
  twenty: 20,
  thirty: 30,
  forty: 40,
  fifty: 50,
  sixty: 60,
  ninety: 90,
};

function numberIn(text: string): number | null {
  const digits = text.match(/\b(\d{1,3})\b/);
  if (digits) return Number(digits[1]);
  for (const [word, value] of Object.entries(NUMBER_WORDS)) {
    if (new RegExp(`\\b${word}\\b`).test(text)) return value;
  }
  return null;
}

interface Constraints {
  maxMinutes?: number;
  diet?: Recipe['diet'][number];
  effort?: Recipe['effort'];
  terms: string[];
}

const DIET_WORDS: Array<[RegExp, Recipe['diet'][number]]> = [
  [/\bvegan\b|\bplant[- ]based\b|\bno dairy and no meat\b/, 'vegan'],
  [/\bvegetarian\b|\bveggie\b|\bmeat[- ]free\b|\bno meat\b/, 'vegetarian'],
  [/\bpescatarian\b|\bfish\b|\bseafood\b/, 'pescatarian'],
  [/\bgluten[- ]free\b|\bno gluten\b|\bcoeliac\b|\bceliac\b/, 'gluten-free'],
  [/\bdairy[- ]free\b|\bno dairy\b|\blactose\b/, 'dairy-free'],
  [/\bmeat\b|\bmeaty\b|\bchicken\b(?!.*\bno\b)/, 'meat'],
];

function readConstraints(text: string): Constraints {
  const t = text.toLowerCase();
  const constraints: Constraints = { terms: [] };

  if (/\b(quick|fast|hurry|rush|no time|weeknight|tonight|30 min|under)\b/.test(t)) {
    constraints.maxMinutes = 30;
  }
  const minutes = /\b(min|minute|minutes|hour|hours)\b/.test(t) ? numberIn(t) : null;
  if (minutes) {
    constraints.maxMinutes = /\bhour/.test(t) ? minutes * 60 : minutes;
  }

  for (const [pattern, diet] of DIET_WORDS) {
    if (pattern.test(t)) {
      constraints.diet = diet;
      break;
    }
  }

  if (/\b(easy|simple|lazy|effortless|low effort|can't be bothered)\b/.test(t)) {
    constraints.effort = 'easy';
  }
  if (/\b(impress|show off|project|proper|technique|challenge)\b/.test(t)) {
    constraints.effort = 'involved';
  }

  constraints.terms = t
    .replace(/[^a-z0-9\s-]/g, ' ')
    .split(/\s+/)
    .filter((w) => w.length > 2 && !STOP.has(w));

  return constraints;
}

const STOP = new Set([
  'the','and','for','with','you','can','get','got','have','has','want','need','something','some',
  'make','cook','show','find','give','like','love','what','whats','that','this','there','here',
  'about','from','into','just','only','more','less','very','really','please','would','could',
  'should','anything','recipe','recipes','dish','dishes','food','dinner','lunch','meal','idea',
  'ideas','tonight','today','maybe','how','many','much','long','does','take','are','was','not',
]);

function scoreRecipe(recipe: Recipe, c: Constraints): number {
  if (c.maxMinutes !== undefined && recipe.minutes > c.maxMinutes) return -1;
  if (c.diet && !recipe.diet.includes(c.diet)) return -1;

  let score = 1;
  if (c.effort && recipe.effort === c.effort) score += 3;

  const haystack = [
    recipe.name,
    recipe.line,
    recipe.tags.join(' '),
    recipe.diet.join(' '),
    recipe.ingredients.map((i) => i.item).join(' '),
  ]
    .join(' ')
    .toLowerCase();

  for (const term of c.terms) {
    if (haystack.includes(term)) score += 2;
  }
  if (c.maxMinutes !== undefined) score += Math.max(0, 3 - recipe.minutes / 15);
  return score;
}

/* ---- Substitutions -------------------------------------------------------
   Honest swaps only, each with the consequence stated. A companion that says
   "sure, use anything" is worse than one that says nothing. */

const SWAPS: Array<[RegExp, string]> = [
  [/sesame paste|tahini/, 'Tahini for Chinese sesame paste works — it is less roasted, so add a pinch of sugar and a few drops of toasted sesame oil to close the gap.'],
  [/pecorino/, 'Parmesan for pecorino is fine but milder and less salty. Use a little more, and hold back on salting the water.'],
  [/carnaroli|arborio/, 'Arborio for carnaroli: creamier, less forgiving. Pull it a minute earlier — it goes from al dente to porridge fast.'],
  [/saffron/, 'No saffron, no substitute worth making. Turmeric gives you the colour and none of the perfume — better to cook it as a plain parmesan risotto and own it.'],
  [/miso/, 'Miso can go: double the salt in the butter and add a teaspoon of soy. You lose the ferment, you keep the lacquer.'],
  [/chilli crisp|chili crisp/, 'Chilli crisp swap: chilli flakes bloomed in hot neutral oil with a sliced garlic clove. Two minutes, and it keeps for weeks.'],
  [/buttermilk|creme fraiche|crème fraîche/, 'Yoghurt loosened with lemon juice stands in. Same acidity, slightly thinner.'],
  [/feta/, 'Feta out, ricotta salata or a firm goat cheese in. Both bring the salt; ricotta salata crumbles more like the original.'],
  [/butter/, 'Olive oil for butter changes the dish rather than breaking it — you lose the browning, so lean harder on the salt and acid.'],
  [/shishito/, 'Padrón peppers are the same game with a hotter average. Failing that, halved sweet mini peppers blister well but stay sweet.'],
];

/* ---- Voice ---------------------------------------------------------------- */

const listNames = (recipes: Recipe[]): string =>
  recipes.length === 1
    ? recipes[0].name
    : `${recipes.slice(0, -1).map((r) => r.name).join(', ')} and ${recipes[recipes.length - 1].name}`;

function describeConstraints(c: Constraints): string {
  const parts: string[] = [];
  if (c.diet) parts.push(c.diet);
  if (c.maxMinutes !== undefined) parts.push(`under ${c.maxMinutes} minutes`);
  if (c.effort === 'easy') parts.push('low effort');
  if (c.effort === 'involved') parts.push('worth the effort');
  return parts.join(', ');
}

function findByName(text: string, catalogue: Recipe[]): Recipe | null {
  const t = text.toLowerCase();
  let best: { recipe: Recipe; hits: number } | null = null;
  for (const recipe of catalogue) {
    const words = recipe.name
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, ' ')
      .split(/\s+/)
      .filter((w) => w.length > 3);
    const hits = words.filter((w) => t.includes(w)).length;
    if (hits > 0 && (!best || hits > best.hits)) best = { recipe, hits };
  }
  return best ? best.recipe : null;
}

/* ---- The engine ----------------------------------------------------------- */

export const localEngine: CompanionEngine = {
  greeting(ctx) {
    return {
      say: `${ctx.catalogue.length} dishes on the shelf. Tell me what kind of evening it is and I will cut it down.`,
      moves: [],
      suggestions: ['Something vegetarian, 20 minutes', 'I want to impress someone', 'What uses noodles?'],
    };
  },

  async respond(input, ctx) {
    const t = input.toLowerCase().trim();

    if (!t) {
      return { say: 'Still here. What are we making?', moves: [] };
    }

    /* --- in-cook navigation comes first: while you are at the stove, "next"
           means the next step, not a new recipe. --- */
    if (ctx.cooking && ctx.focused) {
      const recipe = ctx.focused;

      if (/\b(next|done|ready|continue|go on|then what)\b/.test(t)) {
        const last = ctx.stepIndex >= recipe.steps.length - 1;
        return last
          ? {
              say: `That is the last step. ${recipe.pairing}`,
              moves: [],
              suggestions: ['Back to the shelf'],
            }
          : {
              say: `Step ${ctx.stepIndex + 2}: ${recipe.steps[ctx.stepIndex + 1].title.toLowerCase()}.`,
              moves: [{ kind: 'step', delta: 1 }],
            };
      }

      if (/\b(back|previous|again|repeat|missed|what did you say)\b/.test(t)) {
        return ctx.stepIndex === 0
          ? { say: `We are still on the first step: ${recipe.steps[0].title.toLowerCase()}.`, moves: [] }
          : { say: 'Back one.', moves: [{ kind: 'step', delta: -1 }] };
      }

      if (/\bhow long\b|\bhow much longer\b|\btime left\b/.test(t)) {
        const remaining = recipe.steps
          .slice(ctx.stepIndex)
          .reduce((sum, s) => sum + (s.minutes ?? 0), 0);
        return {
          say: `About ${remaining} minutes left across ${recipe.steps.length - ctx.stepIndex} steps. This step is ${recipe.steps[ctx.stepIndex].minutes ?? 0}.`,
          moves: [],
        };
      }

      const servings = /\b(serve|serving|servings|people|portions|for)\b/.test(t) ? numberIn(t) : null;
      if (servings && servings > 0 && servings <= 24) {
        return {
          say: `Scaled to ${servings}. Timings stay put — only the quantities move.`,
          moves: [{ kind: 'servings', count: servings }],
        };
      }
      if (/\bdouble\b/.test(t)) {
        return {
          say: `Doubled to ${ctx.servings * 2}. Watch the pan size — crowding is what stops things browning.`,
          moves: [{ kind: 'servings', count: ctx.servings * 2 }],
        };
      }

      const missing = SWAPS.find(([pattern]) => pattern.test(t));
      if (missing && /\b(no|without|out of|don't have|dont have|instead of|swap|substitute|replace)\b/.test(t)) {
        return { say: missing[1], moves: [] };
      }

      if (/\b(shelf|back to|browse|different|something else|quit|stop)\b/.test(t)) {
        return { say: 'Back to the shelf.', moves: [{ kind: 'browse' }] };
      }
    }

    /* --- substitutions work outside cook mode too --- */
    const swap = SWAPS.find(([pattern]) => pattern.test(t));
    if (swap && /\b(no|without|out of|don't have|dont have|instead of|swap|substitute|replace)\b/.test(t)) {
      return { say: swap[1], moves: [] };
    }

    /* --- naming a dish --- */
    const named = findByName(t, ctx.catalogue);
    if (named) {
      const wantsToStart = /\b(make|cook|start|let's|lets|do it|go|begin)\b/.test(t);
      return wantsToStart
        ? {
            say: `${named.name}. ${named.steps.length} steps, ${named.minutes} minutes. Starting at step one.`,
            moves: [{ kind: 'focus', id: named.id }, { kind: 'cook', id: named.id }],
          }
        : {
            say: `${named.name} — ${named.line} ${named.minutes} minutes, serves ${named.servings}.`,
            moves: [{ kind: 'focus', id: named.id }],
            suggestions: [`Cook ${named.name.split(',')[0]}`, 'Show me something else'],
          };
    }

    if (/\b(cook|start|make) (it|this|that)\b|\blet's go\b|\bstart cooking\b/.test(t) && ctx.focused) {
      return {
        say: `${ctx.focused.name}. ${ctx.focused.steps.length} steps. I will hold your place.`,
        moves: [{ kind: 'cook', id: ctx.focused.id }],
      };
    }

    if (/\b(everything|all|reset|clear|start over|show all)\b/.test(t)) {
      return {
        say: `Whole shelf back, all ${ctx.catalogue.length}.`,
        moves: [{ kind: 'shelf', ids: ctx.catalogue.map((r) => r.id), label: 'Everything' }],
      };
    }

    if (/\b(hello|hi|hey|help|what can you)\b/.test(t)) {
      return {
        say: 'Give me a constraint — how long you have, what you will not eat, what is already in the fridge. I will narrow the shelf and talk you through whatever you pick.',
        moves: [],
        suggestions: ['Vegan, under 25 minutes', 'Something to impress', 'What can I make with eggs?'],
      };
    }

    /* --- otherwise: it is a search --- */
    const constraints = readConstraints(t);
    const ranked = ctx.catalogue
      .map((recipe) => ({ recipe, score: scoreRecipe(recipe, constraints) }))
      .filter((r) => r.score > 0)
      .sort((a, b) => b.score - a.score);

    const described = describeConstraints(constraints);

    if (ranked.length === 0) {
      return {
        say: described
          ? `Nothing on the shelf is ${described}. The closest I have is ${ctx.catalogue
              .slice()
              .sort((a, b) => a.minutes - b.minutes)[0].name.toLowerCase()} — loosen the time or the diet and I will try again.`
          : 'I did not catch a constraint I can act on. Try a time, a diet, or an ingredient.',
        moves: [],
        suggestions: ['Show me everything', 'Under 30 minutes', 'Vegetarian'],
      };
    }

    const shortlist = ranked.slice(0, Math.min(4, ranked.length)).map((r) => r.recipe);
    const top = shortlist[0];

    return {
      say:
        shortlist.length === 1
          ? `One match: ${top.name}. ${top.line}`
          : `${shortlist.length}${described ? ` ${described}` : ''}: ${listNames(shortlist)}. I would start with ${top.name.split(',')[0]} — ${top.minutes} minutes.`,
      moves: [
        { kind: 'shelf', ids: shortlist.map((r) => r.id), label: described || t },
        { kind: 'focus', id: top.id },
      ],
      suggestions: [`Cook ${top.name.split(',')[0]}`, 'Show me everything'],
    };
  },
};
