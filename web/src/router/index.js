import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import CsvFile from '../views/CsvFile.vue';
import Stats from '../views/Stats.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/csvfile/:id',
    name: 'CsvFile',
    component: CsvFile,
  },
  {
    path: '/csvfile/stats/:id',
    name: 'Stats',
    component: Stats,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
