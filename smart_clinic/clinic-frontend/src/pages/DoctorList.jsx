import { useEffect, useState } from "react";
import { getDoctors } from "../Services/api";
import { useNavigate } from "react-router-dom";

function DoctorList() {
    const [Doctors, setDoctors] = useState([]);
    const navigate = useNavigate();

    const loadDoctors = () => {
        getDoctors()
            .then((res) => {
                setDoctors(res.data);
            })
            .catch((err) => {
                console.log("Error:", err);
            });
    };

    useEffect(() => {
        loadDoctors();
    }, []);
    //logout button
    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/");
    };
    const handleDoctorClick = (doctor) => {
        // Placeholder for future navigation or modal logic
        console.log(`Clicked on Doctor: ${doctor.username}`);
    };

    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2>Doctor List</h2>
                <button className="btn btn-danger" onClick={handleLogout}>Logout</button>
            </div>
            
            <div className="list-group">
                {Doctors.map((p) => (
                    <button 
                        key={p.id} 
                        onClick={() => handleDoctorClick(p)}
                        className="list-group-item list-group-item-action d-flex justify-content-between align-items-center"
                    >
                        <div>
                            <h5 className="mb-1">{p.username}</h5>
                            <small className="text-muted">{p.specialization}</small>
                        </div>
                        <span className="badge bg-primary rounded-pill">View</span>
                    </button>
                ))}
            </div>
        </div>
    );
}

export default DoctorList;