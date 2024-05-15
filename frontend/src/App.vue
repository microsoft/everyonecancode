<template>
  <div id="app">
    <div id="left"></div>
    <div id="right"></div>
    <div id="top"></div>
    <div id="bottom"></div>
    <transition :name="transitionName">
      <vue-page-stack>
        <router-view :key="screen" class="router-view-c"></router-view>
      </vue-page-stack>
    </transition>
    <footer class="footer">
      Made with love ❤️
    </footer>
  </div>
</template>

<style lang="scss">
/* Existing styles */

.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px;
  background-color: #3f0f0f;
  text-align: center;
  font-size: 14px;
  color: #888888;
}
</style>
