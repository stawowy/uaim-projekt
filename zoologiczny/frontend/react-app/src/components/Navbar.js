import { Link } from 'react-router-dom';

const Navbar = ({ cartCount, user , onLogout}) => {
    return (
      <nav className="navbar">
            {/* Logo Section */}
                <Link to="/" className="navbar-logo">
                <img src="https://logowik.com/content/uploads/images/black-circle-pet-shop5686.logowik.com.webp" alt="Pet Shop Logo" className="logo-image" />
            </Link>
        <ul className="navbar-list">
          <li className="navbar-item"><Link to="/" className="navbar-link">Strona główna</Link></li>
          <li className="navbar-item"><Link to="/products" className="navbar-link">Produkty</Link></li>
          <li className="navbar-item"><Link to="/cart" className="navbar-link">Koszyk ({cartCount})</Link></li>
          {user ? (
            <>
              <li className="navbar-item">Welcome, {user.username}</li>
              <li className="navbar-item"><Link to="/profile" className="navbar-link">Profil</Link></li>
              <li className="navbar-item">
              <button onClick={onLogout} className="logout-button">Logout</button>
            </li>
            </>
          ) : (
            <>
              <li className="navbar-item"><Link to="/register" className="navbar-link">Rejestracja</Link></li>
              <li className="navbar-item"><Link to="/login" className="navbar-link">Login</Link></li>
            </>
          )}
        </ul>
      </nav>
    );
  };
  export default Navbar;