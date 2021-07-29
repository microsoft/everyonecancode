<template>
  <div>
    <div>
      <div
        class="tile is-parent"
        v-for="image in imageList"
        :key="image.image_url"
      >
        <div class="tile is-child">
          <b-image ratio="1by1  " :src="`${apiUrl}/${image.image_url}`" />
          <b-button
            id="btn-delete"
            rounded
            type="is-black"
            v-on:click="deleteImage(image)"
          >
            Delete
          </b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class ImageList extends Vue {
  apiUrl = "https://fotobackendtest.azurewebsites.net";
  imageList = [];

  deleteImage(image: any) {
    console.log(image);
    axios.delete(`${this.apiUrl}${image.image_url}`).then(() => {
      this.getImageList();
    });
  }

  mounted() {
    this.getImageList();
  }

  getImageList() {
    axios
      .get(`${this.apiUrl}/images`)
      .then((response) => {
        this.imageList = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#btn-delete {
  margin-top: 5px;
}
</style>
