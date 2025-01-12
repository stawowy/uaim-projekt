
import './ProductDetails.css';
// components/ProductDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';


const ProductDetails = ({ onAddToCart } ) => {
  const { id } = useParams(); // Get the product ID from the route parameters
  const [product, setProduct] = useState(null);
  const [error, setError] = useState(null);
  const [cart, setCart] = useState(() => {
    const savedCart = localStorage.getItem('cart');
    return savedCart ? JSON.parse(savedCart) : [];
  });

  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        const response = await fetch(`http://localhost:5000/api/products/${id}`);
        if (!response.ok) {
          throw new Error('Failed to fetch product details');
        }
        const data = await response.json();
        setProduct(data);
        console.log('Fetched product details:', data);
      } catch (err) {
        console.error('Error fetching product details:', err);
        setError('Could not load product details. Please try again later.');
      }
    };

    fetchProductDetails();
  }, [id]);


  const handleAddToCart = () => {
    if (product) {
      console.log('Adding product to cart from ProductDetails:', product);
      onAddToCart(product);
    }
  };

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  if (!product) {
    return <div className="loading-message">Loading product details...</div>;
  }

  return (
    <div className="product-details-container">
      <img src={'http://localhost:5000/api/photos/' + product.image_path} alt={product.name} className="product-details-image" />
      <h2 className="product-details-header">{product.name}</h2>
      <p className="product-description">{product.description}</p>
      <p className="product-price">Cena: ${product.price}</p>
      <p className="product-stock">Na stanie: {product.stock_quantity}</p>
      <p className="product-category">Kategoria: {product.category} / {product.subcategory}</p>
      <p className="product-rating">Ocena: {product.rating}</p>
      <button onClick={handleAddToCart} className="add-to-cart-button">Dodaj do koszyka</button>
    </div>
  );
};

export default ProductDetails;
