import axios from 'axios'


const API = axios.create({
   baseURL: '/api'
});

//add api tokens for jwt
API.interceptors.request.use((req) => {
   const token = localStorage.getItem('token');
   if (token && !req.url.includes('register') && !req.url.includes('token')) {
      req.headers.Authorization = `Bearer ${token}`;
   }
   return req; //very imp
});
export default API;

//api endpoints patient
export const getPatients = () => API.get('clinic/patient/');
export const addPatient = (data) => API.post('clinic/patient/', data);
export const registerPatient = (data) => API.post('register/', data);