import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TopBar from './components/TopBar.js';
import Register from './components/Register';
import Login from './components/Login';
import ProductList from './components/ProductList';
import ProductDetails from './components/ProductDetails';
import Cart from './components/Cart';
import Navbar from './components/Navbar.js';
import UserProfile from './components/UserProfile';
import HomePage from './components/HomePage.js';
import Checkout from './components/Checkout.js';
import AuthProvider from './components/AuthProvider';  
import './App.css';

const App = () => {
  const [cart, setCart] = useState([]);
  const [user, setUser] = useState(null);

  const saveCartToLocalStorage = (cart) => {
    localStorage.setItem('cart', JSON.stringify(cart));
  };

  const handleAddToCart = (product) => {
    const existingProduct = cart.find(item => item.id === product.product_id);
    if (existingProduct) {
      setCart(cart.map(item =>
        item.id === product.product_id
          ? { ...item, quantity: item.quantity + 1 }
          : item
      ));
    } else {
      setCart([...cart, { ...product, quantity: 1 }]);
    }
    saveCartToLocalStorage(cart);
  };

  const handleRemoveFromCart = (id) => {
    setCart(cart.filter(item => item.id !== id));
    saveCartToLocalStorage(cart);
  };

  const handleLogin = (user) => {
    setUser(user);
    console.log('User logged in:', user);
  };

  const handleLogout = () => {
    setUser(null);
    console.log('User logged out');
  };

  return (
    <AuthProvider>
      <Router>
        <Navbar
          cartCount={cart.reduce((count, item) => count + item.quantity, 0)}
          user={user}
          onLogout={handleLogout}
        />
        <div className="container">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/register" element={<Register />} />
            <Route path="/login" element={<Login onLogin={handleLogin} />} />
            <Route path="/products" element={<ProductList onAddToCart={handleAddToCart} />} />
            <Route
              path="/products/:id"
              element={<ProductDetails cartItems={cart} onAddToCart={handleAddToCart} />}
            />
            <Route path="/cart" element={<Cart cartItems={cart} onRemoveFromCart={handleRemoveFromCart} />} />
            {/* Przekazujemy user do UserProfile (opcjonalnie) */}
            <Route path="/profile" element={<UserProfile user={user} />} />
            <Route path="/checkout" element={<Checkout cartItems={cart} user={user} />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
};

export default App;
