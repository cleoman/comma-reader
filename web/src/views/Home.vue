<template>
  <div>
    <v-card raised>
      <v-card-title>Upload</v-card-title>
      <v-card-text>
        <v-file-input accept=".csv" label="Upload .csv file" v-model="inputFile"></v-file-input>
        <v-btn right @click="uploadCsv">Upload File</v-btn>
      </v-card-text>
    </v-card>
    <v-card>
      <v-card-title>List of uploaded files</v-card-title>
      <v-card-text>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th>Name</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="row in csvFiles" :key="row.id">
                <td>{{row.name}}</td>
                <td>
                  <router-link :to="{ path: '/csvfile/'+ row.id}" >View</router-link>
                  |
                  <a href="#">Download (nonfunctional)</a>
                  |
                  <router-link :to="{ path: 'csvfile/stats/' + row.id }" >Stats</router-link>
                  |
                  <a href="#">Delete (nonfunctional)</a>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Home',
  components: {
  },
  computed: mapState({
    csvFiles: (state) => state.csvFiles,
  }),
  methods: {
    uploadCsv() {
      const reader = new FileReader();
      const csvContent = this.inputFile;
      const fileName = csvContent.name;
      const store = this.$store;

      reader.onload = (e) => {
        const postObject = { name: fileName, content: e.target.result };
        store.dispatch('postCsvFile', postObject);
        // not sure if this will work to display updated table
        store.dispatch('loadCsvFiles');
      };

      reader.readAsText(csvContent);
    },
  },
  data() {
    return {
      inputFile: null,
    };
  },
  beforeMount() {
    this.$store.dispatch('loadCsvFiles');
  },
};
</script>
