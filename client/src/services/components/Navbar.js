import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import the CSS file

function Navbar() {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/users">Users</Link></li>
                <li><Link to="/posts">Posts</Link></li>
                <li><Link to="/projects">Projects</Link></li>
                <li><Link to="/login">Login</Link></li>
                
            </ul>
        </nav>
    );
}

export default Navbar;
