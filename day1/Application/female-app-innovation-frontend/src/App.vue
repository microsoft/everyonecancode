<template>
  <div id="app">
    <Profile/>
    <ImageList/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import ImageList from "./components/ImageList.vue";
import Profile from "./components/Profile.vue";

@Component({
  components: {
    Profile,
    ImageList
  },
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
