import { ref } from "vue";
import axiosClient from "../axios";

export default function usePosts() {
  const post = ref([]);
  const posts = ref([]);
  const postsCount = ref(0);
  const totalCount = ref(0);
  const currentPage = ref(1);
  const totalPages = ref(0);
  const pageSize = 6;

  const getPosts = async (pageNumber = 1) => {
    let response = await axiosClient.get(`/posts/?page=${pageNumber}`);
    posts.value = response.data.results;
    totalCount.value = response.data.count;
    currentPage.value = pageNumber;
    totalPages.value = Math.ceil(response.data.count / pageSize);
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
    totalCount,
    currentPage,
    totalPages,
    getPost,
    getPosts,
  };
}
