import axios from "axios";

const API = axios.create({
  baseURL: "/api/",
});


// Attach JWT token
API.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");

  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }

  return req; // VERY IMPORTANT
});

//refresh the token
API.interceptors.response.use(
  (response) => response, async (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem("token");
      window.location.href = "/";
    }
    return Promise.reject(error);
  }
);

export default API;

// API endpoints
export const getPatients = () => API.get("clinic/patients/");
export const addPatient = (data) => API.post("clinic/patients/", data);
export const getDoctors = () => API.get("clinic/doctors/");
// add for registration
export const registerPatient = (data) =>
  API.post("register/", data);

export const registerDoctor = (data) =>
  API.post("clinic/doctors/", data);

export const getAppointments = () => API.get("clinic/appointments/");
export const addAppointment = (data) => API.post("clinic/appointments/", data);
export const getProfile = () => API.get("profile/");
