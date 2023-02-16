<template>
  <b-navbar fixed-bottom centered :mobile-burger="false">
    <template #brand>
      <div id="left"></div>
      <div id="right"></div>
      <div id="top"></div>
      <div id="bottom"></div>
      <div class="buttons-container navbar-center">
        <b-button v-if="showCameraButton" rounded type="is-black">
          <router-link to="/camera">
            <b-icon type="is-white" icon="camera" pack="fas"></b-icon>
          </router-link>
        </b-button>
        <b-button v-if="showSpeechButton" rounded type="is-black">
          <router-link to="/microphone">
            <b-icon type="is-white" icon="microphone" pack="fas"></b-icon>
          </router-link>
        </b-button>
        <b-button v-if="showFaceButton" rounded type="is-black">
          <router-link to="/faceai">
            <b-icon type="is-white" icon="grin-stars" pack="fas"></b-icon>
          </router-link>
        </b-button>
        <b-button v-if="showVisionButton" rounded type="is-black">
          <router-link to="/vision">
            <b-icon type="is-white" icon="object-group" pack="fas"></b-icon>
          </router-link>
        </b-button>
      </div>
    </template>
  </b-navbar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import {
  imageApiUrl,
  faceApiKey,
  faceApiEndpoint,
  speechApiKey,
  visionApiKey,
} from "../settings";

@Component
export default class Navbar extends Vue {
  get showCameraButton(): boolean {
    return imageApiUrl !== "";
  }
  get showFaceButton(): boolean {
    return faceApiKey !== "" && faceApiEndpoint !== "";
  }
  get showSpeechButton(): boolean {
    return speechApiKey !== "";
  }
  get showVisionButton(): boolean {
    return visionApiKey !== "";
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.buttons-container {
  padding: 2px;
}
.navbar-center {
  width: 500px;
  position: absolute;
  left: 50%;
  transform: translatex(-50%);
}

.button {
  margin: 0px 10px;
}

#top,
#bottom,
#left,
#right {
  background: linear-gradient(
    45deg,
    #f09433 0%,
    #e6683c 25%,
    #dc2743 50%,
    #cc2366 75%,
    #bc1888 100%
  );
  position: fixed;
}
#left,
#right {
  top: 0;
  bottom: 0;
  width: 2px;
}
#left {
  left: 0;
}
#right {
  right: 0;
}

#top,
#bottom {
  left: 0;
  right: 0;
  height: 2px;
}
#top {
  top: 0;
}
#bottom {
  bottom: 0;
}
</style>
