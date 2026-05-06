import { useState } from "react";
import { registerPatient } from "../Services/api";
import { useNavigate } from 'react-router-dom';
import axios from "axios";

function RegisterPatient() {
    const [username, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const [age, setAge] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        setError("");
        //registration of patient
        axios.post("/api/register/", { username, password, role: "patient", age: age || null })
            //auto login
            .then(() => {
                return axios.post("/api/token/", { username, password });
            })
            .then((res) => {
                localStorage.setItem("token", res.data.access);
                navigate("/patient-list");
            })
            .catch((err) => {
                console.log(err.response?.data);
                if (err.response?.data?.username) {
                    setError(err.response.data.username[0]);
                } else if (err.response?.data?.password) {
                    setError(err.response.data.password[0]);
                } else {
                    setError("An error occurred during registration.");
                }
            });


    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Register Patient</h2>
            {error && <p style={{ color: "red" }}>{error}</p>}

            <input
                placeholder="Username"
                value={username}
                onChange={(e) => setUserName(e.target.value)}
            />

            <input
                placeholder="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <input
                placeholder="Age"
                value={age}
                onChange={(e) => setAge(e.target.value)}
            />

            <button type="submit">Register</button>
        </form>
    );
}

export default RegisterPatient;