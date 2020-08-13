import Vue from 'vue';
import Vuex from 'vuex';

import { fetchCsvFiles } from '@/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    csvFiles: [],
  },
  mutations: {
    setCsvFiles(state, payload) {
      state.csvFiles = payload.csvFiles;
    },
  },
  actions: {
    loadCsvFiles(context) {
      return fetchCsvFiles().then((response) => {
        context.commit('setCsvFiles', { csvFiles: response.data });
      });
    },
  },
  modules: {
  },
  getters: {
    getCsvFileById: (state) => (id) => state.csvFiles.find((csvFile) => csvFile.id === id),
  },
});
