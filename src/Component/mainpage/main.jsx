// main.jsx
import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import "./main.css"


const Main = () => {
  return (
    <>
     <div className='classOne'>
      <div className='firstone'>
      <li>
            <Link to="/mainpage/dashboard">Home</Link>
          </li>
        <li>
            <Link to="/mainpage/dashboard">dashboard</Link>
          </li>
          <li>
            <Link to="/mainpage/dashboard">dashboard</Link>
          </li>
          <li>
            <Link to="/mainpage/profile">Profile</Link>
          </li>
          <li>
            <Link to="/mainpage/profile">LogOut</Link>
          </li>
      </div>

      <Routes>
        <Route path="dashboard" element={<dashboard />} />
        <Route path="profile" element={<profile />} />
      </Routes>
    </div>
    </>
   
  );
};

export default Main;
