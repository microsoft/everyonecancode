<template>
  <div>
    <img :src="profile.avatar_url" />
    <h2>{{ profile.name }}</h2>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios from "axios";

const githubApiUrl = "https://api.github.com/users/";

@Component
export default class Profile extends Vue {
  githubUsername = "CodeUnicornMartha";
  profile = {};

  mounted() {
    this.getProfileDetails();
  }

  getProfileDetails() {
    axios
      .get(`${githubApiUrl}${this.githubUsername}`)
      .then((response) => {
        this.profile = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
