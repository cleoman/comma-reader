<template>
  <div class="home">
    <div>
      <span>Uploading happens here.</span>
    </div>
    <div>
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
    </div>
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
  beforeMount() {
    this.$store.dispatch('loadCsvFiles');
  },
};
</script>
