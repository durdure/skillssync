import React from "react"
import Back from "../common/back/Back"
import "./team.css"
import Awrapper from "../about/Awrapper"
import "../about/about.css"


import dure from "./image/Duresa.jpg"
import telegram_icone from "./image/icon_telegram-removebg-preview.png"
import youTobe_icon from "./image/youTobe.png"
import whatup_icon from './image/whatup.png'
import tiktok_icon from "./image/tiktok.png"

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
       <Awrapper />
     </>
   )
 }
  