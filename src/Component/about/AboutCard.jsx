import React from "react"
import "./about.css"
import { homeAbout } from "../../dummydata"

const AboutCard = () => {
  return (
    <>
    <div className="aboutUS">
      <h1>Learn a new skill, launch a project, land your dream career</h1>
    </div>


    <div className="search">
      <a href="#">Search by role,industry or skill</a>
      <a href="#">
        <button className="get_started">Search Menber</button>
      </a>
    </div>


    <div className="learn">
      <a href="#">
        <button className="get_startedadd">Get Started</button>
      </a>

      <a href="#">
        <button className="learn_more">Learn More</button>
      </a>
    </div>
    </>
  )
}

export default AboutCard
