<template>
    <div>
    <!--<span class="headline">Books</span>-->
    <template>
  <v-layout row>
    <v-flex>
      <v-card>
        <v-toolbar color="pink" dark>

          <v-toolbar-title>Books</v-toolbar-title>
                   <v-spacer></v-spacer>

          <v-btn @click="createbook" color="pink white--text">
            Publish a Book
          </v-btn>
          <v-btn @click="logout" color="pink white--text">
            Logout
          </v-btn>
        </v-toolbar>

        <v-list three-line>
          <template v-for="book in books">
            <v-list-tile
              :key="book.name"
              avatar
              ripple
              @click="toggle(book.id)"
            >
              <v-list-tile-content>
                <v-list-tile-title>{{ book.name }}</v-list-tile-title>
                <v-list-tile-sub-title class="text--primary">{{ book.description }}</v-list-tile-sub-title>
                <v-list-tile-sub-title>{{ book.author }}</v-list-tile-sub-title>
                <v-list-tile-sub-title>{{ book.pages }}</v-list-tile-sub-title>
              </v-list-tile-content>

            </v-list-tile>
          </template>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>
    <!--<ul id="books">
        <li v-for = "book in books">
            <ul>
                <li>ID : {{book.id}}</li>
                <li>Name : {{book.name}}</li>
                <li>Author : {{book.author}}</li>
                <li>Genre : {{book.genre}}</li>
                <li>Pages : {{book.pages}}</li>
                <li>Description :{{book.description}}</li>
            </ul>
        </li>
    </ul>-->
    </div> 
</template>

<script>
import axios from 'axios';
import router from "../../router";
import Vue from 'vue';
export default {
  name: "Books",
  data: () => ({
      list:[],
      books:[]
  }),  
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
        this.$session.start();
        if(!this.$session.has("token")){
            router.push('/');
        }
        else{
            axios.get("http://localhost:8000/api/books/").then(res =>{
                // this.books = [res.data[0]];
                for(var i=0;i<2;i++){
                   this.books.push(res.data[i]);
                }
                console.log(this.books);
            });
        }
    },
    createbook(){
        router.push('/createbook');
    },
    logout(){
        this.$session.remove('token');
        router.push('/');
    }
  }
};
            // <v-divider
            //   v-if=" + 1 < items.length"
            //   :key="index"
            // ></v-divider>
</script>
