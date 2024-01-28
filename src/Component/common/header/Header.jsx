import React, { useState } from "react"
import { Link } from "react-router-dom"
import Head from "./Head"
import "./header.css"
import { team } from "../../../dummydata"

const Header = () => {
  const [click, setClick] = useState(false)

  return (
    <>
      <Head />
      <header>
        <nav className='flexSB'>
          
          <ul className={click ? "mobile-nav" : "flexSB "} onClick={() => setClick(false)}>
            <li>
              <Link to='/'>Home</Link>
            </li>
                        <li>
              <Link to='/about'>About</Link>
            </li>
            <li>
              {/* <a href={team}>Team</a> */}
              <a href="team">Team</a>
            </li>
                      <li>
              <Link to='/journal'>Journal</Link>
            </li>
            <li>
              <Link to='/contact'>Contact</Link>
            </li>
          </ul>


          <div className='start'>
            <Link to='/mentee' className='button'>
                 <h3>To be Mentee</h3> 
            </Link>
              <div className="button">To be Mentor</div>
            </div>
          <button className='toggle' onClick={() => setClick(!click)}>
            {click ? <i className='fa fa-times'> </i> : <i className='fa fa-bars'></i>}
          </button>
        </nav>
      </header>
    </>
  )
}

export default Header
