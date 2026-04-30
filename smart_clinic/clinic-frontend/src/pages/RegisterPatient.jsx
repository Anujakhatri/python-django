import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerPatient } from "../services/api";

function RegisterPatient() {
    const [username, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();


    const handleSubmit = (e) => {
        e.preventDefault();


        registerPatient({ username, password, role: "patient" })
            .then(() => {
                alert("Patient registered!");
                navigate("/");
            })
            .catch((err) => {
                console.log("response data error:", err.response.data?.status);
                console.log("response data message:", err.response.data?.message);
                alert(JSON.stringify(err.response.data));
            });
    };


    return (
        <form onSubmit={handleSubmit}>
            <h2>Register Patient</h2>


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


            <button type="submit">Register</button>
        </form>
    );
}


export default RegisterPatient;