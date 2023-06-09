<template>
  <div>
  <h1>Краткое содержание текста</h1>
  <br>
  <div class="full-width-div">
    <b-form @submit.prevent="onSubmit">
    <b-form-group
              label="Введите текст, который нужно сократить:"
              label-for="input-1"
          >
    <b-form-input id="input-1" v-model="text" placeholder="Начинайте вводить текст..."></b-form-input>
    </b-form-group>
      <b-button type="submit" variant="primary">Отправить</b-button>
    </b-form>
  </div>

  <br>
  <div>
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
  import {getSummurytext} from "./services/api";
  import TextCardView from "./components/TextCardView.vue";

  export default {
    components: {TextCardView},
    data() {
      return {
        text: '',
        results_first: '',
        results_second: '',
        results_third: ''
      }
    },
    methods: {
      async onSubmit() {
        this.results_first = await getSummurytext(1, this.text)
        this.results_second = await getSummurytext(2, this.text)
        this.results_third = await getSummurytext(3, this.text)
      }
    }
  }
</script>

<style scoped>
  .full-width-div {
  width: 100%;
  margin: 0;
  padding: 0;
}
</style>