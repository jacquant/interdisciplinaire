<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="menuDisplay" app color="green lighten-2" expand-on-hover>
      <v-list dense>
        <v-list-item v-for="(item, index) in menu" :key="index" :to="getRouteUrl(item.href)">
          <v-list-item-action>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.label"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-navigation-drawer
      v-model="filterDisplay"
      app
      color="green lighten-2"
      :right="true"
      :floating="true"
    >
      <v-range-slider v-model="range" :max="max" :min="min" hide-details class="align-center">
        <template v-slot:prepend>
          <v-text-field
            v-model="range[0]"
            class="mt-0 pt-0"
            hide-details
            single-line
            type="number"
            style="width: 60px"
          ></v-text-field>
        </template>
        <template v-slot:append>
          <v-text-field
            v-model="range[1]"
            class="mt-0 pt-0"
            hide-details
            single-line
            type="number"
            style="width: 60px"
          ></v-text-field>
        </template>
      </v-range-slider>
    </v-navigation-drawer>

    <v-app-bar app color="green" dark>
      <v-app-bar-nav-icon @click="menuDisplay = !menuDisplay" />
      <v-toolbar-title>Adaptation Actions</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon @click="filterDisplay = !filterDisplay">mdi-filter</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <transition name="fade" mode="out-in">
        <router-view></router-view>
      </transition>
    </v-content>
    <v-footer app color="green" dark>
      <span
        class="white--text"
      >&copy; 2019 - Projet interdisciplinaire (Antoine Jacques - Pauline Bonmariage - Soazic Delefortrie)</span>
    </v-footer>
  </v-app>
</template>
<script>
export default {
  name: "App",
  data: function() {
    return {
      menu: [
        {
          label: "Map",
          icon: "mdi-map",
          href: "map"
        },
        {
          label: "Charts",
          icon: "mdi-chart-pie",
          href: "charts"
        }
      ],
      menuDisplay: this.$vuetify.breakpoint.lgAndUp,
      filterDisplay: false,
      min: 0,
      max: 100000000,
      slider: 100000000,
      range: [0, 100000000]
    };
  },
  methods: {
    getRouteUrl(name) {
      return this.$router.resolve({ name }).route.path;
    }
  }
};
</script>