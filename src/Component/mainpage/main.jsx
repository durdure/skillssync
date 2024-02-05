// main.jsx
import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import Dashboard from './Dashboard'; // Import your Dashboard component
import Profile from './profile/profile'; // Import your Profile component
import "./main.css";

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
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="profile" element={<Profile />} />
      </Routes>
    </div>
    </>
  );
};

export default Main;
