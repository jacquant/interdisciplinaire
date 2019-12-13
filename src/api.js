"use strict";

import axios from "axios";
import store from "./store";

//// ///////////////////////////////////////////////////////////////////////////
//// Definition of private attributes
//// ///////////////////////////////////////////////////////////////////////////

const base_url_adaptations_geojson =
  "https://data.cdp.net/resource/6zdf-pmyg.geojson";
const base_url_adaptations_json =
  "https://data.cdp.net/resource/6zdf-pmyg.json";
//// ///////////////////////////////////////////////////////////////////////////
//// Definition of private methods
//// ///////////////////////////////////////////////////////////////////////////

/**
 * Execute an API request and return the value of response data.
 *
 * @async
 * @param {object} config - The request configuration.
 * @param {boolean} token - Indicates if the connection token must be added to the request configuration.
 * @returns {Promise<object>}
 */
async function request(config, token) {
  // If necessary, add the token in the request configuration object
  if (token)
    config.headers = {
      "X-App-Token": store.state.apiAppToken
    };

  // Execute the request
  return (await axios(config)).data;
}

//// ///////////////////////////////////////////////////////////////////////////
//// Definition of public methods
//// ///////////////////////////////////////////////////////////////////////////

export default axios;

/**
 * Execute a GET request on the API.
 * Returns directly the response value of the request as defined on {@link https://data.cdp.net/resource/6zdf-pmyg.json}.
 *
 * @param {string} name - The API point.
 * @param {boolean} [withToken=true] - Indicates if the token must be added to the request.
 * @param {object} [c={}] - Additional configuration.
 * @returns {Promise<*>}
 */
export async function get_geojson(name, withToken = true, c = {}) {
  return request(
    { method: "GET", url: base_url_adaptations_geojson + name, ...c },
    withToken
  );
}

export async function get_json(name, withToken = true, c = {}) {
  return request(
    { method: "GET", url: base_url_adaptations_json + name, ...c },
    withToken
  );
}
/**
 * Execute a POST request on the API.
 * Returns directly the response value of the request as defined on {@link https://data.cdp.net/resource/6zdf-pmyg.json}.
 *
 * @param {string} name - The API point.
 * @param {object} data - The data to send.
 * @param {boolean} [withToken=true] - Indicates if the token must be added to the request.
 * @param {object} [c={}] - Additional configuration.
 * @returns {Promise<*>}
 */
export async function post(name, data, withToken = true, c = {}) {
  return request(
    { method: "POST", url: base_url_adaptations_geojson + name, data, ...c },
    withToken
  );
}

/**
 * Execute a PUT request on the API.
 * Returns directly the response value of the request as defined on {@link http://api.chu.cslabs.be/api-doc/}.
 *
 * @param {string} name - The API point.
 * @param {object} data - The data to send.
 * @param {boolean} [withToken=true] - Indicates if the token must be added to the request.
 * @param {object} [c={}] - Additional configuration.
 * @returns {Promise<*>}
 */
export async function put(name, data, withToken = true, c = {}) {
  return request(
    { method: "PUT", url: base_url_adaptations_geojson + name, data, ...c },
    withToken
  );
}
