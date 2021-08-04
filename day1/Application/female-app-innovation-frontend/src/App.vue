<template>
  <div id="app">
    <transition :name="transitionName">
      <vue-page-stack>
        <router-view :key="screen" class="router-view-c"></router-view>
      </vue-page-stack>
    </transition>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
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
export default class App extends Vue {
  transitionName = "forward";
  screen = "home";

  @Watch("$route")
  route(to: any, from: any) {
    if (to.params["stack-key-dir"] === "forward") {
      this.transitionName = "forward";
    } else {
      this.transitionName = "back";
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
  height: 100%;

  .cube-btn {
    border-radius: 5px;
    padding: 15px;
    margin: 5px 0;
  }

  .cube-input {
    margin: 5px 0;
    input {
      padding: 8px;
    }
  }
  .cube-input_active::after {
    border-radius: 5px;
  }
  @keyframes show {
    0% {
      transform: translateY(100px);
    }
    60% {
      transform: translateY(-80upx);
    }
    100% {
      transform: translateY(0px);
    }
  }
}
.router-view-c {
  position: absolute;
  transition: opacity 0.5s, transform 0.5s;
  width: 100%;
}
.forward-enter,
.back-leave-active {
  opacity: 0.5;
  transform: translateX(100%);
}
.forward-leave-active,
.back-enter {
  opacity: 0.5;
  transform: translateX(-100%);
}
@font-face {
  font-family: HaloHandletter;
  src: url("../public/fonts/HaloHandletter.otf") format("opentype");
}
</style>
