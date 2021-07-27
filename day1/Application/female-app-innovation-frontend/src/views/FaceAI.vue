<template>
  <div id="camera">
    <div v-if="!faces">
      <EasyCamera ref="camera" v-model="picture" fullscreen="true"></EasyCamera>
    </div>
    <div v-if="faces" class="tile is-parent">
      <div v-for="face in faces" :key="face.id" class="tile is-child">
        {{ face.faceAttributes.age }}
        {{ face.faceAttributes.emotion }}
        {{ face.faceAttributes.facialHair }}
        {{ face.faceAttributes.gender }}
        {{ face.faceAttributes.smile }}
        {{ face.faceAttributes.glasses }}
        {{ face.faceAttributes.accessories }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch, Ref } from "vue-property-decorator";
import EasyCamera from "easy-vue-camera";
import { ApiKeyCredentials } from "@azure/ms-rest-js";
import { FaceClient } from "@azure/cognitiveservices-face";
import { FaceAttributes } from "@azure/cognitiveservices-face/esm/models/mappers";

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
  faces? = null;

  @Watch("picture")
  savePicture() {
    this.camera.close();
    fetch(this.picture)
      .then((res) => res.blob())
      .then((blob) => {
        client.face
          .detectWithStream(blob, {
            returnFaceAttributes: [
              "age",
              "emotion",
              "facialHair",
              "smile",
              "gender",
              "glasses",
              "accessories",
            ],
          })
          .then((response) => {
            this.faces = response;
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
