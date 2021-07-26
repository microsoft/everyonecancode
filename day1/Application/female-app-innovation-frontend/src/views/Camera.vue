<template>
  <div id="camera">
    <EasyCamera v-model="picture" fullscreen="true"></EasyCamera>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import axios from "axios";
import router from "../router";

const apiUrl = "https://fotobackendtest.azurewebsites.net";

function createGuid() {
  let S4 = () =>
    Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  let guid = `${S4()}${S4()}-${S4()}-${S4()}-${S4()}-${S4()}${S4()}${S4()}`;

  return guid.toLowerCase();
}

@Component({
  components: {},
})
export default class Camera extends Vue {
  picture = "";
  @Watch("picture")
  savePicture() {
    //console.log(this.picture);
    router.back();
    fetch(this.picture)
      .then((res) => res.blob())
      .then((blob) => {
        const file = new File([blob], `${createGuid()}.png`, {
          type: "image/png",
        });
        console.log(file);
        const data = new FormData();
        data.append("file", file);
        return axios.post(`${apiUrl}/upload/`, data, {
          headers: { "Content-Type": "multipart/form-data" },
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
