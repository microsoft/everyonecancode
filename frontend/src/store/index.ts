import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

import { imageApiUrl } from "../settings";

interface Image {
  image_url: string;
}

export const useGitHub = defineStore("github", {
  state: () => ({
    username: ref("CodeUnicornMartha"),
  }),
  actions: {
    setUsername(username: string) {
      this.username = username;
    },
  },
  persist: true,
});

export const useImages = defineStore("images", {
  state: () => ({
    imageList: ref([]),
  }),
  persist: true,
});

// export const useStore = defineStore("state", () => {
//   const imageList = ref([]);

//   const refreshImageList = () => {
//     axios
//       .get(`${imageApiUrl}images`)
//       .then((response) => {
//         imageList.value = response.data;
//       })
//       .catch((error) => {
//         imageList.value = [];
//         console.log(error);
//       });
//   };

//   const deleteImage = (image: Image) => {
//     axios.delete(`${imageApiUrl}${image.image_url}`).then(() => {
//       refreshImageList();
//     });
//   };

//   return {
//     githubUsername,
//     imageList,
//     refreshImageList,
//     deleteImage,
//   };
// });
// export default new Vuex.Store({
//   state: {
//     githubUsername: "CodeUnicornMartha",
//     imageList: [],
//   },
//   mutations: {
//     setGithubUsername(state, githubUsername) {
//       state.githubUsername = githubUsername;
//     },
//     setImageList(state, list) {
//       console.log(list);
//       state.imageList = list;
//     },
//   },
//   actions: {
//     refreshImageList(context) {
//       axios
//         .get(`${imageApiUrl}images`)
//         .then((response) => {
//           context.commit("setImageList", response.data);
//         })
//         .catch((error) => {
//           context.commit("setImageList", []);
//           console.log(error);
//         });
//     },
//     deleteImage(context, image) {
//       axios.delete(`${imageApiUrl}${image.image_url}`).then(() => {
//         context.dispatch("refreshImageList");
//       });
//     },
//   },
//   modules: {},
//   plugins: [vuexLocal.plugin],
// });
