// src/components/PostList.js
import React, { useState, useEffect } from 'react';
import api from '../api'

function PostList() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await api.get('posts/');
                setPosts(response.data);
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        };

        fetchPosts();
    }, []);

    return (
        <div>
            <h1>Posts</h1>
            <ul>
                {posts.map(post => (
                    <li key={post.id}>{post.content}</li>
                ))}
            </ul>
        </div>
    );
}

export default PostList;
