import axios from 'axios'


const API = axios.create ({
   baseURL : '/api'
});


//api endpoints patient
export const getPatients = ()=> API.get('clinic/patient/');
export const addPatient = (data) =>API.post('clinic/patient/',data);

//add api tokens for jwt
API.interceptors.request.use((req)=>{
   const token = localStorage.getItem('token');
   if(token){
       req.headers.Authorization = 'Bearer ${token}';
   }
});
export default API;