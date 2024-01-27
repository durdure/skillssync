// 
// About.jsx
import React from "react";
import "./about.css";
import Back from "../common/back/Back";
import AboutCard from "./AboutCard";

const About = () => {
  console.log("About component rendered");
  return (
    <>
      <Back title='About Us' />
      <AboutCard />
    </>
  );
};

export default About;
