import axios from "axios"
const server = `http://localhost:8000`
export const iris = req => axios.post(`${server}/iris/iris`, req)
export const fashion = req => axios.post(`${server}/iris/fashion`, req)