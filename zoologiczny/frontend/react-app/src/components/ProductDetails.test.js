import { render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter, Route } from 'react-router-dom';
import ProductDetails from './ProductDetails';

describe('ProductDetails Component', () => {
  it('should display loading message initially', () => {
    render(
      <MemoryRouter initialEntries={['/products/1']}>
        <Route path="/products/:id">
          <ProductDetails onAddToCart={jest.fn()} />
        </Route>
      </MemoryRouter>
    );
    expect(screen.getByText(/Loading product details.../i)).toBeInTheDocument();
  });

  it('should fetch and display product details', async () => {
    const mockProduct = {
      id: 1,
      name: 'Test Product',
      description: 'A great product',
      price: 100,
      stock_quantity: 10,
      category: 'Electronics',
      subcategory: 'Laptops',
      rating: 4.5,
      image_path: 'image.jpg',
    };
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockProduct),
      })
    );

    render(
      <MemoryRouter initialEntries={['/products/1']}>
        <Route path="/products/:id">
          <ProductDetails onAddToCart={jest.fn()} />
        </Route>
      </MemoryRouter>
    );

    await waitFor(() => {
      expect(screen.getByText(/Test Product/i)).toBeInTheDocument();
      expect(screen.getByText(/Cena: \$100/i)).toBeInTheDocument();
    });
  });

  it('should handle API errors gracefully', async () => {
    global.fetch = jest.fn(() => Promise.reject(new Error('Failed to fetch')));

    render(
      <MemoryRouter initialEntries={['/products/1']}>
        <Route path="/products/:id">
          <ProductDetails onAddToCart={jest.fn()} />
        </Route>
      </MemoryRouter>
    );

    await waitFor(() => {
      expect(screen.getByText(/Could not load product details/i)).toBeInTheDocument();
    });
  });
});
