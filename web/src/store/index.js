import Vue from 'vue';
import Vuex from 'vuex';

import { fetchCsvFiles, getCsvFileStats, postNewCsvFile } from '@/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    csvFiles: [],
    csvFileStats: [],
  },
  mutations: {
    setCsvFiles(state, payload) {
      state.csvFiles = payload.csvFiles;
    },
    setCsvFileStats(state, payload) {
      state.csvFileStats = payload.csvFileStats;
    },
  },
  actions: {
    loadCsvFiles(context) {
      return fetchCsvFiles().then((response) => {
        context.commit('setCsvFiles', { csvFiles: response.data });
      });
    },
    loadCsvFileStats(context, id) {
      return getCsvFileStats(id).then((response) => {
        context.commit('setCsvFileStats', { csvFileStats: response.data });
      });
    },
    postCsvFile(context, file) {
      postNewCsvFile(file).then(() => true);
    },
  },
  modules: {
  },
  getters: {
    getCsvFileById: (state) => (id) => state.csvFiles.find((csvFile) => csvFile.id === id),
  },
});
