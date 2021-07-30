<template>
  <section>
    <div v-if="!faces">
      <EasyCamera ref="camera" v-model="picture" fullscreen></EasyCamera>
    </div>
    <section v-if="faces">
      <b-tabs>
        <b-tab-item label="Results">
          <b-table :data="faces" :columns="columns"> </b-table>
        </b-tab-item>
      </b-tabs>
    </section>
  </section>
</template>

<script lang="ts">
import { Component, Vue, Watch, Ref } from "vue-property-decorator";
import { ApiKeyCredentials } from "@azure/ms-rest-js";
import { FaceClient } from "@azure/cognitiveservices-face";
import { faceApiKey, faceApiEndpoint } from "../settings";

const credentials = new ApiKeyCredentials({
  inHeader: { "Ocp-Apim-Subscription-Key": faceApiKey },
});

const client = new FaceClient(credentials, faceApiEndpoint);

@Component({
  components: {},
})
export default class FaceAI extends Vue {
  @Ref() readonly camera!: any;

  picture = "";
  faces: any = null;

  columns = [
    { field: "faceAttributes.age", label: "Age" },
    { field: "faceAttributes.emotion", label: "Emotion" },
    { field: "faceAttributes.facialHair", label: "Facial Hair" },
    { field: "faceAttributes.gender", label: "Gender" },
    { field: "faceAttributes.smile", label: "Smile" },
    { field: "faceAttributes.glasses", label: "Glasses" },
    { field: "faceAttributes.accessories", label: "accessories" },
  ];
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
</style>
