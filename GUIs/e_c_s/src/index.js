<<<<<<< HEAD
// src/index.js
import React from 'react';
import { createRoot } from 'react-dom/client';
import Chatbox from './components/Chatbox/Chatbox';
import './style.css';

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<Chatbox />);
} else {
  console.error('Target container is not a DOM element.');
}
=======
// src/index.js
import React from 'react';
import { createRoot } from 'react-dom/client';
import Chatbox from './components/Chatbox/Chatbox';
import './style.css';

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<Chatbox />);
} else {
  console.error('Target container is not a DOM element.');
}
>>>>>>> origin/main
