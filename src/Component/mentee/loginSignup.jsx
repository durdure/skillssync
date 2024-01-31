
import React, { useState } from 'react';
import './loginSignup.css';

import { getAuth } from '../firebase/app';
import { auth } from '../firebase/app';
import 'firebase/auth';

import user_icon from '../assets/person_FILL0_wght400_GRAD0_opsz24.png';
import email_icon from '../assets/mail_FILL0_wght400_GRAD0_opsz24.png';
import password_icon from '../assets/lock_FILL0_wght400_GRAD0_opsz24.png';


export default function LoginSignup() {
    const [action, setAction] = useState("Sign Up")
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    
    const handleAuthentication = async () => {
      try {
        if (action === 'Sign Up') {
          await auth.createUserWithEmailAndPassword(email, password);
        } else {
          await auth.signInWithEmailAndPassword(email, password);
        }
        console.log('Authentication successful');
      } catch (error) {
        console.error('Authentication failed', error.message);
      }
    }

  return (
    <div className="container">

      <div className="header">
        <div className="text">{action}</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        {action === 'Login' ? null : (
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
          <div
            className={action === 'Login' ? 'submit gray' : 'submit'}
            onClick={() => handleAuthentication()}
          >
            Sign Up
          </div>
          <div
            className={action === 'Sign Up' ? 'submit gray' : 'submit'}
            onClick={() => handleAuthentication()}
          >
            Log In
          </div>
        </div>
      </div>
    </div>
  );
}

