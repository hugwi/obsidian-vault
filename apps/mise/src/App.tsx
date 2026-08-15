import { useCallback, useEffect, useMemo, useReducer, useRef } from 'react';
import { flushSync } from 'react-dom';
import { RECIPES, type Recipe } from './data/recipes';
import { localEngine, type CompanionContext, type Move } from './companion/engine';
import { Scene } from './three/Scene';
import { ChatPanel } from './ui/ChatPanel';
import { Shelf } from './ui/Shelf';
import { CookMode } from './ui/CookMode';

interface State {
  shelfIds: string[];
  shelfLabel: string | null;
  activeIndex: number;
  view: 'browse' | 'cook';
  stepIndex: number;
  servings: number;
  reelOpen: boolean;
}

type Action =
  | { type: 'select'; index: number }
  | { type: 'cook' }
  | { type: 'watch' }
  | { type: 'browse' }
  | { type: 'step'; delta: number }
  | { type: 'servings'; count: number }
  | { type: 'toggle-reel' }
  | { type: 'clear-filter' }
  | { type: 'moves'; moves: Move[] };

const ALL = RECIPES.map((r) => r.id);

const initial: State = {
  shelfIds: ALL,
  shelfLabel: null,
  activeIndex: 0,
  view: 'browse',
  stepIndex: 0,
  servings: RECIPES[0].servings,
  reelOpen: false,
};

const shelfOf = (ids: string[]): Recipe[] =>
  ids.map((id) => RECIPES.find((r) => r.id === id)).filter((r): r is Recipe => Boolean(r));

function clampIndex(index: number, length: number): number {
  if (length === 0) return 0;
  return Math.max(0, Math.min(length - 1, index));
}

function reduce(state: State, action: Action): State {
  switch (action.type) {
    case 'select':
      return { ...state, activeIndex: clampIndex(action.index, state.shelfIds.length) };

    case 'cook': {
      const recipe = shelfOf(state.shelfIds)[state.activeIndex];
      if (!recipe) return state;
      return { ...state, view: 'cook', stepIndex: 0, servings: recipe.servings, reelOpen: false };
    }

    case 'watch': {
      const recipe = shelfOf(state.shelfIds)[state.activeIndex];
      if (!recipe) return state;
      return { ...state, view: 'cook', stepIndex: 0, servings: recipe.servings, reelOpen: true };
    }

    case 'browse':
      return { ...state, view: 'browse', reelOpen: false };

    case 'step': {
      const recipe = shelfOf(state.shelfIds)[state.activeIndex];
      if (!recipe) return state;
      return {
        ...state,
        stepIndex: Math.max(0, Math.min(recipe.steps.length - 1, state.stepIndex + action.delta)),
      };
    }

    case 'servings':
      return { ...state, servings: Math.max(1, Math.min(24, action.count)) };

    case 'toggle-reel':
      return { ...state, reelOpen: !state.reelOpen };

    case 'clear-filter': {
      const focused = shelfOf(state.shelfIds)[state.activeIndex];
      const index = focused ? ALL.indexOf(focused.id) : 0;
      return { ...state, shelfIds: ALL, shelfLabel: null, activeIndex: Math.max(0, index) };
    }

    /* Moves arrive as a batch from one reply and are folded in order, so
       "shelf, then focus" lands on the right seat of the new arc rather than
       the old one. */
    case 'moves': {
      let next = state;
      for (const move of action.moves) {
        switch (move.kind) {
          case 'shelf': {
            const ids = move.ids.filter((id) => ALL.includes(id));
            next = {
              ...next,
              shelfIds: ids.length ? ids : ALL,
              shelfLabel: ids.length === ALL.length ? null : move.label,
              activeIndex: 0,
            };
            break;
          }
          case 'focus': {
            const index = next.shelfIds.indexOf(move.id);
            next =
              index >= 0
                ? { ...next, activeIndex: index }
                : { ...next, shelfIds: ALL, shelfLabel: null, activeIndex: Math.max(0, ALL.indexOf(move.id)) };
            break;
          }
          case 'cook': {
            const recipe = RECIPES.find((r) => r.id === move.id);
            const index = next.shelfIds.indexOf(move.id);
            next = {
              ...next,
              view: 'cook',
              activeIndex: index >= 0 ? index : next.activeIndex,
              stepIndex: 0,
              servings: recipe?.servings ?? next.servings,
              reelOpen: false,
            };
            break;
          }
          case 'step': {
            const recipe = shelfOf(next.shelfIds)[next.activeIndex];
            if (recipe) {
              next = {
                ...next,
                stepIndex: Math.max(0, Math.min(recipe.steps.length - 1, next.stepIndex + move.delta)),
              };
            }
            break;
          }
          case 'servings':
            next = { ...next, servings: Math.max(1, Math.min(24, move.count)) };
            break;
          case 'browse':
            next = { ...next, view: 'browse', reelOpen: false };
            break;
        }
      }
      return next;
    }

    default:
      return state;
  }
}

/** Cross-fades the two surfaces where the browser supports it, and is a plain
    state change where it does not.

    `flushSync` is load-bearing, not a precaution: the View Transitions API
    snapshots the DOM when the callback returns, and React's update is normally
    async — so without it the transition captures the old tree, commits nothing,
    and leaves a stale snapshot painted over a surface that never changed. */
function transition(run: () => void) {
  const doc = document as Document & { startViewTransition?: (cb: () => void) => void };

  if (
    typeof doc.startViewTransition !== 'function' ||
    matchMedia('(prefers-reduced-motion: reduce)').matches
  ) {
    run();
    return;
  }

  let applied = false;
  const apply = () => {
    if (applied) return;
    applied = true;
    /* `flushSync` is load-bearing inside the callback: the View Transitions API
       snapshots the DOM the moment the callback returns, and React's update is
       normally async, so without it the transition captures a tree that never
       changed. */
    flushSync(run);
  };

  /* The transition decorates the change; it must never own it. Starting one
     captures the whole document, and a full-viewport WebGL canvas can leave
     that capture pending indefinitely — software rasterisers do it every time.
     A gated update means a primary button that visibly does nothing, so the
     state change is on a short fuse and the animation only gets to run if the
     capture beats it there. */
  const fuse = window.setTimeout(apply, 100);

  try {
    doc.startViewTransition(() => {
      window.clearTimeout(fuse);
      apply();
    });
  } catch {
    window.clearTimeout(fuse);
    apply();
  }
}

export default function App() {
  const [state, dispatch] = useReducer(reduce, initial);
  const shelf = useMemo(() => shelfOf(state.shelfIds), [state.shelfIds]);
  const focused = shelf[state.activeIndex] ?? null;
  const cooking = state.view === 'cook' && Boolean(focused);

  const context: CompanionContext = useMemo(
    () => ({
      catalogue: RECIPES,
      shelfIds: state.shelfIds,
      focused,
      cooking,
      stepIndex: state.stepIndex,
      servings: state.servings,
    }),
    [state.shelfIds, focused, cooking, state.stepIndex, state.servings],
  );

  // The engine always reads live state, never a closed-over snapshot.
  const contextRef = useRef(context);
  contextRef.current = context;

  const onMoves = useCallback((moves: Move[]) => {
    if (moves.length === 0) return;
    const changesView = moves.some((m) => m.kind === 'cook' || m.kind === 'browse');
    if (changesView) transition(() => dispatch({ type: 'moves', moves }));
    else dispatch({ type: 'moves', moves });
  }, []);

  // Arrows drive whichever surface is in front.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement | null;
      if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA')) return;

      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        dispatch(cooking ? { type: 'step', delta: -1 } : { type: 'select', index: state.activeIndex - 1 });
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        dispatch(cooking ? { type: 'step', delta: 1 } : { type: 'select', index: state.activeIndex + 1 });
      } else if (e.key === 'Enter' && !cooking && focused) {
        transition(() => dispatch({ type: 'cook' }));
      } else if (e.key === 'Escape' && cooking) {
        transition(() => dispatch({ type: 'browse' }));
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [cooking, state.activeIndex, focused]);

  return (
    <div className={`app app--${state.view}`}>
      <Scene
        recipes={shelf}
        activeIndex={state.activeIndex}
        cooking={cooking}
        onPick={(index) => dispatch({ type: 'select', index })}
        onScrub={(index) => dispatch({ type: 'select', index })}
      />

      <header className="brand">
        <span className="brand__mark">Mise</span>
        <span className="brand__sub">{cooking ? 'at the stove' : 'tonight'}</span>
      </header>

      <main className="stage">
        {cooking && focused ? (
          <CookMode
            recipe={focused}
            stepIndex={state.stepIndex}
            servings={state.servings}
            reelOpen={state.reelOpen}
            onStep={(delta) => dispatch({ type: 'step', delta })}
            onServings={(count) => dispatch({ type: 'servings', count })}
            onToggleReel={() => dispatch({ type: 'toggle-reel' })}
            onExit={() => transition(() => dispatch({ type: 'browse' }))}
          />
        ) : (
          <Shelf
            recipes={shelf}
            activeIndex={state.activeIndex}
            shelfLabel={state.shelfLabel}
            onSelect={(index) => dispatch({ type: 'select', index })}
            onCook={() => transition(() => dispatch({ type: 'cook' }))}
            onWatch={() => transition(() => dispatch({ type: 'watch' }))}
            onClearFilter={() => dispatch({ type: 'clear-filter' })}
          />
        )}
      </main>

      <ChatPanel engine={localEngine} context={context} contextRef={contextRef} onMoves={onMoves} />
    </div>
  );
}
