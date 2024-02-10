import React from "react"
import "./about.css"
import { homeAbout } from "../../dummydata"

import second from "./teacher1-removebg-preview.png"


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


    <section id="team">
      <div className="team-heading">
        <h3>Our Top Mentor</h3>
      </div>
      <div className="team-box">
        <div className="b-t-image">
          <img src={second} alt=""
          style={
            {
              width:"500px",
              marginTop:"30px"
            }
          }
          />
        </div>
        <div className="b-t-text">
          <strong>Julia William</strong>
          <span>AI Engineer</span>
        </div>
      </div>
    </section>
    </>
  )
}

export default AboutCard
