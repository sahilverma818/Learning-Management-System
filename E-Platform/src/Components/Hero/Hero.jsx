import React from "react";
import './Hero.css'
import classroom from '../../assets/class.jpg'

const Hero = () => {
    return (
        <div>
            <div className="hero">
                <h1 className="hero_header">
                    Unlock Your Potential With Top Tier Online Courses
                </h1>
                <p> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Pariatur quas nesciunt aliquid amet debitis quos, laboriosam nostrum, molestiae repudiandae, doloribus atque rem esse dolorum. Minima.</p>
                <div className="btn">
                    <button className="cta_button"> Explore Courses </button>
                </div>
                <img src={classroom} alt="" />
            </div>
        </div>
    )
}

export default Hero