import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";

import axios from "axios";

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

const apiUrl = "https://fotobackendtest.azurewebsites.net";

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
      state.imageList = list;
    },
  },
  actions: {
    refreshImageList(context) {
      axios
        .get(`${apiUrl}/images`)
        .then((response) => {
          context.commit("setImageList", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteImage(context, image) {
      axios.delete(`${apiUrl}${image.image_url}`).then(() => {
        context.dispatch("refreshImageList");
      });
    },
  },
  modules: {},
  plugins: [vuexLocal.plugin],
});
