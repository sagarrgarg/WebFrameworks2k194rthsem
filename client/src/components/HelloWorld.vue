<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        ></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Books
        </h1>
      </v-flex>

      <v-flex
        mb-5
        xs12
      >
        <h2 class="headline font-weight-bold mb-3">Login Page</h2>

        <v-layout justify-center>
           <v-btn color="pink white--text" @click="LogIn">Login</v-btn>
        </v-layout>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import router from '../router';
  export default {
    name: "Books",
  methods: {
    LogIn() {
        this.$session.start();
        if(!this.$session.has("token")){
            router.push('/auth');
        }
        else{
          router.push('/books')
        }
    }
  }
  }
</script>

<style>

</style>
