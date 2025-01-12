import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ProductList from './ProductList';

describe('ProductList Component', () => {
  it('should render the product list header and search input', () => {
    render(<ProductList onAddToCart={jest.fn()} />);
    expect(screen.getByText(/Lista produktów/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Search products.../i)).toBeInTheDocument();
  });

  it('should fetch and display products', async () => {
    const mockProducts = [
      { product_id: 1, name: 'Product 1', price: 10, image_path: 'image1.jpg' },
      { product_id: 2, name: 'Product 2', price: 20, image_path: 'image2.jpg' },
    ];
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockProducts),
      })
    );

    render(<ProductList onAddToCart={jest.fn()} />);

    await waitFor(() => {
      expect(screen.getByText(/Product 1/i)).toBeInTheDocument();
      expect(screen.getByText(/Product 2/i)).toBeInTheDocument();
    });
  });

  it('should filter products by search term', async () => {
    const mockProducts = [
      { product_id: 1, name: 'Product 1', price: 10, image_path: 'image1.jpg' },
      { product_id: 2, name: 'Another Product', price: 20, image_path: 'image2.jpg' },
    ];
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockProducts),
      })
    );

    render(<ProductList onAddToCart={jest.fn()} />);

    await waitFor(() => {
      fireEvent.change(screen.getByPlaceholderText(/Search products.../i), {
        target: { value: 'Another' },
      });
    });

    expect(screen.queryByText(/Product 1/i)).not.toBeInTheDocument();
    expect(screen.getByText(/Another Product/i)).toBeInTheDocument();
  });
});
