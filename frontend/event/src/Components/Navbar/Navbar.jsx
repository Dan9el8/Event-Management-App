import React from 'react'
import './Navbar.css'
import logo from '../../assets/logo.png'

const Navbar = () => {
  return (
    <div className='nav'> 
    <img src={logo} alt="" />       
            <ul className='nav-menu'>
                <li>Home</li>
                <li>About</li>
                <li>Events</li>
                <li>Contact</li>
                <li>Sign-up</li>
            </ul>
            <div className="sign-up">Sign-up</div>      
    </div>
  )
}

export default Navbar
