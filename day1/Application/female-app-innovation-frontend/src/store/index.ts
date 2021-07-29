import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {githubUsername:""},
  mutations: {
    setGithubUsername (state, githubUsername) {
      state.githubUsername = githubUsername;
    }
  },
  actions: {},
  modules: {},
});

