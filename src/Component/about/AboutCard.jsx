import React from "react"
import "./about.css"
import { homeAbout } from "../../dummydata"

import second from "./second.jpg"


const AboutCard = () => {
  return (
    <>
    <div className="aboutUS">
      <h1>Learn a new skill, launch a project, land your dream career</h1>
      <div className="search">
      <a href="#">Search by role, industry or skill</a>
      </div>
      <div className="learn">
      <button class="Btn">
        Get Started
        </button>
      </div>
      
    </div>


    <h1 className="titleOne">Meet Our top Mentors</h1>
    <div className="mentors">

         <div className="mentor">
            <img src={second} alt=""/>
         </div>
         
         <div className="mentor">
          <img src={second} alt="" srcset="" />
         </div>
         <div className="mentor">
            <img src={second} alt=""/>
         </div>
        </div>
    </>
  )
}

export default AboutCard
