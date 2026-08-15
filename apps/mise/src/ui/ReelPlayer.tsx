import { Player } from '@remotion/player';
import { StepReel } from '../remotion/StepReel';

/* Lazy-loaded so the Remotion runtime never lands in the first paint. */
export default function ReelPlayer({
  recipeId,
  durationInFrames,
  fps,
}: {
  recipeId: string;
  durationInFrames: number;
  fps: number;
}) {
  return (
    <Player
      component={StepReel}
      inputProps={{ recipeId }}
      durationInFrames={durationInFrames}
      fps={fps}
      compositionWidth={1600}
      compositionHeight={900}
      style={{ width: '100%', borderRadius: 'var(--r-md)', overflow: 'hidden' }}
      controls
      autoPlay
      acknowledgeRemotionLicense
    />
  );
}
