import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
const HomePage = () => {
    const [currentImageIndex, setCurrentImageIndex] = useState(0);
    const images = [
      { src: 'https://t3.ftcdn.net/jpg/03/15/33/46/360_F_315334622_sU5qBAIVbeLTeaZt2t6TBGhS4De4ShXA.jpg', alt: 'Dog' },
      { src: 'https://via.placeholder.com/800x400?text=Cat+Toys', alt: 'Cat Toys' },
      { src: 'https://via.placeholder.com/800x400?text=Fish+Tanks', alt: 'Fish Tanks' }
    ];
  

  
    return (
      <div className="home-page">
        <div className="carousel">
          <img
            src={images[currentImageIndex].src}
            alt={images[currentImageIndex].alt}
            className="carousel-image"
          />
        </div>
        <h2 className="home-header">Welcome to Our Pet Store!</h2>
        <p className="home-text">Find the best products for your pets. High-quality food, fun toys, and more!</p>
        <div className="home-links">
          <Link to="/products" className="home-link">Shop Now</Link>
        </div>
      </div>
    );
  };
  export default HomePage;