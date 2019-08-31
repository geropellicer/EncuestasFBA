<template>
  <div class="home">
    <div class="container mt-2">

              <div id="carrusel" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li v-for="pregunta in preguntas" :key="pregunta.codigo" data-target="#carrusel" :data-slide-to="pregunta.codigo" class="active"></li>
            </ol>
            <div class="carousel-inner">
              <div v-for="pregunta in preguntas" :key="pregunta.codigo" v-bind:class="{ active: pregunta.codigo == 1 }" class="carousel-item card bg-light mb-3">
                <div class="card-header">Pregunta {{ pregunta.codigo }} de {{ preguntas.length }}</div>
                <div class="card-body">
                  <h5 class="card-title">{{ pregunta.texto }}</h5>
                  <p class="card-text">{{ pregunta.descripcion }}</p>

                    <div class="btn-group btn-group-toggle" data-toggle="buttons">
                      <label v-for="respuesta in pregunta.respuestas" :key="respuesta.codigo" class="btn btn-secondary">
                        <input type="radio" :name="pregunta" :id="respuesta.codigo" autocomplete="off"> {{respuesta.texto}}
                      </label>
                    </div>

                </div>
              </div>
            </div>
            <a class="carousel-control-prev" href="#carrusel" role="button" data-slide="prev" style="margin-left: -15%">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carrusel" role="button" data-slide="next" style="margin-right: -15%">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
          
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "encuestadetalle",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      encuesta: {},
      preguntas: [],
      next: null,
      loadingQuestions: false,
    }
  },
  methods: {
      onSubmit: function(id){
      // Mandamos a la base
            if (this.fechaTurno && this.horarioTurno) {
            let endpoint = `/apic/alquileres/`;
            let datetime = this.fechaTurno + 'T' + this.horarioTurno;
            this.fechahorarioTurno = datetime;
            apiService(endpoint, "POST", { turno_desde: datetime,
                                            turno_hasta: datetime,
                                            cancha: this.cancha.id,
                                            cliente: this.clienteSend,
                                            empleado: this.empleadoSend,})
                .then(data => {
                this.alquileres.unshift(data)
                })
            if (this.error) {
                this.error = null;
            }
            } else {
                this.error = "You can't send an empty answer!";
            }

                this.fechaTurno = '';
                this.horarioTurno = '';
                this.canchaAlquilandoSend = '';
                this.clienteSend = '';
                this.empleadoSend = '';
                this.fechahorarioTurno = '';
                this.alquilando = false;

      },
        cerrarFormulario: function(){
        this.alquilando = false;
        this.alquilandoNum = 0;
        },

    getEncuestaDetalles() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/encuestas/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.encuesta = data;
            this.preguntas = data.preguntas
            this.setPageTitle(data.texto)
          } else {
            this.encuesta = null;
            this.setPageTitle("404 - Error")
          }

        })
    },
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    async eliminarAlquiler(id, alquiler) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/apic/alquileres/${id}/`;
      try {
        await apiService(endpoint, "DELETE");
        let conseguidor = id;
        var index = this.alquileres.indexOf(alquiler);
        if (index !== -1) this.alquileres.splice(index, 1);
      }
      catch (err) {
        console.log(err)
      }
    },
    alquilar(id){
        this.alquilando = true;
        this.alquilandoNum = id;
    }
  },
  created() {
    this.getEncuestaDetalles()
    document.title = "Encuestas APP";
  }, 
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
