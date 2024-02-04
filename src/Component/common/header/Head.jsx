import React, { useEffect, useState } from "react"
import logoImage from '../header/Skillsynoc.png'
import { Link } from "react-router-dom"

const Head = () => {
  const [login, setLogin] = useState( localStorage.getItem("logedin") || "false");

  useEffect(() => {
    const handleStorageChange = () => {
      setLogin(localStorage.getItem('logedin') || 'false');
    };

    // Listen for storage changes
    window.addEventListener('storage', handleStorageChange);

    // Cleanup the listener on component unmount
    return () => {
      window.removeEventListener('storage', handleStorageChange);
    };
  }, []);

  return (
    <>
      <section className='head'>
        
        <div className='container flexSB'>
          <img src={logoImage} alt="" srcset="" />
          <div className='logo'>
            <h1>Skillsync</h1>
            <span>Online Mentorship</span>
          </div>          
          <div className="flower"></div>
          <Link to='/mentee'>
          <button className="buttonThree"> <h1>{login == "true"? "yes": "else"}</h1></button>
          </Link>   
        </div>
      </section>
    </>
  )
}

export default Head
