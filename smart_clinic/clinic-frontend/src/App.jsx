import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import Login from "./pages/Login";
import PatientList from "./pages/PatientList";
import DoctorList from "./pages/DoctorList";
import RegisterPatient from "./pages/RegisterPatient";
import RegisterDoctor from "./pages/RegisterDoctor";
import HomePage from "./pages/HomePage";

function App() {
    const isAuthenticated = localStorage.getItem("token");

    return (
        <BrowserRouter>
            <div style={{textAlign: "center"}}>
                <h1>Clinic App</h1>

                <Routes>
                    {/*  Pages */}
                    <Route path="/register" element={<RegisterPatient/>}/>
                    <Route path="/register_doctor" element={<RegisterDoctor/>}/>
                    <Route path="/login" element={<Login/>}/>
                    <Route path="/patient-list" element={<PatientList/>}/>
                    <Route path="/doctor-list" element={<DoctorList/>}/>
                    <Route path="/home-page" element={<HomePage/>}/>
                    {/* Protected Route */}
                    <Route
                        path="/patient-list"
                        element={
                            isAuthenticated ? <PatientList/> : <Navigate to="/login"/>
                        }
                    />

                    <Route
                        path="/login"
                        element={
                            <Navigate to="/login"/>
                        }
                    />
                    <Route
                        path="/"
                        element={
                            <Navigate to="/home-page"/>
                        }
                    />
                    <Route
                        path="register_doctor"
                        element={
                            <Navigate to="/register_doctor"/>
                        }
                    />
                    <Route
                        path="doctor-list"
                        element={
                            <Navigate to="/doctor-list"/>
                        }
                    />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;