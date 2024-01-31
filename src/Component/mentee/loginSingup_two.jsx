
// import React, { useState } from 'react'
// import './loginSignup.css'

// import user_icon from '../assets/person_FILL0_wght400_GRAD0_opsz24.png'
// import email_icon from '../assets/mail_FILL0_wght400_GRAD0_opsz24.png'
// import password_icon from '../assets/lock_FILL0_wght400_GRAD0_opsz24.png'

// export default function LoginSignup() {
//     const [action, setAction] = useState("Sign Up")
//   return (
//     <div className="container">

//        <div className="header">
//             <div className="text">{action}</div>
//             <div className="underline"></div>
//        </div>

//             <div className="inputs">
//             {action==="Login" ? <div></div> : <div className="input">
//                     <img src={user_icon} alt="" />
//                     <input type="text" placeholder='name' required />
//                 </div>}
                
//                 <div className="input">
//                     <img src={email_icon} alt="" />
//                     <input type="email" placeholder='Email' required='@gmail.com' />
//                 </div>
//                 <div className="input">
//                     <img src={password_icon} alt="" />
//                     <input type="password" placeholder='Password' />
//                 </div>
//                 {action === "Sign Up" ? <div></div>:<div className="forgot-password">
//                     Lost Password
//                     <span>Click here</span></div>}            
//                 <div className="submit-container">
//                     <div className= {action === "Login" ? "submit gray":"submit"} onClick={()=>{(setAction("Sign Up"))}} >Sign Up</div>
//                     <div className= {action === "Sign Up"? "submit gray":"submit"} onClick={()=>{(setAction("Login"))}} >Log In</div>
//                 </div>
//             </div>
//         </div>             
//   );
// };
