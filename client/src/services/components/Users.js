// src/components/Users.js
import React, { useEffect, useState } from 'react';
import { getUsers, createUser } from '../api';

function Users() {
    const [users, setUsers] = useState([]);
    const [newUser, setNewUser] = useState({});

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        const usersData = await getUsers();
        setUsers(usersData);
    };

    const handleCreateUser = async () => {
        await createUser(newUser);
        // Refresh the list of users after creating a new user
        fetchUsers();
    };

    return (
        <div>
            <h2>Users</h2>
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.username}</li>
                ))}
            </ul>
            <input
                type="text"
                placeholder="Enter username"
                value={newUser.username || ''}
                onChange={(e) => setNewUser({ ...newUser, username: e.target.value })}
            />
            <button onClick={handleCreateUser}>Add User</button>
        </div>
    );
}

export default Users;
