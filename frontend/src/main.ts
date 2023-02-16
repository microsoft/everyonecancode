import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import Buefy from "buefy";
import "buefy/dist/buefy.css";

import { library } from "@fortawesome/fontawesome-svg-core";
// internal icons
import {
  faCamera,
  faMicrophone,
  faGrinStars,
  faCheck,
  faExclamationCircle,
  faArrowLeft,
  faObjectGroup,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import router from "./router";
import EasyCamera from "easy-vue-camera";
import VueRecord from "@codekraft-studio/vue-record";
import VueSimpleAlert from "vue-simple-alert";

library.add(
  faCamera as any,
  faMicrophone as any,
  faGrinStars as any,
  faCheck as any,
  faExclamationCircle as any,
  faArrowLeft as any,
  faObjectGroup as any
);
Vue.use(VueSimpleAlert);
Vue.use(VueRecord);
Vue.component("vue-fontawesome", FontAwesomeIcon);
Vue.use(Buefy, {
  defaultIconComponent: "vue-fontawesome",
  defaultIconPack: "fas",
});
Vue.component("EasyCamera", EasyCamera);
Vue.config.productionTip = false;
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
