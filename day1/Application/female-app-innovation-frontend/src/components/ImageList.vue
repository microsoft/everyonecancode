<template>
  <div>
    <div>
      <div class="tile is-parent" v-for="image in imageList" :key="image">
        <div class="tile is-child">
        <b-image ratio="1by1  " :src="image.url" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios from "axios";

const apiUrl = "https://fotobackendtest.azurewebsites.net";

@Component
export default class ImageList extends Vue {
  imageList = [];

  mounted() {
    this.getImageList();
  }

  getImageList() {
    axios
      .get(`${apiUrl}/images`)
      .then((response) => {
        this.imageList = response.data.files.map((file: any) => {
          return {
            url: `${apiUrl}/images/${file}`,
          };
        });
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
