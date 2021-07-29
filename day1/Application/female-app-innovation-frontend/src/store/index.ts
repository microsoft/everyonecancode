import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

Vue.use(Vuex);

export default new Vuex.Store({
  state: { githubUsername: "" },
  mutations: {
    setGithubUsername(state, githubUsername) {
      state.githubUsername = githubUsername;
    },
  },
  actions: {},
  modules: {},
  plugins: [vuexLocal.plugin],
});
