import React, { useState } from 'react';

const Checkout = ({ cartItems, user }) => {
  const [address, setAddress] = useState('');
  const [orderMessage, setOrderMessage] = useState('');
  const [error, setError] = useState('');

  const handleAddressChange = (e) => {
    setAddress(e.target.value);
  };

  const handleSubmitOrder = async () => {
    if (!user || !user.token) {
      setError('You must be logged in to place an order.');
      return;
    }

    if (!address) {
      setError('Please provide a delivery address.');
      return;
    }

    const orderPayload = {
      user_id: user.id,
      products: cartItems.reduce((acc, item) => {
        acc[item.id] = item.quantity;
        return acc;
      }, {}),
      address,
    };

    try {
      const response = await fetch('/api/order', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${user.token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(orderPayload),
      });

      if (!response.ok) {
        throw new Error('Failed to place order');
      }

      const data = await response.json();
      setOrderMessage(data.message || 'Order placed successfully!');
      setError('');
    } catch (err) {
      console.error('Error placing order:', err);
      setError('Failed to place order. Please try again.');
      setOrderMessage('');
    }
  };

  return (
    <div className="checkout-container">
      <h2>Checkout</h2>
      {cartItems.length === 0 ? (
        <p>Twój koszyk jest pusty.</p>
      ) : (
        <>
          <h3>Podsumowanie zamówienia</h3>
          <ul>
            {cartItems.map((item) => (
              <li key={item.id}>
                {item.name} - Ilość: {item.quantity} - Razem: ${item.price * item.quantity}
              </li>
            ))}
          </ul>
          <h3>Adres</h3>
          <input
            type="text"
            value={address}
            onChange={handleAddressChange}
            placeholder="Enter your address"
            className="form-input"
          />
          <button onClick={handleSubmitOrder} className="form-button">Złóż zamówienie</button>
          {orderMessage && <p className="success-message">{orderMessage}</p>}
          {error && <p className="error-message">{error}</p>}
        </>
      )}
    </div>
  );
};

export default Checkout;
