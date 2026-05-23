import axios from 'axios'

// Get API URL from environment variable or use default
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Fields API
export const fieldsAPI = {
  getAll: () => apiClient.get('/v1/fields'),
  getById: (id) => apiClient.get(`/v1/fields/${id}`),
  create: (data) => apiClient.post('/v1/fields', data),
  update: (id, data) => apiClient.put(`/v1/fields/${id}`, data),
  delete: (id) => apiClient.delete(`/v1/fields/${id}`)
}

// Irrigation API
export const irrigationAPI = {
  getSchedule: (fieldId) => apiClient.get(`/v1/irrigation/${fieldId}/schedule`),
  getTips: (fieldId) => apiClient.get(`/v1/irrigation/${fieldId}/tips`),
  control: (fieldId, action) => apiClient.post(`/v1/irrigation/${fieldId}/${action}`)
}

// Weather API
export const weatherAPI = {
  getForecast: (latitude, longitude) => 
    apiClient.get(`/v1/weather/forecast`, { params: { latitude, longitude } }),
  getCurrent: (latitude, longitude) => 
    apiClient.get(`/v1/weather/current`, { params: { latitude, longitude } })
}

// Satellite API
export const satelliteAPI = {
  getImagery: (fieldId) => apiClient.get(`/v1/satellite/${fieldId}/imagery`),
  getNDVI: (fieldId) => apiClient.get(`/v1/satellite/${fieldId}/ndvi`)
}

// Analytics API
export const analyticsAPI = {
  getDailyAnalysis: (fieldId) => apiClient.get(`/v1/analytics/${fieldId}/daily`),
  getWaterSavings: (fieldId) => apiClient.get(`/v1/analytics/${fieldId}/water-savings`)
}

export default apiClient
