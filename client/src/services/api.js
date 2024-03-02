// src/services/api.js
import axios from 'axios';

export const API_BASE_URL = 'http://localhost:8000/api/v1/';

export const getUsers = async () => {
    const response = await axios.get(`${API_BASE_URL}userprofiles/`);
    console.log(response.data)
    return response.data;
};

export const createUser = async (userData) => {
    const response = await axios.post(`${API_BASE_URL}users/`, userData);
    return response.data;
};

// Similarly, define functions for other resources (posts, projects, events, etc.)