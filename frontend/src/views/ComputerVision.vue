<template>
  <section>
    <div v-if="!description">
      <EasyCamera
        v-on:close="onClose"
        ref="camera"
        v-model="picture"
        :fullscreenZIndex="-1"
        fullscreen
      ></EasyCamera>
    </div>
    <section v-if="description">
      <NavBarBack />
      <h1>Results</h1>
      <div v-for="caption in description.captions">
        <p>{{ caption.text }}</p>
      </div>
      <div v-for="tag in description.tags">
        <p>{{ tag }}</p>
      </div>
    </section>
  </section>
</template>

<script lang="ts">
import { Component, Vue, Watch, Ref } from "vue-property-decorator";
import { ApiKeyCredentials } from "@azure/ms-rest-js";
import { ComputerVisionClient } from "@azure/cognitiveservices-computervision";
import { visionApiKey, visionApiEndpoint } from "../settings";
import NavBarBack from "../components/NavBarBack.vue";

import router from "../router";
import {
  DescribeImageInStreamResponse,
  ImageCaption,
} from "@azure/cognitiveservices-computervision/esm/models";

const credentials = new ApiKeyCredentials({
  inHeader: { "Ocp-Apim-Subscription-Key": visionApiKey },
});

const client = new ComputerVisionClient(credentials, visionApiEndpoint);

function check(value: number, text: string) {
  return value > 0.5 ? text : "";
}

@Component({
  components: { NavBarBack },
})
export default class FaceAI extends Vue {
  @Ref() readonly camera!: any;

  picture = "";
  description: DescribeImageInStreamResponse | null = null;

  onClose(): void {
    router.back();
  }

  @Watch("picture")
  savePicture(): void {
    this.camera.stop();
    fetch(this.picture)
      .then((res) => res.blob())
      .then((blob) => {
        client
          .describeImageInStream(blob)
          .then((res) => {
            this.description = res;
          })
          .catch((err) => {
            this.$alert(
              "An error occurred while trying to connect to Computer Vision. Try again and ask your coach if the problem persists.",
              "Computer Vision not available",
              "warning"
            ).then(() => this.$router.go(0));
            console.log("An error occurred:");
            console.error(err);
          });
      });
  }
}
</script>

<style scoped>
#faceRectContainer {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  margin-top: -3.25rem;
  pointer-events: none;
}

#faceRect {
  object-fit: cover;
  height: 100%;
  width: 100%;
  z-index: 2;
}
</style>
<style>
body.has-navbar-fixed-bottom {
  padding-bottom: 0rem;
  padding-top: 0rem;
}
</style>
