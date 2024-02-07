import React from "react"
import Back from "../common/back/Back"
import "./team.css"
// import "../about/about.css"


import dure from "./image/Duresa.jpg"
import bag from "./image/backGd.jpg"
import facebok from "./image/facebook.png"
import youTobe from "./image/youTobe.png"
import whatup from "./image/whatup.png"

export default function Team() {
  return (
    <>
       <Back title='Meet our Team' />
       <section className='team padding'>
        <div className="container">
          <h1 className="heading">MEET THE TEAM</h1>
          <div className="card-warpper">

            
            <div className="card">
              <img src={bag} alt="card background" className="card-img" />
              <img src={dure} alt="profile image" className="profile-img" />
              <h1>Duresa Eshetu</h1>
              <p className="job-title">Web Developer</p>
              <p className="about">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                Eius possimus excepturi magnam perspiciatis corrupti? Ullam, 
                quam asperiores pariatur quia amet ducimus impedit aspernatur 
                voluptas ex odit at, qui excepturi laboriosam?
              </p>
              <a href="#" className="btn">Contact</a>
              <ul className="social-media">
                <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-facebook-f"><img src={facebok} alt="" /></i> </a> </li>
               
               <li> 
                  <a href=""> <i className="fab fa-youTobe-f"><img src={youTobe} alt="" /></i> </a> </li>

                
                <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-whatsapp-f"><img src={whatup} alt="" /></i> </a> </li>
              </ul>
            </div>

            <div className="card">
              <img src={bag} alt="card background" className="card-img" />
              <img src={dure} alt="profile image" className="profile-img" />
              <h1>Duresa Eshetu</h1>
              <p className="job-title">Web Developer</p>
              <p className="about">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                Eius possimus excepturi magnam perspiciatis corrupti? Ullam, 
                quam asperiores pariatur quia amet ducimus impedit aspernatur 
                voluptas ex odit at, qui excepturi laboriosam?
              </p>
              <a href="#" className="btn">Contact</a>
              <ul className="social-media">
                <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-facebook-f"><img src={facebok} alt="" /></i> </a> </li>
               
               <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-youTobe-f"><img src={youTobe} alt="" /></i> </a> </li>

                
                <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-whatsapp-f"><img src={whatup} alt="" /></i> </a> </li>
              </ul>
            </div>


            <div className="card">
              <img src={bag} alt="card background" className="card-img" />
              <img src={dure} alt="profile image" className="profile-img" />
              <h1>Duresa Eshetu</h1>
              <p className="job-title">Web Developer</p>
              <p className="about">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                Eius possimus excepturi magnam perspiciatis corrupti? Ullam, 
                quam asperiores pariatur quia amet ducimus impedit aspernatur 
                voluptas ex odit at, qui excepturi laboriosam?
              </p>
              <a href="#" className="btn">Contact</a>
              <ul className="social-media">
                <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-facebook-f"><img src={facebok} alt="" /></i> </a> </li>
               
               <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-youTobe-f"><img src={youTobe} alt="" /></i> </a> </li>

                
                <li> 
                  <a href=""> <i style={
                  {color: "blue"}
                } className="fab fa-whatsapp-f"><img src={whatup} alt="" /></i> </a> </li>
              </ul>
            </div>

          </div>
         </div>
       </section>
    
     </>
   )
 }
  