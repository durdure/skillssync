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
          <div className="button">
              <button>Singin/SignUp</button>
            </div>

          <div className='social'>
            <i className='fab fa-facebook-f icon'></i>
            <i className='fab fa-instagram icon'></i>
            <i className='fab fa-twitter icon'></i>
            <i className='fab fa-youtube icon'></i>
          </div> 
        </div>
      </section>
    </>
  )
}

export default Head
