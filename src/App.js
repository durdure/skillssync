// App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./Component/common/header/Header";
import About from "./Component/about/About";
// import CourseHome from "./Component/allcourses/CourseHome";
import Team from "./Component/team/Team";
// import Pricing from "./Component/pricing/Pricing";
// import Blog from "./Component/blog/Blog";
import Contact from "./Component/contact/contact";
import Footer from "./Component/common/footer/Footer";
import Home from "./Component/home/Home";
// import LoginSignup from './Component/mentee/loginSignup';
// import AboutHome from "./Component/about/AboutHome";
import LogInSingUp from "./Component/mentee/loginSignup"

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
          <Route path='/' element={<Home />} />
           <Route path='/about' element={<About />} />
          {/* <Route path='/courses' element={<CourseHome />} /> */}
          <Route path='/team' element={<Team />} />
          {/* <Route path='/pricing' element={<Pricing />} /> */}
          {/* <Route path='/journal' element={<Blog />} /> */}
          <Route path='/contact' element={<Contact />} />
          <Route path='/mentee' element={<LogInSingUp />}/>
        </Routes>
         <Footer />
      </Router>
    </>
  );
}

export default App;
