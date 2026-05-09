import React, { useState, useEffect } from "react";
import { getAppointments, getProfile } from "../Services/api";

function DoctorDashboard() {
    const [appointments, setAppointments] = useState([]);
    const [profile, setProfile] = useState(null);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const [profileRes, apptsRes] = await Promise.all([
                getProfile(),
                getAppointments()
            ]);
            setProfile(profileRes.data);

            // Filter appointments for this doctor only
            const doctorAppts = apptsRes.data.filter(
                (a) => a.doctor === profileRes.data.username
            );
            setAppointments(doctorAppts);
        } catch (error) {
            console.error("Error fetching data", error);
        }
    };

    return (
        <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto", textAlign: "left" }}>
            <h2>Doctor Dashboard</h2>

            <div style={{ marginTop: "30px" }}>
                <h3 className="mb-4">My Appointments</h3>
                {appointments.length === 0 ? (
                    <p className="text-muted">You have no appointments booked yet.</p>
                ) : (
                    <div className="table-responsive">
                        <table className="table">
                            <thead>
                                <tr>
                                    <th scope="col">Serial</th>
                                    <th scope="col">Patient</th>
                                    <th scope="col">Date</th>
                                    <th scope="col">Age</th>
                                    <th scope="col">Time</th>
                                </tr>
                            </thead>
                            <tbody>
                                {appointments.map((appt, index) => (
                                    <tr key={appt.id}>
                                        <th scope="row">{index + 1}</th>
                                        <td>{appt.patient}</td>
                                        <td>{appt.date}</td>
                                        <td>{appt.patient_age || 'N/A'}</td>
                                        <td>{appt.time}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </div>
    );
}

export default DoctorDashboard;