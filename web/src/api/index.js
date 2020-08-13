import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export default function fetchCsvFiles() {
  return axios.get(`${API_URL}/csvfiles`);
}
