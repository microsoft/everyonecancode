<template>
  <div id="camera">
    <EasyCamera v-model="picture" fullscreen="true"></EasyCamera>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import router from "../router";

@Component({
  components: {},
})
export default class FaceAI extends Vue {
  picture = "";
  @Watch("picture")
  savePicture() {
    //console.log(this.picture);
    router.back();
    fetch(this.picture)
      .then((res) => res.blob())
      .then((blob) => {
        const file = new File([blob], `face.png`, {
          type: "image/png",
        });
        console.log(file);
        const data = new FormData();
        data.append("file", file);
        // TODO: call face api
      });
  }
}
</script>

<style scoped>
#camera {
  width: 100vh;
}
</style>
