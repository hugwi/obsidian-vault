/* The companion panel.

   Two rules hold this together. The reply is never just text — every answer
   carries `moves` that re-form the shelf behind the glass, so the conversation
   and the room stay the same thing. And nothing here fakes latency: the local
   engine answers immediately, and the reveal you see is the text arriving, not
   a staged wait. */

import { useEffect, useRef, useState } from 'react';
import type { CompanionContext, CompanionEngine, CompanionReply, Move } from '../companion/engine';
import { Icon } from './Icon';

interface Message {
  id: number;
  role: 'you' | 'mise';
  text: string;
  suggestions?: string[];
}

const reduced = () =>
  typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;

/** Reveals the reply a word at a time. Not a typewriter gimmick: it gives the
    carousel behind the glass time to finish re-forming, so you read the answer
    at the pace the room changes. */
function useReveal(text: string, active: boolean): string {
  const [shown, setShown] = useState(active ? '' : text);

  useEffect(() => {
    if (!active || reduced()) {
      setShown(text);
      return;
    }
    const words = text.split(' ');
    const total = Math.min(620, words.length * 26);
    const start = Date.now();

    /* Stepped on a timer rather than requestAnimationFrame. The reply is the
       content, and rAF is frame-gated: on a page carrying a full-viewport WebGL
       canvas those callbacks can be starved indefinitely, which would leave the
       companion's answer permanently blank. A timer still fires when frames do
       not, so the worst case is a reveal that lands in one step. */
    const id = window.setInterval(() => {
      const t = Math.min(1, (Date.now() - start) / total);
      const eased = 1 - Math.pow(1 - t, 2);
      setShown(words.slice(0, Math.max(1, Math.round(eased * words.length))).join(' '));
      if (t >= 1) window.clearInterval(id);
    }, 30);
    return () => window.clearInterval(id);
  }, [text, active]);

  return shown;
}

function Bubble({ message, live }: { message: Message; live: boolean }) {
  const text = useReveal(message.text, live && message.role === 'mise');
  return (
    <div className={`bubble bubble--${message.role}`}>
      {message.role === 'mise' && <span className="bubble__who">Mise</span>}
      <p>{text}</p>
    </div>
  );
}

export interface ChatPanelProps {
  engine: CompanionEngine;
  context: CompanionContext;
  onMoves: (moves: Move[]) => void;
  /** kept in a ref by the parent so the engine always reads current state */
  contextRef: { current: CompanionContext };
}

export function ChatPanel({ engine, context, onMoves, contextRef }: ChatPanelProps) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [draft, setDraft] = useState('');
  const [busy, setBusy] = useState(false);
  const [liveId, setLiveId] = useState(-1);
  const nextId = useRef(0);
  const log = useRef<HTMLDivElement>(null);

  // Opening line, once.
  useEffect(() => {
    const hello: CompanionReply = engine.greeting(contextRef.current);
    setMessages([{ id: nextId.current++, role: 'mise', text: hello.say, suggestions: hello.suggestions }]);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    const el = log.current;
    if (!el) return;
    el.scrollTo({ top: el.scrollHeight, behavior: reduced() ? 'auto' : 'smooth' });
  }, [messages]);

  const send = async (raw: string) => {
    const text = raw.trim();
    if (!text || busy) return;

    setDraft('');
    setBusy(true);
    setMessages((m) => [...m, { id: nextId.current++, role: 'you', text }]);

    const reply = await engine.respond(text, contextRef.current);

    // The room moves first, then the words land on top of it.
    onMoves(reply.moves);

    const id = nextId.current++;
    setLiveId(id);
    setMessages((m) => [...m, { id, role: 'mise', text: reply.say, suggestions: reply.suggestions }]);
    setBusy(false);
  };

  const last = messages[messages.length - 1];
  const suggestions = last?.role === 'mise' ? last.suggestions : undefined;

  return (
    <aside className="companion glass glass--thick glass--dense glass--live" aria-label="Cooking companion">
      <header className="companion__head">
        <h2 className="companion__title">Companion</h2>
        <p className="companion__state tnum">
          {context.cooking && context.focused
            ? `Cooking · step ${context.stepIndex + 1} of ${context.focused.steps.length}`
            : `${context.shelfIds.length} on the shelf`}
        </p>
      </header>

      <div className="companion__log" ref={log} role="log" aria-live="polite" aria-atomic="false">
        {messages.map((m) => (
          <Bubble key={m.id} message={m} live={m.id === liveId} />
        ))}
      </div>

      {suggestions && suggestions.length > 0 && (
        <div className="companion__suggestions">
          {suggestions.map((s) => (
            <button key={s} type="button" className="chip" onClick={() => void send(s)} disabled={busy}>
              {s}
            </button>
          ))}
        </div>
      )}

      <form
        className="companion__compose"
        onSubmit={(e) => {
          e.preventDefault();
          void send(draft);
        }}
      >
        <label className="visually-hidden" htmlFor="companion-input">
          Ask the companion
        </label>
        <input
          id="companion-input"
          className="companion__input"
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          placeholder={context.cooking ? 'next · how long · no feta' : 'vegetarian, twenty minutes…'}
          autoComplete="off"
          enterKeyHint="send"
        />
        <button
          type="submit"
          className="btn btn--primary companion__send"
          disabled={!draft.trim() || busy}
          aria-busy={busy}
        >
          <Icon name="send" size={18} />
          <span className="visually-hidden">Send</span>
        </button>
      </form>
    </aside>
  );
}
