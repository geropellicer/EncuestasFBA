<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="encuesta in encuestas"
           :key="encuesta.id">

            <div class="card w-100">
              <div class="card-body">
                <h5 class="card-title">{{ encuesta.texto }}</h5>
                
                <div v-if="encuesta">
                    <router-link :to="{ name: 'encuesta', params: { id: encuesta.id }}">Ver detalles</router-link>
                </div>
                
              </div>
            </div>

        <h2>
          
        </h2>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...cargando...</p>
        <button
          v-show="next"
          @click="getEncuestas"
          class="btn btn-sm btn-outline-success"
          >Cargar mas
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      encuestas: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getEncuestas() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/encuestas/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
          this.encuestas.push(...data.results)
          this.loadingQuestions = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    }
  },
  created() {
    this.getEncuestas()
    document.title = "Encuestas FBA";
  }
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #DC3545;
}

.question-link {
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343A40;
  text-decoration: none;
}
</style>
