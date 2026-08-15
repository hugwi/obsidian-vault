import { Composition } from 'remotion';
import { RECIPES } from '../data/recipes';
import { FPS, StepReel, reelDuration } from './StepReel';

/* Registered for the CLI (`npm run reel`, `npm run reel:studio`). The app itself
   mounts <StepReel /> through <Player>, so the timeline in the panel and the
   timeline in the exported MP4 are the same code. */
export function RemotionRoot() {
  return (
    <Composition
      id="StepReel"
      component={StepReel}
      fps={FPS}
      width={1600}
      height={900}
      defaultProps={{ recipeId: RECIPES[0].id }}
      calculateMetadata={({ props }) => {
        const recipe = RECIPES.find((r) => r.id === props.recipeId) ?? RECIPES[0];
        return { durationInFrames: reelDuration(recipe) };
      }}
    />
  );
}
