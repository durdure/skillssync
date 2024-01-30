import React from "react"
import { blog } from "../../../dummydata"
import "./footer.css"
import image_ppi from "../header/one_1111-removebg-preview.png"
import logof from "../header/Skillsynoc.png"


const Footer = () => {
  return (
    <>
      <section className='newletter'>

            <div className="note">
              <h1>Newsletter - Stay tune and get the latest update</h1>
              <span>Far far away, behind the word mountains</span>
              <div className="buttonOne">
                <button className="Get"> Get Started</button>
                <button className="Get"> Learn More</button>
                </div>
             
            </div>
            <img src={image_ppi} alt="" />
      </section>








      <footer>
        <div className='container padding'>
          <div className='box logo'> 


              <div className='logo'>     
                  <img src={logof} alt="" />    
                  <div className="onoo">
                    <h1>Skillsync</h1>
                  </div> 
                  <i className='fab fa-facebook-f icon'></i>
                  <i className='fab fa-twitter icon'></i>
                  <i className='fab fa-instagram icon'></i>
             </div>
             <p>A small river named Duden flows by their place and supplies it with the necessary regelialia.</p>
            </div>

            <div className='box link'>
            <h3>Explore</h3>
            <ul>
              <li>About Us</li>
              <li>Services</li>
              <li>Courses</li>
              <li>Blog</li>
              <li>Contact us</li>
            </ul>
          </div>
          <div className='box link'>
            <h3>Quick Links</h3>
            <ul>
              <li>Contact Us</li>
              <li>Pricing</li>
              <li>Terms & Conditions</li>
              <li>Privacy</li>
              <li>Feedbacks</li>
            </ul>
          </div>
          <div className='box'>
            <h3>Recent Post</h3>
            {blog.slice(0, 3).map((val) => (
              <div className='items flexSB'>
                <div className='img'>
                  <img src={val.cover} alt='' />
                </div>
                <div className='text'>
                  <span>
                    <i className='fa fa-calendar-alt'></i>
                    <label htmlFor=''>{val.date}</label>
                  </span>
                  <span>
                    <i className='fa fa-user'></i>
                    <label htmlFor=''>{val.type}</label>
                  </span>
                  <h4>{val.title.slice(0, 40)}...</h4>
                </div>
              </div>
            ))}
          </div>
          <div className='box last'>
            <h3>Have a Questions?</h3>
            <ul>
              <li>
                <i className='fa fa-map'></i>
                203 Fake St. Mountain View, San Francisco, California, USA
              </li>
              <li>
                <i className='fa fa-phone-alt'></i>
                +2 392 3929 210
              </li>
              <li>
                <i className='fa fa-paper-plane'></i>
                info@yourdomain.com
              </li>
            </ul>
          </div>
        </div>
      </footer>
      <div className='legal'>
        <p>
          Copyright ©2022 All rights reserved | This template is made with <i className='fa fa-heart'></i> by GorkhCoder
        </p>
      </div>
      
    </>
  )
}


export default Footer
