/* Cook mode — an Operate surface.

   The dish is still turning behind the glass, but from here on the interface
   gets out of the way: one step large enough to read from across a counter,
   the quantities already scaled, and the reel one tap away when you want the
   whole method at a glance. */

import { lazy, Suspense, useMemo } from 'react';
import type { Recipe } from '../data/recipes';
import { reelDuration, FPS } from '../remotion/StepReel';
import { HeatBars, Icon } from './Icon';
import { useEntrance } from './useEntrance';

/* The player pulls in the whole Remotion runtime; it stays out of the first
   paint until someone actually asks for the reel. */
const ReelPlayer = lazy(() => import('./ReelPlayer'));

const HEAT_LEVEL: Record<NonNullable<Recipe['steps'][number]['heat']>, 0 | 1 | 2 | 3> = {
  none: 0,
  low: 1,
  medium: 2,
  high: 3,
};

/** Scale to the requested servings, then round to something a cook can measure. */
function scaleQty(qty: number | null, from: number, to: number): string {
  if (qty === null) return '';
  const value = (qty * to) / from;
  if (value >= 100) return String(Math.round(value / 5) * 5);
  if (value >= 10) return String(Math.round(value));
  if (value >= 1) return String(Math.round(value * 2) / 2);
  return String(Math.round(value * 4) / 4);
}

export interface CookModeProps {
  recipe: Recipe;
  stepIndex: number;
  servings: number;
  reelOpen: boolean;
  onStep: (delta: number) => void;
  onServings: (count: number) => void;
  onToggleReel: () => void;
  onExit: () => void;
}

export function CookMode({
  recipe,
  stepIndex,
  servings,
  reelOpen,
  onStep,
  onServings,
  onToggleReel,
  onExit,
}: CookModeProps) {
  const step = recipe.steps[stepIndex];
  const entering = useEntrance(stepIndex, 600);
  const last = stepIndex === recipe.steps.length - 1;
  const duration = useMemo(() => reelDuration(recipe), [recipe]);
  const elapsed = recipe.steps.slice(0, stepIndex).reduce((sum, s) => sum + (s.minutes ?? 0), 0);
  const total = recipe.steps.reduce((sum, s) => sum + (s.minutes ?? 0), 0);

  return (
    <div className="cook">
      <section className="cook__method glass glass--thick glass--dense glass--live" aria-label="Method">
        <header className="cook__head">
          <button type="button" className="btn btn--quiet" onClick={onExit}>
            <Icon name="left" size={18} />
            Shelf
          </button>
          <h2 className="cook__dish">{recipe.name}</h2>
        </header>

        {/* Progress is the honest kind: minutes behind you out of minutes total. */}
        <div className="cook__progress" role="group" aria-label="Progress">
          <div className="cook__bar">
            <span style={{ transform: `scaleX(${total ? elapsed / total : 0})` }} />
          </div>
          <p className="cook__progress-copy tnum">
            Step {stepIndex + 1} of {recipe.steps.length} · about {total - elapsed} min left
          </p>
        </div>

        <article className="cook__step" data-entering={entering ? '' : undefined} key={stepIndex}>
          <div className="cook__step-meta tnum">
            <span className="cook__step-n">{String(stepIndex + 1).padStart(2, '0')}</span>
            {step.minutes !== undefined && (
              <span className="cook__step-time">
                <Icon name="clock" size={15} />
                {step.minutes} min
              </span>
            )}
            {step.heat && step.heat !== 'none' && (
              <span className="cook__step-heat" title={`${step.heat} heat`}>
                <HeatBars level={HEAT_LEVEL[step.heat]} />
                <span className="visually-hidden">{step.heat} heat</span>
              </span>
            )}
          </div>

          <h3 className="cook__step-title">{step.title}</h3>
          <p className="cook__step-body measure">{step.body}</p>
        </article>

        <div className="cook__nav">
          <button
            type="button"
            className="btn"
            onClick={() => onStep(-1)}
            disabled={stepIndex === 0}
          >
            <Icon name="left" size={16} />
            Back
          </button>
          <button
            type="button"
            className="btn btn--primary"
            onClick={() => (last ? onExit() : onStep(1))}
          >
            {last ? (
              <>
                <Icon name="check" size={16} />
                Done
              </>
            ) : (
              <>
                Next step
                <Icon name="right" size={16} />
              </>
            )}
          </button>
          <button type="button" className="btn btn--quiet" onClick={onToggleReel}>
            <Icon name={reelOpen ? 'close' : 'play'} size={16} />
            {reelOpen ? 'Close reel' : 'Reel'}
          </button>
        </div>

        {last && <p className="cook__pairing">{recipe.pairing}</p>}
      </section>

      <section className="cook__mise glass glass--dense" aria-label="Ingredients">
        <div className="cook__servings">
          <h3>Mise en place</h3>
          <div className="cook__stepper" role="group" aria-label="Servings">
            <button
              type="button"
              className="btn btn--quiet"
              onClick={() => onServings(Math.max(1, servings - 1))}
              disabled={servings <= 1}
            >
              <Icon name="left" size={16} />
              <span className="visually-hidden">Fewer servings</span>
            </button>
            <span className="cook__servings-count tnum">
              <Icon name="people" size={16} />
              {servings}
            </span>
            <button
              type="button"
              className="btn btn--quiet"
              onClick={() => onServings(Math.min(24, servings + 1))}
              disabled={servings >= 24}
            >
              <Icon name="right" size={16} />
              <span className="visually-hidden">More servings</span>
            </button>
          </div>
        </div>

        <ul className="cook__ingredients" role="list">
          {recipe.ingredients.map((ing) => (
            <li key={ing.item}>
              <span className="cook__qty tnum">
                {scaleQty(ing.qty, recipe.servings, servings)} {ing.unit}
              </span>
              <span className="cook__item">
                {ing.item}
                {ing.note && <span className="cook__note">{ing.note}</span>}
              </span>
            </li>
          ))}
        </ul>
      </section>

      {reelOpen && (
        <section className="reel glass glass--thick" aria-label="Method reel">
          <Suspense
            fallback={<div className="skeleton reel__skeleton" aria-label="Loading the reel" />}
          >
            <ReelPlayer recipeId={recipe.id} durationInFrames={duration} fps={FPS} />
          </Suspense>
        </section>
      )}
    </div>
  );
}
