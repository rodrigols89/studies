import React from 'react';

import { BrowserRouter, Switch, Route } from 'react-router-dom';

import HomeContent from './pages/home-content/HomeContent';
import Product from './pages/product/Product';

const Routes = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={HomeContent} />
      <Route path="/products/:id" component={Product} />
    </Switch>
  </BrowserRouter>
)

export default Routes;
