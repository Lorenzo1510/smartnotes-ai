import api from "./axios";

export const login = async (username: string, password: string) => {
  const response = await api.post("/login", {
    username,
    password,
  });
  return response.data.access_token;
};

export const register = async (username: string, password: string) => {
  const response = await api.post("/register", {
    username,
    password,
  });
  return response.data;
};
