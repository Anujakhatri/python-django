import React from "react";
import Appointment from "./appointments/Appointment";

function PatientDashboard() {
    return (
        <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto", textAlign: "left" }}>
            <h2>Patient Dashboard</h2>
            <Appointment patient={true} />
        </div>
    );
}

export default PatientDashboard;