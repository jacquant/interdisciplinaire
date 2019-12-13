<template>
  <MglMap :accessToken="accessToken" :mapStyle="mapStyle" :replaceSource="true" @load="onMapLoaded">
    <MglNavigationControl position="top-right" />
    <MglMarker :coordinates="coordinates">
      <v-icon slot="marker" size="0">mdi-map-marker</v-icon>
      <MglPopup
        :coordinates="coordinates"
        :showed="popup"
        :closeButton="false"
        :closeOnClick="true"
      >
        <div>
          {{city_country_projects[0]}} - {{city_country_projects[1]}}
          <br />
          {{city_country_projects[2]}} Project(s)
        </div>
      </MglPopup>
    </MglMarker>
    <MglGeojsonLayer
      :sourceId="geoJsonSourceId"
      :source="geoJsonSource"
      :layer="geoJsonLayer"
      :layerId="geoJsonLayerId"
      @click="onClick"
      @mouseover="onOver"
    />
    <v-bottom-sheet v-model="sheet" scrollable>
      <v-card class="text-center">
        <v-card-title>{{concerned_data[0].properties.city}} - {{concerned_data[0].properties.country}}</v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-container fluid>
            <v-row class="grey lighten-5">
              <v-col cols="1">
                <v-card>#</v-card>
              </v-col>
              <v-col cols="4">
                <v-card>Adaptation action</v-card>
              </v-col>
              <v-col cols="3">
                <v-card>Climate Hazard</v-card>
              </v-col>
              <v-col cols="4">
                <v-card>Co Benefit Area</v-card>
              </v-col>
            </v-row>
            <v-row
              v-for="(item, index) in concerned_data"
              v-bind:item="item"
              v-bind:index="index"
              v-bind:key="index"
            >
              <v-col cols="1">
                <v-card @click="showDetails(index)" flat>{{index + 1}}</v-card>
              </v-col>
              <v-col cols="4">
                <v-card-text>{{item.properties.adaptation_action}}</v-card-text>
              </v-col>
              <v-col cols="3">
                <v-card-text>{{item.properties.climate_hazard}}</v-card-text>
              </v-col>
              <v-col cols="4">
                <v-card-text>{{item.properties.co_benefit_area}}</v-card-text>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>
    <v-row justify="center">
      <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
        <v-card>
          <v-toolbar dark color="green">
            <v-btn icon dark @click="dialog = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Details</v-toolbar-title>
          </v-toolbar>
          <v-card-title>{{selected_data.adaptation_action}}</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-list dense>
              <v-list-item-group v-model="item">
                <v-list-item v-for="(item, i) in Object.keys(selected_data).sort()" :key="i">
                  <v-list-item-content>
                    <v-list-item-title color="black">{{verbose_title[item]}}</v-list-item-title>
                    {{selected_data[item]}}
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card-text>
        </v-card>
      </v-dialog>
    </v-row>
  </MglMap>
</template>

<script>
import Mapbox from "mapbox-gl";
import {
  MglMap,
  MglNavigationControl,
  MglGeojsonLayer,
  MglPopup,
  MglMarker
} from "vue-mapbox";
import * as API from "../api";

import store from "../store";
export default {
  name: "Map",
  components: {
    MglMap,
    MglNavigationControl,
    MglGeojsonLayer,
    MglPopup,
    MglMarker
  },
  data: () => ({
    accessToken: store.state.mapboxToken,
    mapStyle: store.state.mapboxStyle,
    geoJsonSourceId: "mySourceId",
    geoJsonLayerId: "LayerId",
    geoJsonSource: {
      data: { type: "FeatureCollection", features: [] }
    },
    geoJsonLayer: {
      type: "circle",
      paint: {
        "circle-color": "#81C784"
      }
    },
    coordinates: [null, null],
    popup: false,
    sheet: false,
    dialog: false,
    item: 1,
    city_country_projects: [null, null, null],
    concerned_data: [{ properties: { city: null, country: null } }],
    selected_data: {},
    verbose_title: {
      access: "Access",
      account_number: "Account Number",
      action_description_and_implementation_progress:
        "Action Description And Implementation Progress",
      action_title: "Action Title",
      adaptation_action: "Adaptation Action",
      cdp_region: "CDP Region",
      city: "City",
      climate_hazard: "Climate Hazard",
      co_benefit_area: "Co-Benefit Area",
      country: "Country",
      finance_status: "Finance status",
      last_update: "Last Update",
      organization: "Organization",
      population: "Population",
      population_year: "Population Year",
      primary_source_fund: "Primary Source Fund",
      reporting_authority: "Reporting Authority",
      status_of_action: "Status of Action",
      total_cost_of_project: "Total Cost Of Project",
      total_cost_provided_by_the_local_government:
        "Total Cost Provided By The Local Government",
      web_link: "Web Link",
      year_reported_to_cdp: "Year Reported To CDP"
    }
  }),
  created: async function() {
    store.state.data = await API.get_geojson("?$limit=5000");
    this.geoJsonSource = { data: store.state.data };
    this.mapbox = Mapbox;
  },
  methods: {
    onMapLoaded() {
      this.geoJsonSource = { data: store.state.data };
    },
    onClick(e) {
      this.concerned_data = e.mapboxEvent.features;
      store.state.concerned_data = this.concerned_data;
      this.sheet = !this.sheet;
    },
    showDetails(index) {
      this.selected_data = store.state.concerned_data[index].properties;
      console.log(this.selected_data);
      delete this.selected_data[":@computed_region_n7dz_xzkg"];
      this.dialog = !this.dialog;
    },
    onOver(e) {
      this.coordinates = [e.mapboxEvent.lngLat.lng, e.mapboxEvent.lngLat.lat];
      this.city_country_projects = [
        e.mapboxEvent.features[0].properties.city,
        e.mapboxEvent.features[0].properties.country,
        e.mapboxEvent.features.length
      ];
      this.popup = !this.popup;
    }
  }
};
</script>