import React, { useState } from 'react';
import './loginSignup.css';

import { auth } from "../../firebase";
import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

import user_icon from '../assets/person_FILL0_wght400_GRAD0_opsz24.png';
import email_icon from '../assets/mail_FILL0_wght400_GRAD0_opsz24.png';
import password_icon from '../assets/lock_FILL0_wght400_GRAD0_opsz24.png';
import { useNavigate } from 'react-router-dom';


export default function LoginSignup() {
    const [action, setAction] = useState("Sign Up")
    const [email, setEmail] = useState('duresaeshetu2001@gmail.com');
    const [password, setPassword] = useState('DURE488e@AASTU');
    const [authenticated, setAuthenticated] = useState(false);
    const navigate = useNavigate();
    
    const handleAuthentication = async () => {
      try {
        if (action === 'Sign Up') {
          try {
              const response = await createUserWithEmailAndPassword(auth, email, password);
              setAuthenticated(true);
              navigate("/");
          } catch(error) {
              console.log("Sorry, something went wrong. Please try again.");
              console.log(error);
          }
        } else {
          try {
              await signInWithEmailAndPassword(auth, email, password).then(
                (user) => console.log(user)
              )
              localStorage.setItem("logedin", true)
              setAuthenticated(true);
              navigate("./profile");
          } catch(error) {
              console.log(error.message);
          }
        }

      } catch (error) {
        console.error('Authentication failed', error.message);
      }
    }

    if (authenticated){
      navigate('/main')
      return null
    }

  return (
    <div className="container">

      <div className="header">
        <div className="text">{action}</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        {action === 'Log In' ? null : (
          <div className="input">
            <img src={user_icon} alt="" />
            <input type="text" placeholder="name" required />
          </div>
        )}

        <div className="input">
          <img src={email_icon} alt="" />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          
        </div>
        <div className="input">
          <img src={password_icon} alt="" />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>


        {action === 'Sign Up' ? null : (
          <div className="forgot-password">
            Lost Password
            <span>Click here</span>
          </div>
        )}
        <div className="submit-container">
          <div className={action === 'Log In' ? 'submit gray' : 'submit'} onClick={() => {action === "Sign Up" ?  handleAuthentication() : setAction("Sign Up")}}> Sign Up </div>

          <div
            className={action === 'Sign Up' ? 'submit gray' : 'submit'}
            onClick={() => {
              action === "Log In" ? handleAuthentication() : setAction("Log In"); 
            }}
          >
            Log In
          </div>

        </div>
      </div>
    </div>
  );
}