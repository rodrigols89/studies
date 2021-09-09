import React, { Component } from 'react';
import api from '../../services/api';
import { Link } from 'react-router-dom';

import './Product.css';

export default class Product extends Component {
  state = {
    product: {},
  };

  async componentDidMount() {
    const { id } = this.props.match.params;
    const responde = await api.get(`/products/${id}`);
    this.setState({ product: responde.data });
  }

  render() {
    const { product } = this.state;

    return (
      <div className="product-info">
        <h1>{product.title}</h1>
        <p>{product.description}</p>
        <p>
          <a href={product.url}>{product.url}</a>
        </p>
        <Link className="back" to={`/`}>Back</Link>
      </div>
    );
  }
}
