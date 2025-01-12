import { render, screen, fireEvent } from '@testing-library/react';
import Cart from './Cart';

describe('Cart Component', () => {
  const mockCartItems = [
    { id: 1, name: 'Product 1', quantity: 2, price: 10 },
    { id: 2, name: 'Product 2', quantity: 1, price: 20 },
  ];

  it('should display cart items and total', () => {
    render(<Cart cartItems={mockCartItems} onRemoveFromCart={jest.fn()} />);

    expect(screen.getByText(/Product 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Total: \$40.00/i)).toBeInTheDocument();
  });

  it('should call onRemoveFromCart when removing an item', () => {
    const mockRemoveFromCart = jest.fn();
    render(<Cart cartItems={mockCartItems} onRemoveFromCart={mockRemoveFromCart} />);

    fireEvent.click(screen.getAllByText(/Remove/i)[0]);
    expect(mockRemoveFromCart).toHaveBeenCalledWith(1);
  });
});
