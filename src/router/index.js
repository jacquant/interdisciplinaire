import Vue from "vue";
import VueRouter from "vue-router";
import Charts from "../views/Charts.vue";
import Map from "../views/Map.vue";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "map",
      component: Map
    },
    {
      path: "/charts",
      name: "charts",
      component: Charts
    }
  ]
});
