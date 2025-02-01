import React from 'react'
import './Hero.css'

const Hero = () => {
  return (
    <div className="hero-container">
      <div className="animated-background">
        <div className="cube"></div>
        <div className="cube"></div>
        <div className="cube"></div>
        <div className="cube"></div>
        <div className="cube"></div>
      </div>
      <div className="hero-content">
        <h1 className="hero-title">Welcome to Koully</h1>
        <p className="hero-subtitle">Discover and create unforgettable experiences</p>
        <button className="hero-button">Explore Events</button>
      </div>
    </div>
  )
}

export default Hero
