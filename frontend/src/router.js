import Vue from "vue";
import Router from "vue-router";
import EncuestaDetalle from "./views/EncuestaDetalle.vue";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/logout/",
      name: "logout",
    },
    {
      path: "/encuesta/:id",
      name: "encuesta",
      component: EncuestaDetalle,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound
    }
  ]
});
