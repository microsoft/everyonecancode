<template>
  <div id="microphone">
    <div id="select">
      <h2>Select your language:</h2>
      <select name="lang" @change="onChange($event)" class="custom-select">
        <option value="de-DE" selected>German</option>
        <option value="en-US">English</option>
        <option value="ja-JP">日本語</option>
      </select>
    </div>
    <br />
    <NavBarBack />
    <VueRecordAudio mode="press" @stream="onStream" @result="onResult" />
    <p class="is-large">{{ text }}</p>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

// This works after `npm run build`:
import {
  AudioConfig,
  SpeechConfig,
  SpeechRecognizer,
  SpeechRecognitionEventArgs,
} from "microsoft-cognitiveservices-speech-sdk";

// This works on local machines:
// import "microsoft-cognitiveservices-speech-sdk/distrib/browser/microsoft.cognitiveservices.speech.sdk.bundle";
// import type * as SpeechSDKType from "microsoft-cognitiveservices-speech-sdk/distrib/lib/microsoft.cognitiveservices.speech.sdk";

// declare global {
//   interface Window {
//     SpeechSDK: {
//       AudioConfig: typeof SpeechSDKType.AudioConfig;
//       OutputFormat: typeof SpeechSDKType.OutputFormat;
//       Recognizer: typeof SpeechSDKType.Recognizer;
//       SpeechConfig: typeof SpeechSDKType.SpeechConfig;
//       SpeechRecognizer: typeof SpeechSDKType.SpeechRecognizer;
//     };
//   }
// }
// const {
//   AudioConfig,
//   OutputFormat,
//   Recognizer,
//   SpeechConfig,
//   SpeechRecognizer,
// } = window.SpeechSDK;

import { speechApiKey } from "../settings";

import NavBarBack from "../components/NavBarBack.vue";

const region = "westeurope";

var recognizer: SpeechRecognizer;

@Component({
  components: { NavBarBack },
})
export default class Microphone extends Vue {
  text = "";
  selectedLanguage = "de-DE";

  onStream(stream: MediaStream): void {
    const speechConfig = SpeechConfig.fromSubscription(speechApiKey, region);
    speechConfig.speechRecognitionLanguage = this.selectedLanguage;
    const audioConfig = AudioConfig.fromStreamInput(stream);
    recognizer = new SpeechRecognizer(speechConfig, audioConfig);
    recognizer.recognizing = this.onRegonitionResult;
    recognizer.recognized = this.onRegonitionResult;
    recognizer.startContinuousRecognitionAsync();
  }

  onRegonitionResult(sender: any, event: SpeechRecognitionEventArgs): void {
    this.text = event.result.text;
  }

  onResult(): void {
    recognizer.stopContinuousRecognitionAsync();
  }

  onChange(e: any) {
    this.selectedLanguage = e.target.value;
    console.log(e.target.value);
  }
}
</script>

<style scoped>
#microphone {
  margin-top: 3.25rem;
}
.custom-select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 57px;
  padding: 10px 38px 10px 16px;
  background-size: 10px;
  transition: border-color 0.1s ease-in-out, box-shadow 0.1s ease-in-out;
  border: 1px solid #ddd;
  border-radius: 3px;
}
.custom-select:hover {
  border: 1px solid #999;
}
.custom-select:focus {
  border: 1px solid #999;
  box-shadow: 0 3px 5px 0 rgba(0, 0, 0, 0.2);
  outline: none;
}
/* remove default arrow in IE */
select::-ms-expand {
  display: none;
}

/* DEMO STYLING */
html {
  height: 100%;
  font-size: 62.5%;
}
body {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: "Source Sans Pro", sans-serif;
  font-size: 1.8rem;
  color: #333;
  background: radial-gradient(ellipse at center, #f5f5f5 0%, #ddd 100%);
}
.custom-select {
  font-family: "Source Sans Pro", sans-serif;
  font-size: 1.6rem;
}
</style>
