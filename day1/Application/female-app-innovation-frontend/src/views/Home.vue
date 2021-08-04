<template>
  <div id="app">
    <b-navbar fixed-top :mobile-burger="false">
      <template #brand>
        <b-navbar-item id="fontnavbar" class="title is-2">
          Milligram
        </b-navbar-item>
      </template>
    </b-navbar>
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

<style scoped>
#fontnavbar {
  font-family: HaloHandletter;
}
</style>
