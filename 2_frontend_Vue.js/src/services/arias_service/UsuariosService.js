import axios from 'axios';

const API_URL = 'https://api-hotel-suqt.onrender.com/usuarios/';

export const getUsersByPage = (page) => {
  return axios.get(`${API_URL}usuarios-por-pagina/?page=${page}`);
};

export const deleteUser = (id_usuario) => {
  return axios.delete(`${API_URL}delete/${id_usuario}`);
};

export const updateUser = (id_usuario, formData) => {
  return axios.put(`${API_URL}update-other-user/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

export const updateCurrentUser = (formData) => {
  return axios.put(`${API_URL}update-user/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};
