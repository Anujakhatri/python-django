import { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import PatientList from './pages/PatientList'
function App(){
   const [reload, setReload] = useState(false);
   const refresh = () => {
       setReload(!reload);
       };
   return(


           <div style={{textAlign: 'center'}}>
               <h1> Clinic APP </h1>
               <BrowserRouter>
                   <Routes>
                       <Route path= "/login" element = {<Login/>}/>
                       </Routes>
                   </BrowserRouter>
               <PatientList key={reload}/>
           </div>
       );
   }
export default App;
