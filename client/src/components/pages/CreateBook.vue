<template>
    <v-container grid-list md>
        <v-layout row wrap align-center justify-center fill-height>
            <v-flex sm8 lg4>
                        <span class="headline">Login To Books</span>
                         <!--remove this shit-->
                        <!--<v-layout row fill-height justify-center align-center v-if="loading">
                            <v-progress-circular :size="50" color="primary" indeterminate/>
                        </v-layout>-->
                        <v-form ref="form" v-model="valid" lazy-validation>
                            <v-container>
                                <v-text-field v-model="book.name" :maxlength="100" label="Book Name" required/>
                                <v-text-field v-model="book.genre" :maxlength="50" label="Genre" required/>
                                <v-text-field v-model="book.author" :maxlength="50" label="Author" required/>
                                <v-text-field type="number" v-model="book.pages" label="Pages"/>
                                <v-text-field v-model="book.description" :counter="250" :maxlength="250" label="Description" required/>
                            </v-container>
                            <v-btn color="pink white--text" :disabled="!valid" @click="addbook">ADD</v-btn>
                        </v-form>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import axios from 'axios';
import router from "../../router";
export default {
  name: "Books",
  data: () => ({
        book: {},
        valid: true
  }),
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
        this.$session.start();
        axios.defaults.headers.common['Authorization'] = this.$session.get('token');
        xios.defaults.headers.post['Content-Type'] = 'application/json';
        if(!this.$session.has("token")){
            router.push('/auth');
        }
    },
    addbook(){
        axios.post('http://localhost:8000/api/books/', this.book).then(res =>{
                    router.push('/books/');
                }).catch(e => {
                    alert("Wrong Entries");
                })
    }
  }
};
</script>
