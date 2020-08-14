import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export function fetchCsvFiles() {
  return axios.get(`${API_URL}/csvfiles`);
}

export function getCsvFileStats(id) {
  return axios.get(`${API_URL}/csvfiles/stats/${id}`);
}

export function postNewCsvFile(file) {
  console.log(file);
  return axios.post(`${API_URL}/csvfiles`, {
    name: file.name,
    raw_content: file.content,
  });
}
