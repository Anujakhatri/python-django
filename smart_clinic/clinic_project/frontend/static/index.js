const token = localStorage.getItem("token");

// Fetch Doctors
fetch("/doctors/", {
    method: "GET",
    headers: {
        "Authorization": token ? "Bearer " + token : ""
    }
})
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('doctors_list');
        list.innerHTML = ""; // Clear existing list
        if (Array.isArray(data)) {
            data.forEach(doctor => {
                const li = document.createElement('li');
                li.innerText = doctor.name;
                list.appendChild(li);
            });
        }
    }).catch(error => console.error("error is :", error));

//fetch patients
fetch("/patients/", {
    headers: {
        "Authorization": token ? "Bearer " + token : ""
    }
})
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('patient_list');
        list.innerHTML = "";
        if (Array.isArray(data)) {
            data.forEach(patient => {
                const li = document.createElement('li');
                li.innerText = patient.name;
                list.appendChild(li);
            });
        }
    }).catch(error => console.error("error is :", error))

//fetch appointments
fetch("/appointments/", {
    headers: {
        "Authorization": token ? "Bearer " + token : ""
    }
})
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('appointment_list');
        list.innerHTML = "";
        if (Array.isArray(data)) {
            data.forEach(appointment => {
                const li = document.createElement('li');
                li.innerText = `Patient ${appointment.patient.name} visiting Doctor ${appointment.doctor.name} on ${new Date(appointment.date).toLocaleDateString()} (${appointment.status})`;
                list.appendChild(li);
            });
        }
    }).catch(error => console.error("error is :", error))
