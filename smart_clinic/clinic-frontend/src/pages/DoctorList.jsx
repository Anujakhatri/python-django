import {useEffect, useState} from "react";
import {getDoctors} from "../services/api";
import {useNavigate} from "react-router-dom";

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
        navigate("/login");
    };
    return (
        <div>
            <h2>Doctor List</h2>
            <button onClick={handleLogout}>Logout</button>
            {Doctors.map((p) => (
                <div key={p.id}>
                    <p>
                        {p.username} - {p.specialization}
                    </p>
                </div>
            ))}
        </div>
    );
}

export default DoctorList;