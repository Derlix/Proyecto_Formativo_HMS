
import api from './api'; 

// Función para manejar el inicio de sesión
export const login = async (username, password) => {
  try {
    // Enviar solicitud de inicio de sesión
    const response = await api.post('/login/token', new URLSearchParams({
      grant_type: '',
      username,
      password,
      scope: '',
      client_id: '',
      client_secret: ''
    }), {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
    
    // Retornar la respuesta de la API
    return response;
  } catch (error) {
    // Manejar errores de la solicitud
    if (error.response) {
      throw error; // Lanza el error para que lo maneje el store
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};

// Función para manejar el registro de un nuevo usuario
export const register = async (fullName, email, userRole, password) => {
  try {
    // Enviar solicitud de registro
    const response = await api.post('/access/register', {
      full_name: fullName,
      mail: email,
      user_role: userRole,
      passhash: password
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    
    // Retornar la respuesta de la API
    return response;
  } catch (error) {
    // Manejar errores de la solicitud
    if (error.response) {
      throw error; // Lanza el error para que lo maneje el store
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};

// Función para enviar código de reseteo de contraseña
export const requestResetCode = async (email) => {
  try {
    const response = await api.post(`login/request-reset-code?email=${encodeURIComponent(email)}`, '', {
      headers: {
        'accept': 'application/json'
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para verificar código y actualizar contraseña
export const changePassword = async (email, newPassword, code) => {
  try {
    const response = await api.post('/login/change-password', {
      email,
      new_password: newPassword,
      code
    }, {
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};