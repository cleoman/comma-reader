<template>
  <div>
    {{matchingFile.name}}
    <v-data-table :headers="headers" :items="csvFileContent"></v-data-table>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'CsvFile',
  components: {
  },
  computed: {
    ...mapGetters({
      getCsvFileById: 'getCsvFileById',
    }),
    matchingFile() {
      return this.getCsvFileById(parseInt(this.$route.params.id, 10));
    },
    csvFileContent() {
      return JSON.parse(this.matchingFile.parsed_content);
    },
    headers() {
      if (this.matchingFile.parsed_content === null) {
        return ['No valid headers detected'];
      }
      const csvContent = JSON.parse(this.matchingFile.parsed_content);
      const headers = Object.keys(csvContent[0]);
      return headers.map((item) => ({ text: item, value: item }));
    },
  },
  beforeMount() {
    this.$store.dispatch('loadCsvFiles');
  },
};
</script>
