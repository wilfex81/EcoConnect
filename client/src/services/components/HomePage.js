import React from 'react';
import './HomePage.css'; // Import your CSS file for styling

function HomePage() {
    return (
        <div className="home-page">
            <header className="header">
                <h1>Welcome to EcoConnect</h1>
                <p>A platform for eco-friendly enthusiasts</p>
            </header>
            <main className="main-content">
                <section className="features">
                    <h2>Features</h2>
                    <ul>
                        <li>Connect with like-minded individuals</li>
                        <li>Share eco-friendly tips and tricks</li>
                        <li>Join events and projects in your community</li>
                    </ul>
                </section>
                <section className="about">
                    <h2>About Us</h2>
                    <p>EcoConnect is dedicated to creating a sustainable future by connecting individuals, communities, and organizations committed to environmental conservation and eco-friendly practices.</p>
                </section>
            </main>
            <footer className="footer">
                <p>&copy; 2024 EcoConnect. All rights reserved.</p>
            </footer>
        </div>
    );
}

export default HomePage;
