<template>
  <div>
    {{matchingFile.name}}
    <table>
      <thead>
        <th v-for="header in headers" :key="header">
          {{header}}
        </th>
      </thead>
    </table>
  </div>
</template>

<script>
// import { mapState } from 'vuex';
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
    headers() {
      if (this.matchingFile.parsed_content === null) {
        return ['No valid headers detected'];
      }
      const csvContent = JSON.parse(this.matchingFile.parsed_content);
      const headers = Object.keys(csvContent[0]);
      return headers;
    },
  },
  beforeMount() {
    this.$store.dispatch('loadCsvFiles');
  },
};
</script>
