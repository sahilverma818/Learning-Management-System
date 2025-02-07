import React from "react";
import "./Footer.css";
import { FaFacebookF, FaTwitter, FaInstagram, FaLinkedin } from "react-icons/fa";

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer_container">
                <div className="footer_about">
                    <h2>EduPlatform</h2>
                    <p>Your trusted learning partner for quality online education.</p>
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
