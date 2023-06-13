<template>
  <div class="profile is-size-4">
    <b-image
      :src="profile.avatar_url"
      alt="Profile Picture of User"
      ratio="1by1"
      style="margin-top: 100px"
      rounded
    ></b-image>
    <h1>{{ profile.name }}</h1>
    <div class="buttons">
      <b-button
        tag="router-link"
        to="/editprofile"
        rounded
        type="is-black"
        expanded
      >
        Edit Profile
      </b-button>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import axios from "axios";
import store from "../store/index";

const githubApiUrl = "https://api.github.com/users/";

@Component({ store: store })
export default class Profile extends Vue {
  profile = {};

  mounted() {
    this.getProfileDetails();
  }
  get githubUsername() {
    return this.$store.state.githubUsername;
  }

  @Watch("githubUsername")
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
