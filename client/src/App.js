import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './services/components/Navbar';
import HomePage from './services/components/HomePage';
import UserProfileForm from './services/components/UserProfileForm';
import PostList from './services/components/PostList';
import ProjectList from './services/components/ProjectList';
import Login from './services/components/Login';


function App() {
    return (
        <Router>
            <div className="app">
                <Navbar />
                <Routes>
                    <Route exact path="/" element={<HomePage />} />
                    <Route path="/users" element={<UserProfileForm />} />
                    <Route path="/posts" element={<PostList />} />
                    <Route path="/projects" element={<ProjectList />} />
                    <Route path="/login" element={<Login />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
