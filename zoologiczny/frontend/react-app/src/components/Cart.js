// Komponent koszyka
import { useNavigate } from 'react-router-dom';

const Cart = ({ cartItems, onRemoveFromCart }) => {
  const navigate = useNavigate();
  const handleCheckout = () => {
    navigate('/checkout');
  };
  

  console.log('Rendering cart with items:', cartItems);

  return (
    <div className="cart-container">
      <h2 className="cart-header">Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
       <ul className="cart-list">
          {cartItems.map(item => (
            <li key={item.product_id} className="cart-item">
              {item.name} - Quantity: {item.quantity} - Price: {item.price} - Total: ${(item.price * item.quantity).toFixed(2)}
              <button onClick={() => onRemoveFromCart(item.id)} className="remove-button">Remove</button>
            </li>
          ))}
        </ul>
          <button onClick={handleCheckout} className="checkout-button">Checkout</button>
        </>
      )}
    </div>
  );
};

export default Cart;