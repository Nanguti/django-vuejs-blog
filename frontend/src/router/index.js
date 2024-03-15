import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import PostDetails from "../views/PostDetails.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/post/:id",
    name: "postDetail",
    component: PostDetails,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
