<template>
  <div id="app">
    <div class="container">
      <Profile />
      <ImageList />
      <Navbar />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import ImageList from "../components/ImageList.vue";
import Profile from "../components/Profile.vue";
import Navbar from "../components/Navbar.vue";

@Component({
  components: {
    Profile,
    ImageList,
    Navbar,
  },
})
export default class Home extends Vue {}
</script>

<style scoped></style>
