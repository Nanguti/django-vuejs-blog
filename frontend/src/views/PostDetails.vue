<template>
  <DefaultLayout
    class="bg-gradient-to-r from-gray-100 via-[#bce1ff] to-gray-100"
  >
    <div class="overflow-hidden">
      <div class="max-w-8xl mx-auto">
        <div class="flex px-4 pt-8 pb-10 lg:px-8">
          <router-link
            class="group flex font-semibold text-sm leading-6 text-slate-700 hover:text-slate-900 dark:text-slate-200 dark:hover:text-white"
            to="/"
            ><svg
              viewBox="0 -9 3 24"
              class="overflow-visible mr-3 text-slate-400 w-auto h-6 group-hover:text-slate-600 dark:group-hover:text-slate-300"
            >
              <path
                d="M3 0L0 3L3 6"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              ></path>
            </svg>
            Go back
          </router-link>
        </div>
      </div>

      <div v-if="post">
        <div class="px-4 sm:px-6 md:px-8 pb-10">
          <div class="max-w-3xl mx-auto">
            <main>
              <article class="relative pt-10">
                <h1
                  class="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-slate-200 md:text-3xl"
                >
                  {{ post.title }}
                </h1>
                <div class="text-sm leading-6">
                  <dl>
                    <dt class="sr-only">Date</dt>
                    <dd
                      class="absolute top-0 inset-x-0 text-slate-700 dark:text-slate-400"
                    >
                      <time datetime="2024-03-06T16:30:00.000Z">{{
                        formatDate(post.published_date)
                      }}</time>
                    </dd>
                  </dl>
                </div>
                <div class="mt-6">
                  <ul class="flex flex-wrap text-sm leading-6 -mt-6 -mx-5">
                    <li
                      class="flex items-center font-medium whitespace-nowrap px-5 mt-6"
                    >
                      <img
                        :src="post.featured_image"
                        alt=""
                        class="mr-3 w-9 h-9 rounded-full bg-slate-50 dark:bg-slate-800"
                        decoding="async"
                      />
                      <div class="text-sm leading-4">
                        <div class="text-slate-900 dark:text-slate-200">
                          Author Name:{{ " " }} {{ post.author_name }}
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="mt-12 prose prose-slate dark:prose-dark">
                  <div
                    class="relative not-prose [a:not(:first-child)>&amp;]:mt-12 [a:not(:last-child)>&amp;]:mb-12 my-12 first:mt-0 last:mb-0 rounded-2xl overflow-hidden [figure>&amp;]:my-0"
                  >
                    <img
                      :src="post.featured_image"
                      alt="Tailwind CSS v4.0-alpha"
                      decoding="async"
                    />
                    <div
                      class="absolute inset-0 rounded-2xl ring-1 ring-inset ring-slate-900/10 dark:ring-white/10"
                    ></div>
                  </div>

                  <p>
                    {{ post.content }}
                  </p>
                </div>
              </article>
            </main>
            <footer class="mt-16">
              <div class="relative pb-28">
                <section
                  class="relative py-16 border-t border-slate-200 dark:border-slate-200/5"
                >
                  <h2
                    class="text-xl font-semibold text-slate-900 tracking-tight dark:text-white"
                  >
                    Get all of our updates directly to your&nbsp;inbox.<br />Sign
                    up for our newsletter.
                  </h2>
                  <div class="mt-5 max-w-md">
                    <form
                      action="https://app.convertkit.com/forms/3181881/subscriptions"
                      method="post"
                      class="flex flex-wrap -mx-2"
                    >
                      <div class="px-2 grow-[9999] basis-64 mt-3">
                        <div class="group relative">
                          <svg
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            aria-hidden="true"
                            class="w-6 h-full absolute inset-y-0 left-3 text-slate-400 pointer-events-none group-focus-within:text-sky-500 dark:group-focus-within:text-slate-400"
                          >
                            <path
                              d="M5 7.92C5 6.86 5.865 6 6.931 6h10.138C18.135 6 19 6.86 19 7.92v8.16c0 1.06-.865 1.92-1.931 1.92H6.931A1.926 1.926 0 0 1 5 16.08V7.92Z"
                            ></path>
                            <path d="m6 7 6 5 6-5"></path>
                          </svg>
                          <input
                            name="email_address"
                            type="email"
                            required=""
                            autocomplete="email"
                            aria-label="Email address"
                            class="appearance-none shadow rounded-md ring-1 ring-slate-900/5 leading-5 sm:text-sm border border-transparent py-2 placeholder:text-slate-400 pl-12 pr-3 block w-full text-slate-900 focus:outline-none focus:ring-2 focus:ring-sky-500 bg-white dark:bg-slate-700/20 dark:ring-slate-200/20 dark:focus:ring-sky-500 dark:text-white"
                            placeholder="Subscribe via email"
                          />
                        </div>
                      </div>
                      <div class="px-2 grow flex mt-3">
                        <button
                          type="submit"
                          class="bg-sky-500 flex-auto shadow text-white rounded-md text-sm border-y border-transparent py-2 font-semibold px-3 hover:bg-sky-600 dark:hover:bg-sky-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-300 dark:focus:ring-offset-slate-900 dark:focus:ring-sky-700"
                        >
                          Subscribe
                        </button>
                      </div>
                    </form>
                  </div>
                </section>
              </div>
            </footer>
          </div>
        </div>
      </div>
    </div>
    <a
      href="#"
      target="_blank"
      class="md:absolute top-20 right-10 p-4 float-right"
      ><img
        src="https://www.buymeacoffee.com/assets/img/guidelines/logo-mark-3.svg"
        alt="Buy Me A Coffee"
        class="transition-all rounded-full w-14 -rotate-45 hover:shadow-sm shadow-lg ring hover:ring-4 ring-white"
    /></a>
  </DefaultLayout>
</template>

<script setup>
import usePosts from "../composables/posts";
import DefaultLayout from "../layouts/DefaultLayout.vue";
import { onMounted } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
const { post, getPost } = usePosts();
onMounted(() => {
  const postId = router.currentRoute.value.params.id;
  getPost(postId);
});

const formatDate = (dateString) => {
  const options = {
    weekday: "long",
    month: "long",
    day: "numeric",
    year: "numeric",
  };
  const date = new Date(dateString);
  return date.toLocaleDateString("en-US", options);
};
</script>
