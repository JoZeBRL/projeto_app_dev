import axios, { InternalAxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';

const apiClient = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    const token = localStorage.getItem('token');
    if (token && config.headers) {
      // Uso do método .set() para compatibilidade segura de tipagem no Axios
      config.headers.set('Authorization', `Bearer ${token}`);
    }
    return config;
  },
  (error: AxiosError) => Promise.reject(error)
);

apiClient.interceptors.response.use(
  (response: AxiosResponse) => response,
  (error: AxiosError) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      // Redirecionamento limpo para expurgar sessão inválida
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default apiClient;
