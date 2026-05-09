import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import PatientList from "./pages/PatientList";
import DoctorList from "./pages/DoctorList";
import RegisterPatient from "./pages/RegisterPatient";
import RegisterDoctor from "./pages/RegisterDoctor";
import AdminDashboard from "./pages/AdminDashboard";
import HomePage from "./pages/HomePage";
import PatientDashboard from "./pages/PatientDashboard";
import DoctorDashboard from "./pages/DoctorDashboard";
import Apointment from "./pages/appointments/Appointment";

function ProtectedRoute({ children }) {
    const isAuthenticated = localStorage.getItem("token");
    return isAuthenticated ? children : <Navigate to="/" />;
}

function App() {
    return (
        <BrowserRouter>
            <div style={{ textAlign: "center" }}>
                <h1>Clinic App</h1>

                <Routes>
                    {/*  Pages */}
                    <Route path="/register" element={<RegisterPatient />} />
                    <Route path="/register_doctor" element={<RegisterDoctor />} />
                    <Route path="/patient-login" element={<Login role="patient" />} />
                    <Route path="/doctor-login" element={<Login role="doctor" />} />
                    <Route path="/admin-login" element={<Login role="admin" />} />
                    <Route path="/" element={<HomePage />} />

                    {/* Protected Routes */}
                    <Route
                        path="/admin"
                        element={
                            <ProtectedRoute><AdminDashboard /></ProtectedRoute>
                        }
                    />
                    <Route
                        path="/patient-list"
                        element={
                            <ProtectedRoute><PatientList /></ProtectedRoute>
                        }
                    />
                    <Route
                        path="/doctor-list"
                        element={
                            <ProtectedRoute><DoctorList /></ProtectedRoute>
                        }
                    />
                    <Route
                        path="/patient-dashboard"
                        element={
                            <ProtectedRoute><PatientDashboard /></ProtectedRoute>
                        }
                    />
                    <Route
                        path="/doctor-dashboard"
                        element={
                            <ProtectedRoute><DoctorDashboard /></ProtectedRoute>
                        }
                    />
                    <Route
                        path="/appointments"
                        element={
                            <ProtectedRoute><Apointment /></ProtectedRoute>
                        }
                    />
                    <Route
                        path="*"
                        element={
                            <Navigate to="/" />
                        }
                    />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;