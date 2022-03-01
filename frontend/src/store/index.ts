import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";

import axios from "axios";

import { imageApiUrl } from "../settings";

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    githubUsername: "CodeUnicornMartha",
    imageList: [],
  },
  mutations: {
    setGithubUsername(state, githubUsername) {
      state.githubUsername = githubUsername;
    },
    setImageList(state, list) {
      console.log(list)
      state.imageList = list;
    },
  },
  actions: {
    refreshImageList(context) {
      axios
        .get(`${imageApiUrl}images`)
        .then((response) => {
          context.commit("setImageList", response.data);
        })
        .catch((error) => {
          context.commit("setImageList", []);
          console.log(error);
        });
    },
    deleteImage(context, image) {
      axios.delete(`${imageApiUrl}${image.image_url}`).then(() => {
        context.dispatch("refreshImageList");
      });
    },
  },
  modules: {},
  plugins: [vuexLocal.plugin],
});
