// import React from "react"
// import Back from "../common/back/Back"
// import "./contact.css"
// import arrow from './image/arrow_forward_FILL0_wght400_GRAD0_opsz24.png'
// import message from './image/message.png'



// const Contact = () => {
//   const onSubmit = async (event) => {
//     event.preventDefault();
//     const formData = new FormData(event.target);

//     formData.append("access_key", "964665b0-58c8-4fef-8b88-b09c17c93435");

//     const object = Object.fromEntries(formData);
//     const json = JSON.stringify(object);

//     const res = await fetch("https://api.web3forms.com/submit", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         Accept: "application/json"
//       },
//       body: json
//     }).then((res) => res.json());

//     if (res.success) {
//       console.log("Success", res);
//     }
//   };

//   return (
//     <>
//     <section className="body">
//     <div className="contact-container">
//       <form onSubmit={onSubmit} className="contact-left">
//         <div className="contact-left-title">
//           <h2>Get in touch</h2>
//           <hr/>
//         </div>
//         <input type="text" name="name" placeholder="Your Name" className="contact-input" required/>
//         <input type="email" name="email" placeholder="Your Email" className="contact-input" required/>
//         <textarea name="message" placeholder="Your Message" className="contact-input" required></textarea>
//         <button type="submit">Submit <img src= {arrow} className="icon" 
//         style={
//           {width: '40px',
//           height: '40px',
//           marginLeft: '10px'}
//         }
//         /> </button>
//       </form>
//       <div className="contact-right">
//         <img src={message} alt="" 
//         style={
//           {width: '100%',
//           height: '100%',
//           objectFit: 'cover'}
//         }
//         />
//       </div>
//      </div>
//     </section>
     
//     </>
//   )
// }

// export default Contact



import React, { useState } from "react";
import Back from "../common/back/Back";
import "./contact.css";
import arrow from "./image/arrow_forward_FILL0_wght400_GRAD0_opsz24.png";
import message from "./image/message.png";

const Contact = () => {
  const [submitSuccess, setSubmitSuccess] = useState(false);

  const onSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    formData.append("access_key", "964665b0-58c8-4fef-8b88-b09c17c93435");

    const object = Object.fromEntries(formData);
    const json = JSON.stringify(object);

    const res = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: json,
    }).then((res) => res.json());

    if (res.success) {
      console.log("Success", res);
      setSubmitSuccess(true);
    }
  };

  return (
    <>
      <section className="body">
        <div className="contact-container">
          {!submitSuccess ? (
            <form onSubmit={onSubmit} className="contact-left">
              <div className="contact-left-title">
                <h2>Get in touch</h2>
                <hr />
              </div>
              <input
                type="text"
                name="name"
                placeholder="Your Name"
                className="contact-input"
                required
              />
              <input
                type="email"
                name="email"
                placeholder="Your Email"
                className="contact-input"
                required
              />
              <textarea
                name="message"
                placeholder="Your Message"
                className="contact-input"
                required
              ></textarea>
              <button type="submit">
                Submit{" "}
                <img
                  src={arrow}
                  className="icon"
                  style={{
                    width: "40px",
                    height: "40px",
                    marginLeft: "10px",
                  }}
                />{" "}
              </button>
            </form>
          ) : (
            <div className="success-message">
              <p>Successfully Submitted!</p>
              <a href="/">Go Back</a>
            </div>
          )}
          <div className="contact-right">
            <img
              src={message}
              alt=""
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
          </div>
        </div>
      </section>
    </>
  );
};

export default Contact;
