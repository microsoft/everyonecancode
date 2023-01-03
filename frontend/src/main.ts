// import Vue from "vue";
import App from "./App.vue";
// import store from "./store";
import Buefy from "buefy";
import "buefy/dist/buefy.css";

// import { library } from "@fortawesome/fontawesome-svg-core";
// internal icons
// import {
//   faCamera,
//   faMicrophone,
//   faGrinStars,
//   faCheck,
//   faExclamationCircle,
//   faArrowLeft,
// } from "@fortawesome/free-solid-svg-icons";
// import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import router from "./router";

// import EasyCamera from "easy-vue-camera";
// import VueRecord from "@codekraft-studio/vue-record";
// import VueSimpleAlert from "vue-simple-alert";

// library.add(
//   faCamera as any,
//   faMicrophone as any,
//   faGrinStars as any,
//   faCheck as any,
//   faExclamationCircle as any,
//   faArrowLeft as any
// );
// Vue.use(VueSimpleAlert);
// Vue.use(VueRecord);
// Vue.component("vue-fontawesome", FontAwesomeIcon);
// Vue.use(Buefy, {
//   defaultIconComponent: "vue-fontawesome",
//   defaultIconPack: "fas",
// });
// Vue.component("EasyCamera", EasyCamera);
// Vue.config.productionTip = false;
/// New Stuff
import { createApp } from "vue";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

const app = createApp(App);

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
app.use(pinia);
app.use(Buefy);
app.use(router);

app.mount("#app");
