// src/components/PostList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../api';
import PostForm from './PostForm';
import './PostList.css';

function PostList() {
    const [posts, setPosts] = useState([]);
    const [showForm, setShowForm] = useState(false); // State to control the visibility of the form

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}posts/`);
                setPosts(response.data);
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        };

        fetchPosts();
    }, []);

    const handleToggleForm = () => {
        setShowForm(!showForm); // Toggle the visibility of the form
    };

    return (
        <div className="post-list-container">
            <h2>Posts</h2>
            <button className="create-post-btn" onClick={handleToggleForm}>Create Post</button>
            {showForm && <PostForm />} {/* Render the form only if showForm is true */}
            <ul className="post-items">
                {posts.map(post => (
                    <li key={post.id} className="post-item">
                        <p><strong>User:</strong> {post.user.username}</p>
                        <p><strong>Content:</strong> {post.content}</p>
                        <p><strong>Created At:</strong> {post.created_at}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default PostList;
