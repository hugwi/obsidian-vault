/* One icon set, authored here: 24×24, 1.5 stroke, round caps and joins.
   No glyph or emoji stands in for an icon anywhere in this app. */

import type { ReactElement, SVGProps } from 'react';

type IconName = 'clock' | 'people' | 'left' | 'right' | 'send' | 'play' | 'close' | 'check' | 'list';

const PATHS: Record<IconName, ReactElement> = {
  clock: (
    <>
      <circle cx="12" cy="12" r="8.25" />
      <path d="M12 7.75V12l2.75 1.75" />
    </>
  ),
  people: (
    <>
      <path d="M15.5 19.25v-1.5a3.25 3.25 0 0 0-3.25-3.25h-3.5A3.25 3.25 0 0 0 5.5 17.75v1.5" />
      <circle cx="10.5" cy="8.5" r="3.25" />
      <path d="M18.5 19.25v-1.5a3.25 3.25 0 0 0-2.5-3.16M15.5 5.44a3.25 3.25 0 0 1 0 6.12" />
    </>
  ),
  left: <path d="M14.5 5.75 8.25 12l6.25 6.25" />,
  right: <path d="M9.5 5.75 15.75 12 9.5 18.25" />,
  send: <path d="M4.75 12 19.25 5.25 15.5 19.25l-4-5.5-6.75-1.75Z" />,
  play: <path d="M8.75 5.75 18.25 12l-9.5 6.25V5.75Z" />,
  close: <path d="M6.75 6.75l10.5 10.5M17.25 6.75l-10.5 10.5" />,
  check: <path d="M5.75 12.5 10 16.75l8.25-9.5" />,
  list: (
    <>
      <path d="M9.25 7.25h9M9.25 12h9M9.25 16.75h9" />
      <path d="M5.75 7.25h.01M5.75 12h.01M5.75 16.75h.01" />
    </>
  ),
};

export function Icon({
  name,
  size = 20,
  ...rest
}: { name: IconName; size?: number } & SVGProps<SVGSVGElement>) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
      {...rest}
    >
      {PATHS[name]}
    </svg>
  );
}

/** The heat scale, shared with the reel. */
export function HeatBars({ level }: { level: 0 | 1 | 2 | 3 }) {
  return (
    <svg width="26" height="14" viewBox="0 0 34 18" fill="none" aria-hidden="true">
      {[0, 1, 2].map((i) => (
        <rect
          key={i}
          x={1 + i * 12}
          y={17 - (i + 1) * 4.6}
          width="8"
          height={(i + 1) * 4.6}
          rx="2"
          fill={i < level ? 'currentColor' : 'rgb(255 246 236 / 0.16)'}
        />
      ))}
    </svg>
  );
}
