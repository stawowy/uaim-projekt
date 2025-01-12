import './ProductList.css';

import React, { useState, useEffect } from 'react';
const ProductList = ({ onAddToCart }) => {
  const [products, setProducts, ] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/products');
        const data = await response.json();
        setProducts(data);
        console.log('Fetched products:', data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };
    fetchProducts();
  }, []);

  const handleAddToCart = (product) => {
    console.log('Adding product to cart:', product);
    onAddToCart(product);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredProducts = products.filter(product =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="product-list">
  
      <h2 className="product-list-header">Lista produktów <input
        type="text"
        placeholder="Search products..."
        value={searchTerm}
        onChange={handleSearchChange}
        className="search-input"
      /></h2>
      
      <div className="product-grid">
        {filteredProducts.map(product => (
          <div key={product.product_id} className="product-card">
            <img src={'http://localhost:5000/api/photos/' + product.image_path} alt={product.name} className="product-image" />
            <h className="product-name">{product.name}</h>
            <p className="product-price">{product.price}$</p>
            <button onClick={() => handleAddToCart(product)} className="add-to-cart-button">Dodaj do koszyka</button>
            <a href={`/products/${product.product_id}`} className="product-details-link">Pokaż szczegóły</a>
          </div>
        ))}
      </div>
    </div>
  );
};
  export default ProductList;