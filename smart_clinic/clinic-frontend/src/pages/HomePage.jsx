import { useState } from "react";
// import axios from "axios";
import { Link } from "react-router-dom";


function HomePage() {
    return (<div>
        <h2>Home Page</h2>
        <ul>

            <li><Link to="/patient-login">Patient Login</Link></li>
            <li><Link to="/doctor-login">Doctor Login</Link></li>
            <li><Link to="/admin-login">Admin Login</Link></li>
            <li><Link to="/register">Patient Registration </Link></li>
            <li><Link to="/register_doctor">Doctor Registration </Link></li>
        </ul>
    </div>
    );

}

export default HomePage;