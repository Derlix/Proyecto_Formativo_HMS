import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Función para crear un nuevo usuario
export const createUser = async (fullName, email, userRole, passhash, idHotel, fileImg) => {
  try {
    const formData = new FormData();
    formData.append('nombre_completo', fullName);
    formData.append('email', email);
    formData.append('usuario_rol', userRole);
    formData.append('passhash', passhash);
    formData.append('id_hotel', idHotel);
    if (fileImg) {
      formData.append('file_img', fileImg);
    }

    const response = await api.post('/usuarios/create', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para obtener un usuario por su email
export const getUserByEmail = async (email) => {
  try {
    const response = await api.get(`/usuarios/obtener-usuario-por-email?email=${encodeURIComponent(email)}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; 
    } else {
      throw new Error('Error de red o de servidor'); 
    }
  }
};

// Función para obtener todos los usuarios con paginación
export const getUsersByPage = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/usuarios/usuarios-por-pagina?page=${page}&page_size=${pageSize}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para actualizar un usuario
export const updateUser = async (userId, fullName, email, userRole, userStatus, fileImg) => {
  try {
    const formData = new FormData();
    formData.append('id_usuario', userId);
    if (fullName) formData.append('nombre_completo', fullName);
    if (email) formData.append('email', email);
    if (userRole) formData.append('usuario_rol', userRole);
    if (userStatus !== undefined) formData.append('usuario_estado', userStatus);
    if (fileImg) formData.append('file_img', fileImg);

    const response = await api.put(`/usuarios/update-other-user`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para actualizar el usuario actual
export const updateCurrentUser = async (fullName, email, userRole, userStatus, fileImg = null) => {
  try {
    const formData = new FormData();
    if (fullName) formData.append('nombre_completo', fullName);
    if (email) formData.append('email', email);
    if (userRole) formData.append('usuario_rol', userRole);
    if (userStatus !== undefined) formData.append('usuario_estado', userStatus);
    if (fileImg) {
      formData.append('file_img', fileImg);
    }

    const response = await api.put(`/usuarios/update-self/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para eliminar un usuario
export const deleteUser = async (userId) => {
  try {
    const response = await api.delete(`/usuarios/delete/${userId}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para actualizar la contraseña de un usuario
export const updatePassword = async (currentPassword, newPassword) => {
  try {
    const response = await api.put(`/usuarios/actualizar-password`, {
      current_password: currentPassword,
      new_password: newPassword,
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
