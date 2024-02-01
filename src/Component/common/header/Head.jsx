import React from "react"
import logoImage from '../header/Skillsynoc.png'
import { Link } from "react-router-dom"

const Head = () => {
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
          <button className="buttonThree"> <h1>SingIn/SignUp</h1></button>
          </Link>
            
        </div>
      </section>
    </>
  )
}

export default Head
