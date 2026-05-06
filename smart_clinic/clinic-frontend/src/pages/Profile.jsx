import React, { useState, useEffect } from "react";
import API from "../Services/api"

function Profile() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        API.get("profile/")
            .then((res) => setUser(res.data))
            .catch((err) => console.log("Error loading profile"));
    }, []);

    if (!user) return <div>Loading...</div>;

    return (
        <div>
            <h2>Profile</h2>
            <p>Username: {user.username}</p>
            <p>Email: {user.email}</p>
            <p>Role: {user.role}</p>

            {/* doctor fields */}
            {user.specialization && <p>Specialization: {user.specialization}</p>}
            {user.experience && <p>Experience: {user.experience}</p>}

            {/* patient fields */}
            {user.age && <p>Age: {user.age}</p>}
        </div>
    );
}

export default Profile;