/* Browse: the billboard for whatever the arc is holding at centre, plus the rail
   that lets you pick without dragging. */

import type { Recipe } from '../data/recipes';
import { Icon } from './Icon';
import { useEntrance } from './useEntrance';

export interface ShelfProps {
  recipes: Recipe[];
  activeIndex: number;
  shelfLabel: string | null;
  onSelect: (index: number) => void;
  onCook: () => void;
  onWatch: () => void;
  onClearFilter: () => void;
}

const EFFORT_COPY: Record<Recipe['effort'], string> = {
  easy: 'Easy',
  steady: 'Steady',
  involved: 'Involved',
};

function DishName({ recipe }: { recipe: Recipe }) {
  const entering = useEntrance(recipe.id);
  return (
    <h1 className="billboard__name" data-entering={entering ? '' : undefined}>
      {recipe.name}
    </h1>
  );
}

export function Shelf({
  recipes,
  activeIndex,
  shelfLabel,
  onSelect,
  onCook,
  onWatch,
  onClearFilter,
}: ShelfProps) {
  const recipe = recipes[activeIndex];

  if (!recipe) {
    /* Empty shelf teaches the way back rather than saying "no results". */
    return (
      <div className="billboard billboard--empty glass">
        <h2>Nothing left on the shelf</h2>
        <p className="measure">
          That filter has no dishes behind it. Loosen the time or the diet, or put everything back.
        </p>
        <button type="button" className="btn btn--primary" onClick={onClearFilter}>
          Show everything
        </button>
      </div>
    );
  }

  return (
    <>
      <section className="billboard" aria-live="polite">
        {shelfLabel && (
          <button type="button" className="chip billboard__filter" aria-pressed="true" onClick={onClearFilter}>
            {shelfLabel}
            <Icon name="close" size={14} />
          </button>
        )}

        <DishName recipe={recipe} key={recipe.id} />

        <p className="billboard__line measure">{recipe.line}</p>

        <dl className="billboard__meta tnum">
          <div>
            <dt>
              <Icon name="clock" size={16} />
              <span className="visually-hidden">Time</span>
            </dt>
            <dd>{recipe.minutes} min</dd>
          </div>
          <div>
            <dt>
              <Icon name="people" size={16} />
              <span className="visually-hidden">Serves</span>
            </dt>
            <dd>{recipe.servings}</dd>
          </div>
          <div>
            <dt>
              <Icon name="list" size={16} />
              <span className="visually-hidden">Effort</span>
            </dt>
            <dd>{EFFORT_COPY[recipe.effort]}</dd>
          </div>
        </dl>

        <div className="billboard__actions">
          <button type="button" className="btn btn--primary" onClick={onCook}>
            Cook this
          </button>
          <button type="button" className="btn" onClick={onWatch}>
            <Icon name="play" size={16} />
            Watch the method
          </button>
        </div>
      </section>

      <nav className="rail glass glass--thin" aria-label="Shelf">
        <button
          type="button"
          className="btn btn--quiet rail__step"
          onClick={() => onSelect(activeIndex - 1)}
          disabled={activeIndex === 0}
        >
          <Icon name="left" size={18} />
          <span className="visually-hidden">Previous dish</span>
        </button>

        <ul className="rail__list" role="list">
          {recipes.map((r, i) => (
            <li key={r.id}>
              <button
                type="button"
                className="rail__item"
                aria-current={i === activeIndex ? 'true' : undefined}
                onClick={() => onSelect(i)}
              >
                <span className="rail__item-name">{r.name.split(',')[0]}</span>
                <span className="rail__item-time tnum">{r.minutes}</span>
              </button>
            </li>
          ))}
        </ul>

        <button
          type="button"
          className="btn btn--quiet rail__step"
          onClick={() => onSelect(activeIndex + 1)}
          disabled={activeIndex >= recipes.length - 1}
        >
          <Icon name="right" size={18} />
          <span className="visually-hidden">Next dish</span>
        </button>
      </nav>
    </>
  );
}
