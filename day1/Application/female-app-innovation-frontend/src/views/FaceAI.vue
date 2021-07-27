<template>
  <div id="camera">
    <EasyCamera ref="camera" v-model="picture" fullscreen="true"></EasyCamera>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch, Ref } from "vue-property-decorator";
import EasyCamera from "easy-vue-camera";
import { ApiKeyCredentials } from "@azure/ms-rest-js";
import { FaceClient } from "@azure/cognitiveservices-face";

const endpoint =
  "https://female-tech-gen-face-api.cognitiveservices.azure.com/";
const apiKey = "ad4f4c1263834e3cab0213f29575f3a8";

const credentials = new ApiKeyCredentials({
  inHeader: { "Ocp-Apim-Subscription-Key": apiKey },
});

const client = new FaceClient(credentials, endpoint);

@Component({
  components: {},
})
export default class FaceAI extends Vue {
  @Ref() readonly camera!: EasyCamera;

  picture = "";
  @Watch("picture")
  savePicture() {
    this.camera.close();
    fetch(this.picture)
      .then((res) => res.blob())
      .then((blob) => {
        client.face.detectWithStream(blob).then((response) => {
          console.log(response);
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
