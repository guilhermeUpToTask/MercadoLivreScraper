import axios from "axios";

const BACK_END_DEV_URL = 'http://127.0.0.1:8000/'

const axiosInstance = axios.create({
    baseURL: BACK_END_DEV_URL,
});


export default axiosInstance;