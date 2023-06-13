<template>
  <div>
    <div class="tile is-ancestor" style="margin-bottom: 100px">
      <div class="tile is-parent is-vertical">
        <div
          class="tile is-child"
          v-for="image in imageList"
          :key="image.image_url"
        >
          <b-image ratio="1by1  " :src="`${apiUrl}${image.image_url}`" />
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
import store from "../store/index";
import { imageApiUrl } from "../settings";

@Component({ store: store })
export default class ImageList extends Vue {
  readonly apiUrl = imageApiUrl;

  get imageList() {
    return this.$store.state.imageList;
  }

  deleteImage(image: any) {
    this.$store.dispatch("deleteImage", image);
  }

  mounted() {
    this.$store.dispatch("refreshImageList");
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#btn-delete {
  margin-top: 5px;
}
</style>
