import { useEffect, useState } from "react";
import { getPatients } from "../Services/api";
import { useNavigate } from "react-router-dom";


function PatientList() {
    const [patients, setPatients] = useState([]);
    const navigate = useNavigate();

    const loadPatients = () => {
        getPatients()
            .then((res) => {
                setPatients(res.data);
            })
            .catch((err) => {
                console.log("Error:", err);
            });
    };

    useEffect(() => {
        loadPatients();
    }, []);

    //logout button
    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/");
    };
    const handlePatientClick = (patient) => {
        // Placeholder for future navigation or modal logic
        console.log(`Clicked on Patient: ${patient.username}`);
    };

    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2>Patient List</h2>
                <button className="btn btn-danger" onClick={handleLogout}>Logout</button>
            </div>

            <div className="list-group">
                {patients.map((p) => (
                    <button
                        key={p.id}
                        onClick={() => handlePatientClick(p)}
                        className="list-group-item list-group-item-action d-flex justify-content-between align-items-center"
                    >
                        <div>
                            <h5 className="mb-1">{p.username}</h5>
                            <small className="text-muted">Age: {p.age}</small>
                        </div>
                        <span className="badge bg-primary rounded-pill">View</span>
                    </button>
                ))}
            </div>
        </div>
    );
}

export default PatientList;