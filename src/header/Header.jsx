import React, { useState } from 'react';
import './Header.css';
import LoginSignup from '../Component/LoginSignup/loginSignup'; 
import Logo from "../Component/assets/logo.jpg"


const Header = () => {
  const [showLoginSignup, setShowLoginSignup] = useState(false);

  const handleMenteeClick = () => {
    setShowLoginSignup(true);
  };

  return (
    <header className="app-header">
      <div className="left-content">
        <img src={Logo} alt="Logo" className='logo-image'/>
      <h1>Skillsyncs</h1>
        <nav>
          {!showLoginSignup && <a href="#" onClick={handleMenteeClick}>To be mentee</a>}
          <a href="#">To be mentor</a>
          <a href="#">About Us</a>
          <a href="#">Contact Us</a>
        </nav>
      </div>
      {showLoginSignup && <LoginSignup />}      
    </header>
  );
};
export default Header;