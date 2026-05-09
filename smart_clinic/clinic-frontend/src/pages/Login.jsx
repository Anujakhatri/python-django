import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login({ role }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("/api/token/", {
        username,
        password,
      });

      //  store token
      localStorage.setItem("token", res.data.access);

      const profileRes = await axios.get("/api/profile/", {
        headers: { Authorization: `Bearer ${res.data.access}` },
      });
      const userRole = profileRes.data.role;
      const isSuperuser = profileRes.data.is_superuser;

      if (isSuperuser) {
        navigate("/admin");
        return;
      }

      if (role && userRole !== role) {
        alert(`Error: You are trying to log in as a ${role}, but you are registered as a ${userRole}.`);
        localStorage.removeItem("token");
        return;
      }

      if (userRole === "doctor") {
        navigate("/doctor-dashboard");
      } else if (userRole === "patient") {
        navigate("/patient-dashboard");
      } else {
        navigate("/");
      }

    } catch (err) {
      alert("Invalid credentials or server error");
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>{role ? `${role.charAt(0).toUpperCase() + role.slice(1)} Login` : "Login"}</h2>

      <input
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button type="submit">Login</button>
    </form>
  );
}

export default Login;