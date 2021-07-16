<template>
  <div id="app">
    <div class="container">
      <vue-web-cam selectFirstDevice="true"/>
      <Profile />
      <ImageList />
      <Navbar />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import ImageList from "./components/ImageList.vue";
import Profile from "./components/Profile.vue";
import Navbar from "./components/Navbar.vue";

@Component({
  components: {
    Profile,
    ImageList,
    Navbar,
  },
})
export default class App extends Vue {}
</script>

<style>
body {
  background-image: linear-gradient(rgb(228, 248, 248), rgb(39, 35, 243));
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
