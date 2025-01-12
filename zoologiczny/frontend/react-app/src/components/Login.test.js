import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Login from './Login';

describe('Login Component', () => {
  it('should render the login form', () => {
    render(<Login onLogin={jest.fn()} />);
    expect(screen.getByLabelText(/Email:/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Password:/i)).toBeInTheDocument();
  });

  it('should display error message on invalid credentials', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: false,
      })
    );

    render(<Login onLogin={jest.fn()} />);

    fireEvent.change(screen.getByLabelText(/Email:/i), {
      target: { value: 'test@example.com' },
    });
    fireEvent.change(screen.getByLabelText(/Password:/i), {
      target: { value: 'wrongpassword' },
    });
    fireEvent.click(screen.getByText(/Login/i));

    await waitFor(() => {
      expect(screen.getByText(/Invalid email or password/i)).toBeInTheDocument();
    });
  });

  it('should store tokens and call onLogin on successful login', async () => {
    const mockResponse = {
      access_token: 'access123',
      refresh_token: 'refresh123',
    };
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve(mockResponse),
      })
    );
    const mockOnLogin = jest.fn();

    render(<Login onLogin={mockOnLogin} />);

    fireEvent.change(screen.getByLabelText(/Email:/i), {
      target: { value: 'test@example.com' },
    });
    fireEvent.change(screen.getByLabelText(/Password:/i), {
      target: { value: 'correctpassword' },
    });
    fireEvent.click(screen.getByText(/Login/i));

    await waitFor(() => {
      expect(localStorage.getItem('accessToken')).toBe('access123');
      expect(localStorage.getItem('refreshToken')).toBe('refresh123');
      expect(mockOnLogin).toHaveBeenCalledWith({ username: 'test@example.com' });
    });
  });
});
