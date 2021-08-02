<template>
  <div class="profile is-size-4">
    <b-image
      :src="profile.avatar_url"
      alt="Profile Picture of User"
      ratio="1by1"
      rounded
    ></b-image>
    <h1>{{ profile.name }}</h1>
    <b-field
      label="Github Username"
      :type="status"
      message="Check if your username is correct"
    >
      <b-input v-model="githubUsername" maxlength="30"></b-input>
    </b-field>
    <div class="buttons">
      <b-button
        rounded
        type="is-black"
        expanded
        v-on:click="saveProfile"
        :disabled="!isValid"
        >Save Profile</b-button
      >
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import axios from "axios";
import store from "../store/index";
import { debounce } from "lodash";

const githubApiUrl = "https://api.github.com/users/";

@Component({ store: store })
export default class EditProfile extends Vue {
  githubUsername = this.$store.state.githubUsername;
  isValid = false;
  profile = {};

  @Watch("githubUsername")
  public debouncedOnUsernameChanged = debounce(this.onUsernameChanged, 500);

  get status() {
    if (this.isValid) {
      return "is-success";
    }
    return "is-danger";
  }

  mounted() {
    this.onUsernameChanged();
  }

  onUsernameChanged() {
    console.log(this.githubUsername);
    axios
      .get(`${githubApiUrl}${this.githubUsername}`)
      .then((response) => {
        this.profile = response.data;
        this.isValid = true;
      })
      .catch((error) => {
        console.log(error);
        this.isValid = false;
      });
  }

  saveProfile() {
    this.$store.commit("setGithubUsername", this.githubUsername);
    this.$router.back();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.profile {
  padding: 30px;
}
</style>
