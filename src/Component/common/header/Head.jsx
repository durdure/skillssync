import React from "react"
import logoImage from '../header/Skillsynoc.png'

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

            <button className="buttonThree"> <h1>SingIn/SignUp</h1></button>
        </div>
      </section>
    </>
  )
}

export default Head
