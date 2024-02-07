import React from "react"
import Back from "../common/back/Back"
import "./team.css"
// import "../about/about.css"


import dure from "./image/Duresa.jpg"

export default function Team() {
  return (
    <>
       <Back title='Meet our Team' />
       <section className='team padding'>
         <div className='container grid'>

           <div className="Duresa">
            <img src={dure} />
            <h1>Duresa Eshetu</h1>
            <h3>Full stack and Mining Engineer</h3>
            <div className="lineShow"></div>

            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
              Asperiores iste voluptatibus non ducimus. Voluptatem ex suscipit repudiandae, 
              dignissimos ipsum perferendis magnam voluptates aliquid debitis odio minus eveniet
               rerum saepe accusamus!
               </p>

           </div>


           <div className="Duresa">
            <img src={dure} />
            <h1>Duresa Eshetu</h1>
            <h3>Full stack and Mining Engineer</h3>
            <div className="lineShow"></div>

            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
              Asperiores iste voluptatibus non ducimus. Voluptatem ex suscipit repudiandae, 
              dignissimos ipsum perferendis magnam voluptates aliquid debitis odio minus eveniet
               rerum saepe accusamus!
               </p>

           </div>


           <div className="Duresa">
            <img src={dure} />
            <h1>Duresa Eshetu</h1>
            <h3>Full stack and Mining Engineer</h3>
            <div className="lineShow"></div>

            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
              Asperiores iste voluptatibus non ducimus. Voluptatem ex suscipit repudiandae, 
              dignissimos ipsum perferendis magnam voluptates aliquid debitis odio minus eveniet
               rerum saepe accusamus!
               </p>
           </div>

         </div>
       </section>
    
     </>
   )
 }
  