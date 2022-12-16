import axios from "axios"
const server = `http://localhost:8000`
export const getiris = req => axios.get(`${server}/iris/iris?req=${req}`)
export const postiris = req => axios.post(`${server}/iris/iris`, req)
export const getFashion = id => axios.get(`${server}/iris/fashion?id=${id}`)
export const postFashion = req => axios.post(`${server}/iris/fashion`, req)