// src/components/PostForm.js

import React, { useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../api';

function PostForm() {
    const [formData, setFormData] = useState({
        content: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Assuming you have user information available, you can include it in the form data
            const postData = {
                user: 'user_id_or_username', // Replace with actual user ID or username
                content: formData.content
            };

            const response = await axios.post(`${API_BASE_URL}posts/`, postData);
            console.log('Post created successfully:', response.data);
            // You may want to navigate to a different page or show a success message to the user
        } catch (error) {
            console.error('Error creating post:', error);
            // You may want to display an error message to the user
        }
    };

    return (
        <div>
            <h2>Create Post</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Content:</label>
                    <textarea
                        name="content"
                        value={formData.content}
                        onChange={handleChange}
                    ></textarea>
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default PostForm;
