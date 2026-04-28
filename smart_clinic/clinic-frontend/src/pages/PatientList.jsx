import {useEffect, useState} from 'react';
import {getPatients} from '../services/api';
function PatientList(){
   const [patients, setPatients] = useState([])
   const loadPatients = ()=>{
       getPatients().then((res)=>{
           setPatients(res.data);
           });
       };
   useEffect(()=>{
       loadPatients();
       },[]);
   return (
       <div>
           <h2>Patient List </h2>
           {
               patients.map((p)=>(
                       <div key={p.id}>
                           <p>{p.name} - {p.age}</p>
                         </div>
                    )
               )
           }
           </div>
       );
   }
export default PatientList;