import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { SiEducative } from "react-icons/si";
import './Navbar.css'

const Navbar = () => {

    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('user_role')
        localStorage.removeItem('user_id')
        navigate('/login')
    }

    return (
        <div>
            <nav className="nav_div">
                <div className="navigation">
                    <Link to="/">
                        <div className="nav_header">
                            <div className="logo">< SiEducative/></div>
                            <h2 className="nav_logo"><span>Edu</span>Verse</h2>
                        </div>
                    </Link>
                    <div className="links">
                        <ul>
                            <Link to={'courses'}>
                                <li> Courses </li>
                            </Link>
                            <Link to={'/contacts'}>
                                <li> Contacts </li>
                            </Link>
                            <Link to={'/profile'}>
                                <li>  Profile </li>
                            </Link>
                            { localStorage.getItem('user_role') === 'admin' ? (
                                <Link to={'/dashboard'}>
                                    <li> Dashboard </li>
                                </Link>
                            ) : null}
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