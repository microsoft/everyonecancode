
<template>
  <b-navbar fixed-bottom :mobile-burger="false">
    <template #brand>
      <div class="buttons container">
        <b-button rounded type="is-black">
          <router-link to="/camera">
            <b-icon type="is-white" icon="camera" pack="fas"></b-icon>
          </router-link>
        </b-button>
        <b-button rounded type="is-black">
          <router-link to="/microphone">
            <b-icon type="is-white" icon="microphone" pack="fas"></b-icon>
          </router-link>
        </b-button>
      </div>
    </template>
  </b-navbar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Navbar extends Vue {}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
