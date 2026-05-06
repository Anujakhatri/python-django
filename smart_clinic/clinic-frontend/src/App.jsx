import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import Login from "./pages/Login";
import PatientList from "./pages/PatientList";
import DoctorList from "./pages/DoctorList";
import RegisterPatient from "./pages/RegisterPatient";
import RegisterDoctor from "./pages/RegisterDoctor";
import HomePage from "./pages/HomePage";

function ProtectedRoute({ children }) {
    const isAuthenticated = localStorage.getItem("token");
    return isAuthenticated ? children : <Navigate to="/login" />;
}

function App() {
    return (
        <BrowserRouter>
            <div style={{textAlign: "center"}}>
                <h1>Clinic App</h1>

                <Routes>
                    {/*  Pages */}
                    <Route path="/register" element={<RegisterPatient/>}/>
                    <Route path="/register_doctor" element={<RegisterDoctor/>}/>
                    <Route path="/login" element={<Login/>}/>
                    <Route path="/home-page" element={<HomePage/>}/>
                    
                    {/* Protected Routes */}
                    <Route
                        path="/patient-list"
                        element={
                            <ProtectedRoute><PatientList/></ProtectedRoute>
                        }
                    />
                    <Route
                        path="/doctor-list"
                        element={
                            <ProtectedRoute><DoctorList/></ProtectedRoute>
                        }
                    />

                    {/* Default Route */}
                    <Route
                        path="/"
                        element={
                            <Navigate to="/home-page"/>
                        }
                    />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;