import React from "react"
import "./about.css"
import { homeAbout } from "../../dummydata"


import { Swiper, SwiperSlide } from 'swiper/react';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/pagination';


// import required modules
import { EffectCoverflow, Pagination } from 'swiper/modules';

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
        <Swiper
        effect={'coverflow'}
        grabCursor={true}
        centeredSlides={true}
        slidesPerView={'auto'}
        coverflowEffect={{
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 3,
          slideShadows: true,
        }}
        pagination={true}
        modules={[EffectCoverflow, Pagination]}
        className="mySwiper"
      >
         <SwiperSlide className="swipper-slide">
         <div className="team-box">
        <div className="b-t-image">
          <img src={second} alt=""
          style={
            {
              width:"500px",
              marginTop:"30px",
              paddingLeft:"150px"
            }
          }
          />
        </div>
        <div className="b-t-text">
          <strong>Julia Wi</strong>
          <span>AI Engineer</span>
        </div>
      </div>
        </SwiperSlide> 

        <SwiperSlide className="swipper-slide">
         <div className="team-box">
        <div className="b-t-image">
          <img src={second} alt=""
          style={
            {
              width:"500px",
              marginTop:"30px",
              paddingLeft:"150px"
            }
          }
          />
        </div>
        <div className="b-t-text">
          <strong>Julia William</strong>
          <span>AI Engineer</span>
        </div>
      </div>
        </SwiperSlide>


        <SwiperSlide className="swipper-slide">
         <div className="team-box">
        <div className="b-t-image">
          <img src={second} alt=""
          style={
            {
              width:"500px",
              marginTop:"30px",
              paddingLeft:"150px"
            }
          }
          />
        </div>
        <div className="b-t-text">
          <strong>Julia William</strong>
          <span>AI Engineer</span>
        </div>
      </div>
        </SwiperSlide>


      </Swiper>

    </section>
    </>
  )
}

export default AboutCard
