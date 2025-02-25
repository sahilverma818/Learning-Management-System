import React from "react";
import "./Footer.css";
import { FaFacebookF, FaTwitter, FaInstagram, FaLinkedin } from "react-icons/fa";
import { SiEducative } from "react-icons/si";

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer_container">
                <div className="foot_header">
                    <div className="logo">< SiEducative /></div>
                    <h2 className="foot_logo"><span>Edu</span>Verse</h2>
                </div>

                <div className="footer_links">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Courses</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </div>

                <div className="footer_social">
                    <h3>Follow Us</h3>
                    <div className="social_icons">
                        <a href="#"><FaFacebookF /></a>
                        <a href="#"><FaTwitter /></a>
                        <a href="#"><FaInstagram /></a>
                        <a href="#"><FaLinkedin /></a>
                    </div>
                </div>
            </div>

            <div className="footer_bottom">
                <p>© {new Date().getFullYear()} EduPlatform. All Rights Reserved.</p>
            </div>
        </footer>
    );
};

export default Footer;
