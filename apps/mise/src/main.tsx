import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

/* Both faces are self-hosted through fontsource — nothing is fetched from a
   font CDN at runtime. Fraunces carries the display voice (its SOFT and WONK
   axes are what keep it from reading as a default serif); Geist carries every
   control, label and number. */
import '@fontsource-variable/fraunces/full.css';
import '@fontsource-variable/geist';

import './styles/tokens.css';
import './styles/base.css';
import './styles/glass.css';
import './styles/app.css';

import App from './App';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
