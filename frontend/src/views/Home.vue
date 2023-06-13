<template>
  <div id="app">
    <b-navbar fixed-top :mobile-burger="false">
      <template #brand>
        <div id="left"></div>
        <div id="right"></div>
        <div id="top"></div>
        <div id="bottom"></div>
        <b-navbar-item id="fontnavbar" class="title is-2" style="color:aqua">
          Alphagram
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
