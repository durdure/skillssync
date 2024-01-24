/// Header.jsx
import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="app-header">
      <h1>Skillsyncs</h1>
      <div className="left-content">
        <nav>
          <a href= "./Component/loginSignup">To be mentee</a>
          <a href="#">To be mentor</a>
          <a href="#">About Us</a>
          <a href="#">Contact Us</a>
        </nav>
      </div>
      {/* Add other header elements as needed */}
    </header>
  );
};

export default Header;
