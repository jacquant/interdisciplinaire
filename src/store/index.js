import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiAppToken: "6ChncaiwGpqRmgJuoKNCbuHT2",
    mapboxStyle: "mapbox://styles/jacquant/ck338p35a0rrh1cmuvxi2r39q",
    mapboxToken:
      "pk.eyJ1IjoiamFjcXVhbnQiLCJhIjoiY2syeHFpemxqMDAxYzNsbXFrcWwwOGxmbyJ9.F94lOloBRxltcsySUlvwGA",
    data: {},
    concerned_data: []
  },
  getters: {
    numbers_data: state => {
      return state.data.length;
    }
  },
  mutations: {},
  actions: {},
  modules: {}
});
