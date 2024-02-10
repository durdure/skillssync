// main.jsx
import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import Dashboard from './dashboard/dashboard'; // Import your Dashboard component
import Profile from './profile/profile'; // Import your Profile component
import "./main.css";

import Home_chat from './Home_chat';


const Main = () => {
  return (
    <>
     <div className='classOne'>
      <div className='firstone'>
          <li>
            <Link to="/mainpage/dashboard">Home</Link>
          </li>
          <li>
            <Link to="./Home_chat">chat</Link>
          </li>
          <li>
            <Link to="/mainpage/profile">Profile</Link>
          </li>
          <li>
            <Link to="/mainpage/profile">LogOut</Link>
          </li>
      </div>

      <Routes>
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="profile" element={<Profile />} />
      </Routes>
    </div>
    </>
  );
};

export default Main;
