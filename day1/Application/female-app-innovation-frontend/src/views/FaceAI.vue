<template>
  <section>
    <div v-if="!faces">
      <EasyCamera
        v-on:close="onClose"
        ref="camera"
        v-model="picture"
        fullscreen
      ></EasyCamera>
    </div>
    <section v-if="faces">
      <NavBarBack />
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
import NavBarBack from "../components/NavBarBack.vue";

import router from "../router";

const credentials = new ApiKeyCredentials({
  inHeader: { "Ocp-Apim-Subscription-Key": faceApiKey },
});

const client = new FaceClient(credentials, faceApiEndpoint);

@Component({
  components: { NavBarBack },
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

  onClose() {
    router.back();
  }

  @Watch("picture")
  savePicture() {
    this.camera.stop();
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
            this.faces = response.map((face) => {
              //let anger = face.faceAttributes.emotion.anger;
              //let contempt = face.faceAttributes.emotion.contempt;
              //let disgust = face.faceAttributes.emotion.disgust;
              //let fear = face.faceAttributes.emotion.fear;
              //let happiness = face.faceAttributes.emotion.happiness;
              //let neutral = face.faceAttributes.emotion.neutral;
              //let sadness = face.faceAttributes.emotion.sadness;
              //let surprise = face.faceAttributes.emotion.surprise;
              //let moustache = face.faceAttributes.facialHair.moustache;
              //let beard = face.faceAttributes.facialHair.beard;
              //let sideburns = face.faceAttributes.facialHair.sideburns;
              //let age2 = face.faceAttributes.age;

              const {
                age = 0,
                emotion: {
                  anger = "",
                  contempt = "",
                  disgust = "",
                  fear = "",
                  happiness = "",
                  neutral = "",
                  sadness = "",
                  surprise = "",
                } = {},
                facialHair: { moustache = "", beard = "", sideburns = "" } = {},
              } = { ...face };

              return {
                age: age,
                emotion: `${anger}, ${contempt}, ${disgust}, ${fear}, ${happiness}, ${neutral}, ${sadness}, ${surprise}`,
                facialHair: `${moustache}, ${beard}, ${sideburns}`,
              };
            });
          });
      });
  }
}
</script>

<style scoped></style>
