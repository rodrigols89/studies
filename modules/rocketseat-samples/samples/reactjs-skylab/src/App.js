import React from 'react';
import Routes from './routes';

import Header from './components/Header/Header';

import "./main.css";

const App = () => (
  <div className="App">
    <Header />
    <Routes />
  </div>
);

export default App;
