 "use client"
import React, { useEffect, useState } from 'react'


// const token=localStorage.getItem("access")
const page =  () => {
    const [data, setData] = useState<any>(null)

    useEffect(()=>{
    // const token=localStorage.getItem("access")
    const fetchDashboard=async()=>{
        try {
            const token=localStorage.getItem("access")
            if (!token) {
                setData({ error: 'No access token' })
                return
            }
            const res=await fetch("http://127.0.0.1:8000/accounts/checkdashboard/",
                {
                    method:"GET",

                    headers:{
                        Authorization:`Bearer ${token}`,
                        "Content-Type":"application/json",
                }}
            )
            const result= await res.json();
            if(!res.ok){
                console.error(result)
                setData(result)
            }else{
                console.log("Dashboard data:", result)
                setData(result)
            }
        } catch (err) {
            console.error(err)
            setData({ error: err instanceof Error ? err.message : String(err) })
        }
    }
        fetchDashboard();
    
},[])

    // const res=await fetch("http://127.0.0.1:8000/accounts/checkdashboard/",
    //     {
    //         method:"GET",
    //         headers:{
    //             Authorization:`Bearer ${localStorage.getItem("token")}`,
    //             "Content-Type":"application/json",
    //     }}
    // )
    // const data=await res.json();
  return (
    <>
        <div>{JSON.stringify(data)}</div>
    </>
  )
}

export default page