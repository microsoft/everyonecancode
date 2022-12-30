import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Camera from "../views/Camera.vue";
import Microphone from "../views/Microphone.vue";
import FaceAI from "../views/FaceAI.vue";
import EditProfile from "../views/EditProfile.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/camera",
      name: "camera",
      component: Camera,
    },
    {
      path: "/microphone",
      name: "microphone",
      component: () => import("../views/Microphone.vue"),
    },
    {
      path: "/faceai",
      name: "faceai",
      component: FaceAI,
    },
    {
      path: "/editprofile",
      name: "editprofile",
      component: EditProfile,
    },
  ],
});

export default router;
