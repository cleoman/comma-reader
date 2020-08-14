<template>
  <div>
    <v-card>
      <v-card-title>{{matchingFile.name}} stats</v-card-title>
      <v-card-body>
        <!-- TODO: v-data-table for free sorting -->
        <table border="1px">
          <thead>
            <th>Year</th>
            <th># of entries</th>
          </thead>
          <tbody>
            <tr v-for="(value, name) in csvFileStats.dates" :key="name">
              <td>{{name}}</td>
              <td>{{value}}</td>
            </tr>
          </tbody>
        </table>
      </v-card-body>
    </v-card>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

export default {
  name: 'Stats',
  components: {
  },
  computed: {
    ...mapState({
      csvFileStats: (state) => state.csvFileStats,
    }),
    ...mapGetters({
      getCsvFileById: 'getCsvFileById',
    }),
    matchingFile() {
      return this.getCsvFileById(parseInt(this.$route.params.id, 10));
    },
  },
  beforeMount() {
    this.$store.dispatch('loadCsvFileStats', parseInt(this.$route.params.id, 10));
  },
};
</script>
