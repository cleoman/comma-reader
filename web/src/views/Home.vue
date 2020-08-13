<template>
  <div class="home">
      <div v-for="row in csvFiles" :key="row.id">
        <router-link to="/csvfile">{{row.name}}</router-link>
      </div>
      <csv-table></csv-table>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import CsvTable from '@/components/CsvTable.vue';

export default {
  name: 'Home',
  components: {
    'csv-table': CsvTable,
  },
  computed: mapState({
    csvFiles: (state) => state.csvFiles,
  }),
  beforeMount() {
    this.$store.dispatch('loadCsvFiles');
  },
};
</script>
