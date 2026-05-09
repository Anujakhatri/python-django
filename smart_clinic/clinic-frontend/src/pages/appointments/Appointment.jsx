import React, { useState, useEffect } from "react";
import { getDoctors, getAppointments, addAppointment, getProfile } from "../../Services/api";

function Appointment() {
    const [doctors, setDoctors] = useState([]);
    const [appointments, setAppointments] = useState([]);
    const [profile, setProfile] = useState(null);
    const [formData, setFormData] = useState({
        doctor: "",
        date: "",
        time: "",
        notes: ""
    });
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const [profileRes, docsRes, apptsRes] = await Promise.all([
                getProfile(),
                getDoctors(),
                getAppointments()
            ]);
            setProfile(profileRes.data);
            setDoctors(docsRes.data);

            // Filter appointments for this user only
            const userAppts = apptsRes.data.filter(
                (a) => a.patient === profileRes.data.username
            );
            setAppointments(userAppts);
        } catch (error) {
            console.error("Error fetching data", error);
        }
    };

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage("");

        if (!profile || !profile.patient_id) {
            setMessage("Error: Could not determine your patient profile. Are you sure you are registered as a patient?");
            return;
        }

        try {
            await addAppointment({
                ...formData,
                patient: profile.patient_id
            });
            setMessage("Appointment booked successfully!");
            setFormData({ doctor: "", date: "", time: "", notes: "" });
            fetchData(); // refresh appointments
        } catch (error) {
            setMessage(error.response?.data?.error || "Error booking appointment.");
        }
    };

    return (
        <div className="container mt-4">
            <div className="mb-5 p-4 border rounded shadow-sm bg-white">
                <h3 className="mb-4">Book an Appointment</h3>
                {message && <p style={{ color: message.includes("Error") ? "red" : "green" }}>{message}</p>}

                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="doctorSelect" className="form-label">Select Doctor:</label>
                        <select
                            id="doctorSelect"
                            name="doctor"
                            className="form-select"
                            value={formData.doctor}
                            onChange={handleChange}
                            required
                        >
                            <option value="">-- Choose a doctor --</option>
                            {doctors.map(doc => (
                                <option key={doc.id} value={doc.id}>
                                    Dr. {doc.username} - {doc.specialization}
                                </option>
                            ))}
                        </select>
                    </div>

                    <div className="mb-3">
                        <label htmlFor="appointmentDate" className="form-label">Date:</label>
                        <input
                            type="date"
                            id="appointmentDate"
                            name="date"
                            className="form-control"
                            value={formData.date}
                            onChange={handleChange}
                            required
                        />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="appointmentTime" className="form-label">Time:</label>
                        <input
                            type="time"
                            id="appointmentTime"
                            name="time"
                            className="form-control"
                            value={formData.time}
                            onChange={handleChange}
                            required
                        />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="appointmentNotes" className="form-label">Notes (Optional):</label>
                        <textarea
                            id="appointmentNotes"
                            name="notes"
                            className="form-control"
                            value={formData.notes}
                            onChange={handleChange}
                            rows="3"
                        ></textarea>
                    </div>

                    <button type="submit" className="btn btn-primary">
                        Book Appointment
                    </button>
                </form>
            </div>

            <div>
                <h3 className="mb-4">My Appointments</h3>
                {appointments.length === 0 ? (
                    <p className="text-muted">You have no appointments.</p>
                ) : (
                    <div className="table-responsive">
                        <table className="table">
                            <thead>
                                <tr>
                                    <th scope="col">Serial</th>
                                    <th scope="col">Doctor</th>
                                    <th scope="col">Date</th>
                                    <th scope="col">Time</th>
                                </tr>
                            </thead>
                            <tbody>
                                {appointments.map((appt, index) => (
                                    <tr key={appt.id}>
                                        <th scope="row">{index + 1}</th>
                                        <td>Dr. {appt.doctor}</td>
                                        <td>{appt.date}</td>
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

export default Appointment;