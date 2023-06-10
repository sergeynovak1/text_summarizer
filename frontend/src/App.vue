<template>

  <div className="main">
    <h1>Краткое содержание текста</h1>
    <br>
    <div className="full-width-div">
      <b-form @submit.prevent="onSubmit">
        <b-form-group className="h4"
                      label="Введите ссылку на статью википедии, которую нужно сократить:"
                      label-for="input-1"
        >
          <b-form-input className="custom-input w-100" id="input" v-model="link"
                           placeholder="https://ru.wikipedia.org/..."></b-form-input>
        </b-form-group>
        <br>
        <b-form-group className="custom-label"
                      label="Введите текст, который нужно сократить:"
                      label-for="input-1"
        >
          <b-form-textarea className="custom-input autosize w-100" id="input-1" v-model="text"
                           placeholder="Начинайте вводить текст..."></b-form-textarea>
        </b-form-group>
        <b-button style="margin: 10px" type="submit" variant="primary">Отправить</b-button>

        <b-button @click="this.text=''" type="submit" variant="primary">Стереть</b-button>
      </b-form>
    </div>

    <br>
    <div>
      <b-spinner v-if="this.loading"></b-spinner>
      <b-row>
        <b-col>
          <TextCardView :text="this.results_first" :title="'Частотный анализ'"/>
        </b-col>
        <b-col>
          <TextCardView :text="this.results_second" :title="'Косинусное расстояние'"/>
        </b-col>
        <b-col>
          <TextCardView :text="this.results_third" :title="'TF IDF'"/>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import {getSummurytext, getText} from "./services/api";
import TextCardView from "./components/TextCardView.vue";
import autosize from "autosize/dist/autosize";

export default {
  components: {TextCardView},
  mounted() {
    autosize(document.querySelectorAll('.autosize'));
  },
  data() {
    return {
      loading: false,
      link: '',
      text: '',
      results_first: '',
      results_second: '',
      results_third: ''
    }
  },
  methods: {
    async onSubmit() {
      if (this.link) {
        this.text = await getText(this.link)
      }
      if (this.text) {
        this.loading = true
        this.results_first = await getSummurytext(1, this.text)
        this.results_second = await getSummurytext(2, this.text)
        this.results_third = await getSummurytext(3, this.text)
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
html,
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}


.full-width-div {
  width: 100%;
}


.main {
  width: 95%;
  margin-left: 1rem;
}
</style>