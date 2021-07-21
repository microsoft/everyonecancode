
<template>
  <div id="microphone">
    <VueRecordAudio @stream="onStream" @result="onResult" />
    <p class="is-large">{{ text }}</p>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import {
  SpeechConfig,
  AudioConfig,
  SpeechRecognizer,
  SpeechRecognitionEventArgs,
} from "microsoft-cognitiveservices-speech-sdk";

const apiKey = "d349139ec5084a5b816e99a4a01e02e7";
const region = "westeurope";

const speechConfig = SpeechConfig.fromSubscription(apiKey, region);
speechConfig.speechRecognitionLanguage = "de-DE";
var recognizer: SpeechRecognizer;

@Component({
  components: {},
})
export default class Microphone extends Vue {
  text = "";

  onStream(stream: MediaStream) {
    const audioConfig = AudioConfig.fromStreamInput(stream);
    recognizer = new SpeechRecognizer(speechConfig, audioConfig);
    recognizer.recognizing = this.onRegonitionResult;
    recognizer.recognized = this.onRegonitionResult;
    recognizer.startContinuousRecognitionAsync();
  }

  onRegonitionResult(sender: any, event: SpeechRecognitionEventArgs) {
    this.text = event.result.text;
  }

  onResult() {
    recognizer.stopContinuousRecognitionAsync();
  }
}
</script>

<style scoped>
</style>
