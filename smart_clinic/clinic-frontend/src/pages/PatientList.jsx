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
        navigate("/login");
    };
    return (
        <div>
            <h2>Patient List</h2>
            <button onClick={handleLogout}>Logout</button>
            {patients.map((p) => (
                <div key={p.id}>
                    <p>
                        {p.username} - {p.age}
                    </p>
                </div>
            ))}
        </div>
    );
}

export default PatientList;