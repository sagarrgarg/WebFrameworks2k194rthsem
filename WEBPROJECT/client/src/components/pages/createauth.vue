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
                                <!--<input type="text" v-model="credentials.username" maxlength="70" required placeholder="Email address">
                                <input type="password" v-model="credentials.password" maxlength="20" required placeholder="Password">-->
                                <v-text-field v-model="credentials.username" :maxlength="70" label="Email address" required/>
                                <v-text-field type="password" v-model="credentials.password" :maxlength="20" label="Password" required/>
                            </v-container>
                            <v-btn color="pink white--text" :disabled="!valid" @click="login">Login</v-btn><v-btn color="pink white--text" @click="createone">Create Id</v-btn>
                        </v-form>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import router from '../../router';
export default {
    name: 'Auth',
    data: () => ({
        credentials: {},
        valid:true,
        //loading:false
    }),

    methods:{
        login(){
            if(this.$refs.form.validate()){
          //      this.loading=true;
                axios.post('http://localhost:8000/auth/', this.credentials).then(res =>{
                    this.$session.start();
                    this.$session.set('token',res.data.token);
                    router.push('/books');
                }).catch(e => {
                    alert("Wrong username/passwrod!");
                    alert(credentials);
                })
            }
        }
    }
}
</script>
