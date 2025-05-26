import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Assicurati che sia il tuo backend
  withCredentials: false,
});

export default api;
