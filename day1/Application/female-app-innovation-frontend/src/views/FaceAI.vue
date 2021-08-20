<template>
  <section>
    <div v-if="faces.length == 0">
      <canvas id="ghostVideo" style="display: none"></canvas>
      <div id="faceRectContainer">
        <canvas id="faceRect"></canvas>
      </div>
      <EasyCamera
        v-on:close="onClose"
        ref="camera"
        v-model="picture"
        :fullscreenZIndex="-1"
        fullscreen
      ></EasyCamera>
    </div>
    <section v-if="faces.length > 0">
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
  faces: any = [];
  liveFaces: any = null;
  faceRect = { width: 92, height: 92, left: 301, top: 149 }; // hardcoded rectangle for testing
  useLiveFaceDetection = false; // toggle live face detection in camera view

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

  created() {
    window.setInterval(() => {
      let canvas = document.getElementById("ghostVideo") as HTMLCanvasElement; // declare a canvas element in your html
      let ctx = canvas.getContext("2d");
      let video = document.querySelector("video");
      let imageWidth = 0;
      let imageHeight = 0;

      // move content of video tag into invisible canvas
      const v = video;
      if (ctx == null || v == null) return;

      try {
        imageWidth = v.videoWidth;
        imageHeight = v.videoHeight;
        canvas.width = imageWidth;
        canvas.height = imageHeight;
        ctx.fillRect(0, 0, imageWidth, imageHeight);
        ctx.drawImage(v, 0, 0, imageWidth, imageHeight);
        const frame: string = canvas.toDataURL();
        ctx.clearRect(0, 0, imageWidth, imageHeight); // clean the canvas

        // need to use a new canvas here on top of the camera
        const faceRectCanvas = document.getElementById(
          "faceRect"
        ) as HTMLCanvasElement;
        faceRectCanvas.width = imageWidth;
        faceRectCanvas.height = imageHeight;
        var ctx2 = faceRectCanvas.getContext("2d");

        // draw rectangle
        if (ctx2 != null) {
          ctx2.rect(
            this.faceRect.left,
            this.faceRect.top,
            this.faceRect.width,
            this.faceRect.height
          );
          ctx2.stroke();
        }

        if (frame !== "data:," && this.useLiveFaceDetection) {
          // check if camera is ready
          fetch(frame)
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
                  this.liveFaces = response.map((face) => {
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
                      facialHair: {
                        moustache = 0,
                        beard = 0,
                        sideburns = 0,
                      } = {},
                      gender = "",
                      smile = 0,
                      glasses = "",
                    } = { ...face.faceAttributes };

                    console.log(face.faceRectangle);

                    this.faceRect = face.faceRectangle;
                  });
                });
            });
        }
      } catch (e) {
        console.log(e);
      }
    }, 1000);
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

body.has-navbar-fixed-bottom{
  padding-bottom: 0rem;
  padding-top: 0rem;
}
</style>
