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

function check(value: number, text: string) {
  return value > 0.5 ? text : "";
}

@Component({
  components: { NavBarBack },
})
export default class FaceAI extends Vue {
  @Ref() readonly camera!: any;

  picture = "";
  faces: any = null;

  columns = [
    { field: "age", label: "Age" },
    { field: "emotion", label: "Emotion" },
    { field: "facialHair", label: "Facial Hair" },
    { field: "gender", label: "Gender" },
    { field: "smile", label: "Smile" },
    { field: "glasses", label: "Glasses" },
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
            ],
          })
          .then((response) => {
            this.faces = response.map((face) => {
              const {
                age = 0,
                emotion: {
                  anger = 0,
                  contempt = 0,
                  disgust = 0,
                  fear = 0,
                  happiness = 0,
                  neutral = 0,
                  sadness = 0,
                  surprise = 0,
                } = {},
                facialHair: { moustache = 0, beard = 0, sideburns = 0 } = {},
                gender = "",
                smile = 0,
                glasses = "",
              } = { ...face.faceAttributes };

              return {
                age,
                emotion: `${check(anger, "anger")} ${check(
                  contempt,
                  "contempt"
                )} ${check(disgust, "disgust")} ${check(fear, "fear")} ${check(
                  happiness,
                  "happiness"
                )} ${check(neutral, "neutral")} ${check(
                  sadness,
                  "sadness"
                )} ${check(surprise, "surprise")}`,
                facialHair: `${check(moustache, "moustache")} ${check(
                  beard,
                  "beard"
                )} ${check(sideburns, "sideburns")}`,
                gender,
                smile: `${check(smile, "smile")}`,
                glasses,
              };
            });
          });
      });
  }
}
</script>

<style scoped></style>
