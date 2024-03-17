<!-- views/Home.vue -->
<template>
  <div>
    <DefaultLayout
      class="bg-gradient-to-r from-gray-100 via-[#bce1ff] to-gray-100"
    >
      <main class="mt-16 sm:mt-20 mb-16 sm:mb-20 relative">
        <div class="max-w-6xl mx-auto">
          <SearchBar @goToSearchResults="handleSearch" />
          <ul
            class="grid max-w-[26rem] sm:max-w-[52.5rem] mt-4 sm:mt-4 md:mt-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 mx-auto gap-6 lg:gap-y-8 xl:gap-x-8 lg:max-w-7xl px-4 sm:px-6 lg:px-8 mb-8"
          >
            <li
              v-for="post in posts"
              :key="post.id"
              @click="goToPostDetail(post.id)"
              class="group relative rounded-md bg-slate-50 p-6 dark:bg-slate-800/80 dark:highlight-white/5 hover:bg-slate-100 dark:hover:bg-slate-700/50"
            >
              <div
                class="aspect-[672/494] relative rounded-md transform overflow-hidden shadow-[0_2px_8px_rgba(15,23,42,0.08)] bg-slate-200 dark:bg-slate-700"
              >
                <img
                  alt=""
                  fetchpriority="high"
                  decoding="async"
                  data-nimg="1"
                  class="absolute inset-0 w-full h-full object-cover"
                  :src="post.thumbnail"
                  style="color: transprent"
                />
              </div>
              <div class="flex flex-wrap items-center mt-6">
                <h2
                  class="text-sm leading-6 text-slate-900 dark:text-white font-semibold group-hover:text-sky-500 dark:group-hover:text-sky-400"
                >
                  <router-link
                    :to="{ name: 'postDetail', params: { id: post.id } }"
                  >
                    <span class="absolute inset-0 rounded-3xl"></span>
                    {{ post.title }}
                  </router-link>
                </h2>
                <svg
                  class="w-6 h-6 flex-none opacity-0 group-hover:opacity-100"
                  viewBox="0 0 24 24"
                  fill="none"
                >
                  <path
                    d="M9.75 15.25L15.25 9.75M15.25 9.75H10.85M15.25 9.75V14.15"
                    stroke="#0EA5E9"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  ></path>
                </svg>
                <p
                  class="w-full flex-none text-[0.8125rem] leading-6 text-slate-500 dark:text-slate-400"
                >
                  {{ truncateContent(post.content) }}
                </p>
              </div>
            </li>
          </ul>
          <Pagination
            :totalCount="totalCount"
            :currentPage="currentPage"
            :totalPages="totalPages"
            @goToPage="getPosts"
          />
        </div>
      </main>
      <a
        href="#"
        target="_blank"
        class="md:absolute bottom-0 right-0 p-4 float-right"
        ><img
          src="https://www.buymeacoffee.com/assets/img/guidelines/logo-mark-3.svg"
          alt="Buy Me A Coffee"
          class="transition-all rounded-full w-14 -rotate-45 hover:shadow-sm shadow-lg ring hover:ring-4 ring-white"
      /></a>
    </DefaultLayout>
  </div>
</template>
<script setup>
import usePosts from "../composables/posts";
import { onMounted } from "vue";
import DefaultLayout from "../layouts/DefaultLayout.vue";
import Pagination from "../components/Pagination.vue";
import { useRouter } from "vue-router";
import SearchBar from "../components/SearchBar.vue";

const router = useRouter();
const { posts, totalCount, currentPage, totalPages, getPosts, searchPosts } =
  usePosts();

onMounted(getPosts);

const goToPostDetail = (postId) => {
  router.push({ name: "postDetail", params: { id: postId } });
};
const truncateContent = (content) => {
  if (content.length > 144) {
    return content.slice(0, 144) + "...";
  } else {
    return content;
  }
};
const handleSearch = async (searchQuery) => {
  try {
    await searchPosts(searchQuery.value);
    console.log("Search results updated");
  } catch (error) {
    console.error("Error searching posts:", error);
  }
};
</script>
