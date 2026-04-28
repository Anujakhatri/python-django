import {useState } from 'react';
import axios from 'axios';
function Login(){
   const [username, setUsername] = useState('');


   const [password, setPassword] = useState('');
   const handleLogin = async(e) => {
       e.preventDefault();
       const res = await axios.post('/api/token/',{
           username,password
           });
       //store token
       localStorage.setItem('token', res.data.access);
       alert('Login done');
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