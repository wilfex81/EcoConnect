// src/components/ProjectList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../api';
import './ProjectList.css' ; 

function ProjectList() {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}projects/`);
                setProjects(response.data);
            } catch (error) {
                console.error('Error fetching projects:', error);
            }
        };

        fetchProjects();
    }, []);

    return (
        <div className="project-list-container">
            <h2>Projects</h2>
            <ul className="project-items">
                {projects.map(project => (
                    <li key={project.id} className="project-item">
                        <h3>{project.name}</h3>
                        <p><strong>Description:</strong> {project.description}</p>
                        <p><strong>Start Date:</strong> {project.start_date}</p>
                        <p><strong>End Date:</strong> {project.end_date}</p>
                        <p><strong>Creator:</strong> {project.creator.username}</p>
                        <p><strong>Participants:</strong> {project.participants.map(participant => participant.username).join(', ')}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ProjectList;
