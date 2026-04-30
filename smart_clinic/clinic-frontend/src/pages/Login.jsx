import {useState } from 'react';
import axios from 'axios';
import {useNavigate } from 'react-router-dom';

function Login(){
   const [username, setUsername] = useState('');
   const [password, setPassword] = useState('');
   const navigate = useNavigate();

   const handleLogin = async(e) => {
       e.preventDefault();
       try {
           const res = await axios.post('/api/token/', {
               username,
               password,
           });

           //store token
           localStorage.setItem('token', res.data.access);

           //redirect to home
           navigate('/');
       }catch(err){
           alert("Invalid Credentials");
       }
   };
   return(
       <form onSubmit = {handleLogin}>
           <h2> login form </h2>
           <input placeholder ="add username without space " onChange = {(e)=> setUsername(e.target.value)}/>
           <input placeholder ="add password  " onChange = {(e)=> setPassword(e.target.value)}/>
           <button type = "submit">Login</button>
       </form>
       );
   }
export default Login;