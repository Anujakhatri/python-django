import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import PatientList from "./pages/PatientList";
import RegisterPatient from "./pages/RegisterPatient";

function App() {
    const isAuthenticated = localStorage.getItem("token");


    return (
        <BrowserRouter>
            <div style={{ textAlign: "center" }}>
                <h1>Clinic App</h1>


                <Routes>
                    {/* Login Page */}
                    <Route path="/login" element={<Login />} />


                    {/* Protected Route */}
                    <Route
                        path="/"
                        element={
                            isAuthenticated ? <PatientList /> : <Navigate to="/login" />
                        }
                    />
                    {/* Register Page */}
                    <Route path="/register" element={<RegisterPatient />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}


export default App;
