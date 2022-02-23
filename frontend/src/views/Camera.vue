<template>
  <div id="camera">
    <EasyCamera
      ref="camera"
      v-on:close="onClose"
      v-model="picture"
      fullscreen
    ></EasyCamera>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch, Ref } from "vue-property-decorator";
import axios from "axios";
import router from "../router";
import store from "../store/index";

import { imageApiUrl } from "../settings";

function createGuid() {
  let S4 = () =>
    Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  let guid = `${S4()}${S4()}-${S4()}-${S4()}-${S4()}-${S4()}${S4()}${S4()}`;

  return guid.toLowerCase();
}

@Component({
  store: store,
})
export default class Camera extends Vue {
  @Ref() readonly camera!: any;

  picture = "";

  onClose() {
    router.back();
  }

  @Watch("picture")
  savePicture() {
    this.camera.close();
    fetch(this.picture)
      .then((res) => res.blob())
      .then((blob) => {
        const file = new File([blob], `${createGuid()}.png`, {
          type: "image/png",
        });
        console.log(file);
        const data = new FormData();
        data.append("file", file);
        return axios
          .post(`${imageApiUrl}upload/`, data, {
            headers: { "Content-Type": "multipart/form-data" },
          })
          .then(() => {
            this.$store.dispatch("refreshImageList");
          });
      });
  }
}
</script>

<style scoped>
#camera {
  width: 100vh;
}
</style>
