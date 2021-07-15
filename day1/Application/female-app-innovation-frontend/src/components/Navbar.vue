
<template>
  <b-navbar fixed-bottom :mobile-burger="false">
    <template #start>
      <b-navbar-item tag="div"> Hallo </b-navbar-item>
      <b-navbar-item tag="block">
        <b-icon
          type="is-primary"
          size="is-large"
          icon="camera"
          pack="fas"
        ></b-icon>
      </b-navbar-item>
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
