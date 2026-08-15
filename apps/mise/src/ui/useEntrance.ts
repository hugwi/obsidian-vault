import { useEffect, useState } from 'react';

/* Marks an element as "entering" for a fixed wall-clock window.

   Entrance animations are attached through this rather than run unconditionally,
   because a compositor animation on a page carrying a full-viewport WebGL canvas
   can sit at time zero indefinitely — and a keyframe that starts clipped or
   offset would then hold that state forever. The timer always fires, so the
   element reverts to its ordinary style whether or not the animation ever ran. */
export function useEntrance(key: unknown, ms = 900): boolean {
  const [entering, setEntering] = useState(true);

  useEffect(() => {
    setEntering(true);
    const id = window.setTimeout(() => setEntering(false), ms);
    return () => window.clearTimeout(id);
  }, [key, ms]);

  return entering;
}
