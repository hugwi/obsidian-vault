/* The method, as a reel.

   Cook mode is where you read a step. The reel is where you watch the whole
   method at a glance before you start — which pan, which order, where the long
   waits are. It is a Remotion composition, so the same timeline that plays
   inside the glass panel renders to an MP4 with `npm run reel`. */

import { AbsoluteFill, Sequence, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { RECIPES, type Recipe, type Step } from '../data/recipes';

export const FPS = 30;
const INTRO = 66;
const PER_STEP = 96;
const OUTRO = 78;

export const reelDuration = (recipe: Recipe): number =>
  INTRO + recipe.steps.length * PER_STEP + OUTRO;

/* A type alias rather than an interface on purpose: Remotion constrains
   composition props to `Record<string, unknown>`, and only type aliases carry
   the implicit index signature that satisfies it. */
export type StepReelProps = {
  recipeId: string;
};

const EASE_OUT = (t: number) => 1 - Math.pow(1 - t, 3);

/** Three bars, drawn — the heat scale, not an emoji flame. */
function HeatMark({ heat }: { heat: Step['heat'] }) {
  const level = heat === 'high' ? 3 : heat === 'medium' ? 2 : heat === 'low' ? 1 : 0;
  if (level === 0) return null;
  return (
    <svg width="34" height="18" viewBox="0 0 34 18" fill="none" aria-hidden="true">
      {[0, 1, 2].map((i) => (
        <rect
          key={i}
          x={1 + i * 12}
          y={17 - (i + 1) * 4.6}
          width="8"
          height={(i + 1) * 4.6}
          rx="2"
          fill={i < level ? '#ff8b3d' : '#3a332c'}
        />
      ))}
    </svg>
  );
}

/** The ring drains across the step's own duration, so a 20-minute reduction
    visibly takes longer on screen than a 40-second bloom. */
function TimingRing({ progress, minutes }: { progress: number; minutes?: number }) {
  const r = 46;
  const circumference = 2 * Math.PI * r;
  return (
    <div style={{ position: 'relative', width: 108, height: 108 }}>
      <svg width="108" height="108" viewBox="0 0 108 108" aria-hidden="true">
        <circle cx="54" cy="54" r={r} fill="none" stroke="#2a2521" strokeWidth="3" />
        <circle
          cx="54"
          cy="54"
          r={r}
          fill="none"
          stroke="#ff8b3d"
          strokeWidth="3"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={circumference * (1 - progress)}
          transform="rotate(-90 54 54)"
        />
      </svg>
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'grid',
          placeItems: 'center',
          fontFamily: "'Geist Variable', sans-serif",
          fontVariantNumeric: 'tabular-nums lining-nums',
          color: '#f7f2ec',
        }}
      >
        <div style={{ textAlign: 'center', lineHeight: 1.1 }}>
          <div style={{ fontSize: 30, fontWeight: 600 }}>{minutes ?? '—'}</div>
          <div style={{ fontSize: 11, color: '#8d8177', letterSpacing: '0.08em' }}>MIN</div>
        </div>
      </div>
    </div>
  );
}

function StepCard({ step, index, total }: { step: Step; index: number; total: number }) {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const enter = spring({ frame, fps, config: { damping: 200, mass: 0.6 }, durationInFrames: 26 });
  const exit = interpolate(frame, [PER_STEP - 16, PER_STEP], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const ring = EASE_OUT(
    interpolate(frame, [14, PER_STEP - 12], [0, 1], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    }),
  );

  // The title is uncovered rather than faded — a wipe reads as "next" the way a
  // fade never does.
  const wipe = interpolate(enter, [0, 1], [100, 0]);

  return (
    <AbsoluteFill
      style={{
        padding: '64px 76px',
        opacity: 1 - exit,
        transform: `translateY(${(1 - enter) * 26 - exit * 18}px)`,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: 44 }}>
        <TimingRing progress={ring} minutes={step.minutes} />
        <div style={{ flex: 1, minWidth: 0 }}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 14,
              fontFamily: "'Geist Variable', sans-serif",
              fontSize: 14,
              letterSpacing: '0.1em',
              color: '#8d8177',
              fontVariantNumeric: 'tabular-nums',
              marginBottom: 14,
            }}
          >
            <span>
              {String(index + 1).padStart(2, '0')} / {String(total).padStart(2, '0')}
            </span>
            <HeatMark heat={step.heat} />
          </div>

          <h2
            style={{
              margin: 0,
              fontFamily: "'Fraunces Variable', Georgia, serif",
              fontSize: 58,
              lineHeight: 1.02,
              letterSpacing: '-0.034em',
              color: '#f7f2ec',
              fontVariationSettings: "'SOFT' 12, 'WONK' 1, 'opsz' 120",
              clipPath: `inset(0 ${wipe}% 0 0)`,
            }}
          >
            {step.title}
          </h2>

          <p
            style={{
              margin: '22px 0 0',
              maxWidth: '46ch',
              fontFamily: "'Geist Variable', sans-serif",
              fontSize: 22,
              lineHeight: 1.5,
              color: '#c3b5a8',
              opacity: interpolate(frame, [12, 30], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              }),
            }}
          >
            {step.body}
          </p>
        </div>
      </div>
    </AbsoluteFill>
  );
}

export function StepReel({ recipeId }: StepReelProps) {
  const recipe = RECIPES.find((r) => r.id === recipeId) ?? RECIPES[0];
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const introIn = spring({ frame, fps, config: { damping: 200 }, durationInFrames: 30 });
  const introOut = interpolate(frame, [INTRO - 18, INTRO], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const outroStart = durationInFrames - OUTRO;
  const outroIn = interpolate(frame, [outroStart, outroStart + 24], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ background: '#0a0907' }}>
      {/* the same warmth the app sits in, so the reel does not look pasted in */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(70% 60% at 16% 10%, rgba(255,139,61,0.20), transparent 62%), radial-gradient(60% 55% at 88% 90%, rgba(181,138,192,0.12), transparent 60%)',
        }}
      />

      <Sequence durationInFrames={INTRO}>
        <AbsoluteFill
          style={{
            padding: '0 76px',
            justifyContent: 'center',
            opacity: 1 - introOut,
            transform: `translateY(${(1 - introIn) * 18 - introOut * 22}px)`,
          }}
        >
          <h1
            style={{
              margin: 0,
              fontFamily: "'Fraunces Variable', Georgia, serif",
              fontSize: 78,
              lineHeight: 0.98,
              letterSpacing: '-0.038em',
              color: '#f7f2ec',
              fontVariationSettings: "'SOFT' 12, 'WONK' 1, 'opsz' 144",
              maxWidth: '16ch',
            }}
          >
            {recipe.name}
          </h1>
          <div
            style={{
              marginTop: 26,
              display: 'flex',
              gap: 28,
              fontFamily: "'Geist Variable', sans-serif",
              fontSize: 19,
              color: '#c3b5a8',
              fontVariantNumeric: 'tabular-nums',
            }}
          >
            <span>{recipe.minutes} minutes</span>
            <span>{recipe.steps.length} steps</span>
            <span>serves {recipe.servings}</span>
          </div>
        </AbsoluteFill>
      </Sequence>

      {recipe.steps.map((step, i) => (
        <Sequence key={i} from={INTRO + i * PER_STEP} durationInFrames={PER_STEP}>
          <StepCard step={step} index={i} total={recipe.steps.length} />
        </Sequence>
      ))}

      <Sequence from={outroStart}>
        <AbsoluteFill
          style={{
            padding: '0 76px',
            justifyContent: 'center',
            opacity: outroIn,
            transform: `translateY(${(1 - outroIn) * 16}px)`,
          }}
        >
          <p
            style={{
              margin: 0,
              maxWidth: '24ch',
              fontFamily: "'Fraunces Variable', Georgia, serif",
              fontSize: 44,
              lineHeight: 1.14,
              letterSpacing: '-0.03em',
              color: '#f7f2ec',
              fontVariationSettings: "'SOFT' 12, 'WONK' 1",
            }}
          >
            {recipe.pairing}
          </p>
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
}
