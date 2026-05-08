import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
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

      // fetch profile to get role
      const profileRes = await axios.get("/api/profile/", {
        headers: { Authorization: `Bearer ${res.data.access}` },
      });
      const role = profileRes.data.role;
      const isSuperuser = profileRes.data.is_superuser;

      if (role === "admin" || isSuperuser) {
        navigate("/admin-dashboard");
      } else if (role === "doctor") {
        navigate("/doctor-list");
      } else if (role === "patient") {
        navigate("/patient-list");
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
      <h2>Login</h2>

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