import React, { useEffect, useState } from "react"
import logoImage from '../header/Skillsynoc.png'
import { Link } from "react-router-dom"

const Head = () => {
  const [login, setLogin] = useState( localStorage.getItem("logedin") || "false");
  const handleLogout = () => {
    if (login == "true") {
      localStorage.setItem("logedin", false);
      // refresh the page
      window.location.reload();
      setLogin("false");
      window.location.href = "/mentee";
    }
  };


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
          <Link to={login == "true"? "/mainpage/dashboard" : '/mentee'}>
          <button className="buttonThree" onClick={handleLogout}>  <h1>{login == "true"? "Logout": "Login"}</h1></button>
          </Link>   
        </div>
      </section>
    </>
  )
}

export default Head















// import React from 'react'

// export default function Head() {
//   return (
//     <div>Head</div>
//   )
// }
