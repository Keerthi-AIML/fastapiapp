import axios from "axios";
import type {Job}  from "../types/job" ;                                                                                                                                                                                   ";

const API_BASE_URL = "http://localhost:8000";

export async function getJobs(): Promise<Job[]> {
    const response = await axios.get(`${API_BASE_URL}/job`);
    return response.data;
}

export async function getJob(id:number):Promise<Job>{
    const response=await axios.get(`${API_BASE_URL}/job/${id}`);
    return response.data;
}

export async function CreateJob(company:Job):Promise<Job>{
    const response=await axios.post(`${API_BASE_URL}/job`,company);
    return response.data;
}
export async function UpdateJob(id:number,company:Job):Promise<Job>{
    const response=await axios.put(`${API_BASE_URL}/job/${id}`,company);
    return response.data;
}
export async function DeleteJob(id:number,company:Job):Promise<void>{
    const response=await axios.put(`${API_BASE_URL}/job/${id}`,company);
    return response.data;
}
