import React from "react"
import Back from "../common/back/Back"
import "./team.css"
// import "../about/about.css"



import dure from "./image/Duresa.jpg"
import tik from "./image/tiktok.png"
import alik from "./image/Alik.jpg"

export default function Team() {
  return (
    <>
     <div className="team-section">
      <h1>Our Team</h1>
      <span className="border"></span>
    <div className="ps">
      <a href="#p1"><img src={dure} alt="" 
      style={{width: "200px", borderRadius: "100px", height: "200px",}}
      /></a>
      <a href="#p2"><img src={tik} alt="" /></a>
      <a href="#p3"><img src={alik} alt="" /></a>
    </div>
    <div className="section" id="p1">
      <span className="name">Duresa Eshetu</span>
      <span className="border"></span>
      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Reiciendis, tempora fugit libero eveniet praesentium est 
        deserunt aperiam a asperiores quibusdam nostrum dignissimos,
         impedit pariatur modi. Laudantium perspiciatis dignissimos 
         omnis porro?</p>
     </div>
     <div className="section" id="p2">
      <span className="name">Duresa Eshetu</span>
      <span className="border"></span>
      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
        Reiciendis, tempora fugit libero eveniet praesentium est 
        deserunt aperiam a asperiores quibusdam nostrum dignissimos,
         impedit pariatur modi. Laudantium perspiciatis dignissimos 
         omnis porro?</p>
     </div>
     <div className="section" id="p3">
      <span className="name">Duresa Eshetu</span>
      <span className="border"></span>
      <p> yye yegabg soiewudolor sit, amet consectetur adipisicing elit. 
        Reiciendis, tempora fugit libero eveniet praesentium est 
        deserunt aperiam a asperiores quibusdam nostrum dignissimos,
         impedit pariatur modi. Laudantium perspiciatis dignissimos 
         omnis porro?</p>
     </div>
     </div>
   
     </>
   )
 }
  