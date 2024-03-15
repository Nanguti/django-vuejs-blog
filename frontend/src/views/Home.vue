<template>
  <div>
    <DefaultLayout>
      <main class="mt-16 sm:mt-20 mb-16 sm:mb-20 relative">
        <img
          alt=""
          fetchpriority="high"
          width="2170"
          height="1494"
          decoding="async"
          data-nimg="1"
          class="hidden dark:sm:hidden sm:block absolute top-[-6.25rem] left-1/2 max-w-none w-[67.8125rem] ml-[-46.875rem] pointer-events-none"
          src="/showcase/beams@75.2e4c33d3.jpg"
          style="color: transparent"
        /><img
          alt=""
          fetchpriority="high"
          width="1318"
          height="1190"
          decoding="async"
          data-nimg="1"
          class="hidden dark:block absolute top-[-5rem] left-1/2 max-w-none w-[41.1875rem] ml-[-40rem] pointer-events-none"
          src="/showcase/beams-index-dark@75.8f02ce8a.jpg"
          style="color: transparent"
        />
        <div
          class="relative max-w-3xl px-4 sm:px-6 lg:px-8 mx-auto sm:text-center"
        >
          <h1 class="text-sm leading-6 font-semibold text-sky-500">
            Stay informed and engaged with our latest content.
          </h1>
        </div>
        <ul
          class="grid max-w-[26rem] sm:max-w-[52.5rem] mt-4 sm:mt-4 md:mt-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mx-auto gap-6 lg:gap-y-8 xl:gap-x-8 lg:max-w-7xl px-4 sm:px-6 lg:px-8"
        >
          <li
            v-for="post in posts"
            :key="post.id"
            @click="goToPostDetail(post.id)"
            class="group relative rounded-3xl bg-slate-50 p-6 dark:bg-slate-800/80 dark:highlight-white/5 hover:bg-slate-100 dark:hover:bg-slate-700/50"
          >
            <div
              class="aspect-[672/494] relative rounded-md transform overflow-hidden shadow-[0_2px_8px_rgba(15,23,42,0.08)] bg-slate-200 dark:bg-slate-700"
            >
              <img
                alt=""
                fetchpriority="high"
                width="672"
                height="494"
                decoding="async"
                data-nimg="1"
                class="absolute inset-0 w-full h-full"
                :src="post.thumbnail"
                style="color: transparent"
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
                {{ truncateText(post.content, 144) }}
              </p>
            </div>
          </li>
        </ul>
      </main>
    </DefaultLayout>
  </div>
</template>
<script setup>
import usePosts from "../composables/posts";
import { onMounted } from "vue";
import DefaultLayout from "../layouts/DefaultLayout.vue";
import { useRouter } from "vue-router";

const router = useRouter();

const { posts, getPosts } = usePosts();

onMounted(getPosts);

const truncateText = (text, maxLength) => {
  if (text.length <= maxLength) {
    return text;
  } else {
    return text.substring(0, maxLength) + "...";
  }
};

const goToPostDetail = (postId) => {
  router.push({ name: "postDetail", params: { id: postId } });
};
</script>
