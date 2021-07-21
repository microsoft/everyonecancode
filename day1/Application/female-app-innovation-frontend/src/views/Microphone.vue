
<template>
  <div id="microphone">
    <h1>Microphone</h1>
    <VueRecordAudio @stream="onStream" @result="onResult" />
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import axios from "axios";

const apiUrl =
  "https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken";
const apiKey = "d349139ec5084a5b816e99a4a01e02e7";

@Component({
  components: {},
})
export default class Microphone extends Vue {
  onStream(data: any) {
    console.log(data);
  }

  result(data: any) {
    console.log(data);
  }
}
</script>

<style scoped>
</style>
