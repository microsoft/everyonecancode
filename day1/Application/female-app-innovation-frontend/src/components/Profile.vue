<template>
  <div class="profile is-size-4">
    <b-image
      :src="profile.avatar_url"
      alt="Profile Picture of User"
      ratio="1by1"
      rounded
    ></b-image>
    <h1>{{ profile.name }}</h1>
    <div class="buttons">
      <b-button rounded type="is-black" expanded>
        <router-link to="/editprofile"> Edit Profile </router-link>
      </b-button>
    </div>
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
.profile {
  padding: 30px;
}
</style>
