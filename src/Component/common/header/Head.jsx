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
            <span>ONLINE Mentorship</span>
          </div>

            <button className="buttonThree"> SignIn/SignUp</button>
        </div>
      </section>
    </>
  )
}

export default Head
