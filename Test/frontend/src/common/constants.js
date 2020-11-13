import axios from 'axios'

export const cathAxios = axios.create({
    baseURL: 'http://localhost:5060'
})