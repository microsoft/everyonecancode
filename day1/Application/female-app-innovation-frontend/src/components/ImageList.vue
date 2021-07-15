<template>
  <div>
    <div>
      <div v-for="image in imageList" :key="image">
        <img width="400px" :src="image.url" />
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
