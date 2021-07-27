<template>
  <div>
    <div>
      <div
        class="tile is-parent"
        v-for="image in imageList"
        :key="image.image_url"
      >
        <div class="tile is-child">
          <b-image ratio="1by1  " :src="image.image_url" />
          <b-button rounded type="is-black" v-on:click="deleteImage(image)">
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

const apiUrl = "https://fotobackendtest.azurewebsites.net";

@Component
export default class ImageList extends Vue {
  imageList = [];

  deleteImage(image: any) {
    console.log(image);
    if (window.location.href.split("/")[0] == "https") {
      console.log("change url");
      image.image_url = image.image_url.replace("http://", "https://");
    }
    axios.delete(image.image_url).then(() => {
      this.getImageList();
    });
  }

  mounted() {
    this.getImageList();
  }

  getImageList() {
    axios
      .get(`${apiUrl}/images`)
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
</style>
