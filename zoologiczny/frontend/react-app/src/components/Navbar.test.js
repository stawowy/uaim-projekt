import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import Navbar from './Navbar';

test('renders Navbar with correct links', () => {
  render(
    <Router>
      <Navbar cartCount={2} user={{ username: 'JohnDoe' }} />
    </Router>
  );

  expect(screen.getByText(/Home/i)).toBeInTheDocument();
  expect(screen.getByText(/Products/i)).toBeInTheDocument();
  expect(screen.getByText(/Cart \(2\)/i)).toBeInTheDocument();
  expect(screen.getByText(/Welcome, JohnDoe/i)).toBeInTheDocument();
});
