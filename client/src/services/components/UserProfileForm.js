// UserProfileForm.js
import axios from 'axios';
import { API_BASE_URL } from '../api';
import React, { useState } from 'react';

function UserProfileForm() {
    const [formData, setFormData] = useState({
        bio: '',
        location: '',
        profilePicture: null
    });

    const handleChange = (e) => {
        const { name, value, files } = e.target;
        setFormData({
            ...formData,
            [name]: name === 'profilePicture' ? files[0] : value
        });
    };



    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const formDataToSend = new FormData();
            formDataToSend.append('bio', formData.bio);
            formDataToSend.append('location', formData.location);
            formDataToSend.append('profilePicture', formData.profilePicture);

            const response = await axios.post(`${API_BASE_URL}userprofiles/`, formDataToSend, {
                headers: {
                    'Content-Type': 'multipart/form-data' // Ensure correct content type for file upload
                }
            });

            console.log('Data successfully submitted:', response.data);
            // You may also want to navigate to a different page or show a success message to the user
        } catch (error) {
            // Handle error
            console.error('Error submitting data:', error);
            // You may want to display an error message to the user
        }
    };

    return (
        <div>
            <h2>Create User Profile</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Bio:</label>
                    <textarea
                        name="bio"
                        value={formData.bio}
                        onChange={handleChange}
                    ></textarea>
                </div>
                <div>
                    <label>Location:</label>
                    <input
                        type="text"
                        name="location"
                        value={formData.location}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Profile Picture:</label>
                    <input
                        type="file"
                        name="profilePicture"
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default UserProfileForm;
