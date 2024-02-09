import React from 'react'

import pci from './aboutus.jpg'


export default function About() {
  return (
    <section className="heor">
      <div className="heading">
        <h1>About Us</h1>
      </div>
      <div className="container">
        <div className="hero-content">
          <h2>Welcome to Our Website</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing 
            elit. Voluptas, repellendus, adipisci soluta sint nulla 
            eos dolorem amet debitis quos nisi voluptatem ex facere 
            cumque vitae officiis neque. In, rerum soluta?</p>
          <button className="cta-button">Learn More</button>
        </div>
        <div className="hero-image">
        <img src={pci} alt="" srcset="" />
        </div>
        
      </div>
    </section>
  )
}
