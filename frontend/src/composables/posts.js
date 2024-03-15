import { ref } from "vue";
import axiosClient from "../axios";

export default function usePosts() {
  const post = ref([]);
  const posts = ref([]);
  const postsCount = ref([]);

  const getPosts = async () => {
    let response = await axiosClient.get("/posts");
    posts.value = response.data;
  };

  const getPost = async (id) => {
    let response = await axiosClient.get(`/posts/${id}`);
    console.log("log response.. data " + response.data.title);
    post.value = response.data;
  };

  return {
    post,
    posts,
    postsCount,
    getPost,
    getPosts,
  };
}
