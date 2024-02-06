import React from "react"
import { blog } from "../../../dummydata"
import "./footer.css"

import logof from "../header/Skillsynoc.png"



const Footer = () => {
  return (
    <>
    <div className="overAll">
      <section className='newletter'>
      
      </section>

<footer>
<div className='container'>

  <div className='col'> 

    <div className='pic'>  
       <div className="image_logo">
       <img src={logof} alt="" /> 
        </div>   
      <div>
        <h1>Skillsync</h1>
        <h3>Online mentorship</h3>
      </div> 
     </div>
     <p>A small river named Duden flows by their place and supplies it with the necessary regelialia.</p>
   </div>



  <div className='col'> 
  <h3>Office</h3>
  <p>TIP Road</p>
  <p>AASTU, Addis Ababa</p>
  <p>Alx</p>
  <p className="email_id">info@Skillssync.com</p>
  <h4>+25199 301 8443</h4>

  </div>

  <div className='col'> 
  <h3>Links</h3>
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">Services</a> </li>
    <li><a href="#">About Us</a></li>
    <li><a href="#">Features</a></li>
    <li><a href="#">Contacts</a></li>
  </ul>
  </div>


  <div className='col'> 
  <h3>NewsLetter</h3>
  <form className="form">
    <i className="far fa-envelope"></i>
    <input type="email" placeholder="Enter your email Id" required />
    <button type="submit"><i className="fas fa-arrow-right"> Summit</i></button>
  </form>
  </div>
</div>


<div className='legal'>
<p>
Copyright ©2024 All rights reserved | This template is made with <i className='fa fa-heart'></i> by GorkhCoder
</p>
</div>
</footer>

 </div>
</>
  )
}

export default Footer