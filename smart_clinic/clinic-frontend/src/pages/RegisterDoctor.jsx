import {useState} from "react";
import {useNavigate} from "react-router-dom";
import axios from "axios";

function RegisterDoctor() {
    const [username, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const [specialization, setSpecialization] = useState("");
    const [experience, setExperience] = useState("");

    const navigate = useNavigate(); //  IMPORTANT

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            //  1. REGISTER DOCTOR
            await axios.post("/api/register/", {
                username,
                password,
                role: "doctor",
                specialization,
                experience: Number(experience), //  ensure number
            });

            //  2. AUTO LOGIN
            const res = await axios.post("/api/token/", {
                username,
                password,
            });

            //  3. SAVE TOKEN
            localStorage.setItem("token", res.data.access);

            //  4. REDIRECT
            navigate("/doctor-list");

        } catch (err) {
            console.log("ERROR:", err.response?.data);
            alert("Registration failed");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Register Doctor</h2>

            <input
                placeholder="Username"
                value={username}
                onChange={(e) => setUserName(e.target.value)}
            />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <input
                placeholder="Specialization"
                value={specialization}
                onChange={(e) => setSpecialization(e.target.value)}
            />

            <input
                placeholder="Experience"
                value={experience}
                onChange={(e) => setExperience(e.target.value)}
            />

            <button type="submit">Register</button>
        </form>
    );
}

export default RegisterDoctor;