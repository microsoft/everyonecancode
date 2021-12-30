<template>
  <b-navbar fixed-top :mobile-burger="false">
    <template #brand>
      <div class="buttons container">
        <b-button rounded v-on:click="onBack" type="is-black">
          <b-icon type="is-white" icon="arrow-left" pack="fas"></b-icon>
        </b-button>
      </div>
    </template>
  </b-navbar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import router from "../router";

@Component
export default class NavbarBack extends Vue {
  onBack() {
    router.back();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
