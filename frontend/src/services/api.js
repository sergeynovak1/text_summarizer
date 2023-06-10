import {API_URL} from "./consts";
import axios from "axios";
const instance = axios.create({
    baseURL: API_URL,
});


export async function getSummurytext(num, text) {
    const response = await instance.post(`${num}`, {text});
    return response.data;
}

export async function getText(link) {
    const response = await instance.post(`/get_link`, {link});
    return response.data;
}