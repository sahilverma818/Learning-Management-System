import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { SiEducative } from "react-icons/si";
import './Navbar.css'

const Navbar = () => {

    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('access_token')
        navigate('/login')
    }

    return (
        <div>
            <nav className="nav_div">
                <div className="navigation">
                    <Link to="/">
                        <div className="nav_header">
                            <div className="logo">< SiEducative/></div>
                            <h2 className="nav_logo"><span>Edu</span>Kative</h2>
                        </div>
                    </Link>
                    <div className="links">
                        <ul>
                            <li> Courses </li>
                            <li> Contacts </li>
                            <Link to={'profile'}>
                                <li>  Profile </li>
                            </Link>
                        </ul>
                    </div>
                    { !localStorage.getItem('access_token') ? (
                        <div className="nav_button">
                            <Link to={'login'}>
                                <button> Login </button>
                            </Link>
                            <Link to={'register'}>
                                <button> Sign Up </button>
                            </Link>

                        </div>
                    ) : (
                        <div className="nav_button">
                            <Link to={'login'}>
                                <button onClick={handleLogout}> Logout </button>
                            </Link>
                        </div>
                    )}
                </div>
            </nav>
        </div>
    )
}

export default Navbar