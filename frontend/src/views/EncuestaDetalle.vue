<template>
  <div class="home">
    <div class="container mt-2">

              <div id="carrusel" class="carousel slide mt-5" data-ride="carousel">
            <div class="carousel-inner" style="box-shadow: 0 0 15px 2px rgba(0,0,0,.5)">
              <div v-for="pregunta in preguntas" :key="pregunta.codigo" v-bind:class="{ active: pregunta.codigo == 1 }" class="carousel-item card bg-light">
                <div class="card-header">Pregunta {{ pregunta.codigo }} de {{ preguntas.length }}</div>
                <div class="card-body">
                  <h5 class="card-title">{{ pregunta.texto }}</h5>
                  <p class="card-text">{{ pregunta.descripcion }}</p>

                  <div style="display: flex; justify-content: center; flex-direction: column, align-items: center; width: 100%" class="my-5">
                    <div class="btn-group btn-group-toggle" data-toggle="buttons">
                      <label v-for="respuesta in pregunta.respuestas" :key="respuesta.codigo" class="btn btn-lg btn-secondary p-4">
                        <input type="radio" :name="pregunta.id" :id="respuesta.codigo" :pk="respuesta.id" :codRes="respuesta.codigo" :pkPreg="pregunta.id" :codPreg="pregunta.codigo" autocomplete="off"> {{respuesta.texto}}
                      </label>
                    </div>
                  </div>

                    <button @click="anteriorPregunta" v-if="pregunta.codigo != 1" type="button" class="btn btn-secondary btn-lg float-left mb-3">Anterior</button>
                    <button @click="siguientePregunta" v-if="pregunta.codigo != preguntas.length" type="button" class="btn btn-primary btn-lg float-right mb-3">Siguiente</button>
                    <button v-if="pregunta.codigo == preguntas.length" type="button" class="btn btn-primary btn-lg float-right mb-3" data-toggle="modal" data-target="#exampleModalCenter">Enviar</button>

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
<!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLongTitle">Confirmar</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Enviar respuestas? Esto no se puede deshacer!
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
        <button @click="enviarRespuestas" type="button" class="btn btn-primary">Confirmar</button>
      </div>
    </div>
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
      respuestas: [],
    }
  },
  methods: {
    enviarRespuestas: function(){
      var entradasEnviadas = 0;

      if($('label.active > input').length < this.preguntas.length){
        window.alert("Hay preguntas vacias!");
        return false;
      }

      $('label.active > input').each(function(i, el){
        let pkResp = $(el).attr('pk');
        let codResp = $(el).attr('codRes');
        let pkPreg = $(el).attr('pkPreg');
        let codPreg = $(el).attr('codPreg');
        console.log(pkResp + ' ' + codResp + ' ' + pkPreg + ' ' + codPreg);
        
          if (pkResp && pkPreg) {
          let endpoint = `/api/entradas/`;
          apiService(endpoint, "POST", { pk_pregunta: pkPreg,
                                          pk_respuesta  : pkResp,
                                          cod_pregunta: codPreg,
                                          cod_respuesta: codResp
                                        })
              .then(data => {
                  console.log("Respuesta creada con exito" + i);
                  entradasEnviadas += 1;
                  if(entradasEnviadas == $('label.active > input').length){
                    console.log("LISTO!")
                     location.reload();
                  }
              })
          if (this.error) {
              this.error = null;
          }
          } else {
              this.error = "You can't send an empty answer!";
          }
        
      });
    },
    siguientePregunta: function(){
      $('#carrusel').carousel('next');
    },
    anteriorPregunta: function(){
      $('#carrusel').carousel('prev');
    },
    getEncuestaDetalles() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/encuestas/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.encuesta = data;
            this.preguntas = data.preguntas
            for(let i = 0; i<preguntas.length; i++) {
              let pkPregunta = data.preguntas.i.id;
              let entrada = {pk: 0};
              this.respuestas.push(entrada)
            };
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
    this.getEncuestaDetalles();
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
.btn.btn-lg.btn-secondary.p-4.active {
  background-color: green;
}
</style>
