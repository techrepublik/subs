<script>
import Rightbar from "@/components/right-bar.vue"
import axios from "axios";
import Swal from "sweetalert2";

export default {
    name: "AREGISTER",
    components: {
        Rightbar
    },
    data() {
        return {
            user: {
                first_name: "",
                last_name: "",
                email: "",
                user_type: "employee",
                password1: "",
                password2: "",
            }
        }
    },
    methods:{
        addUser() {
            axios.post("/api/v1/users/", {
                first_name: this.user.first_name,
                last_name: this.user.last_name,
                email: this.user.email,
                user_type: this.user.user_type,
                password1: this.user.password1,
                password2: this.user.password2,
            }).then((respose) => {
                console.log(respose.data)
                Swal.fire({
                    position: "top-end",
                    icon: "success",
                    title: "Your work has been saved",
                    showConfirmButton: false,
                    timer: 1500,
                });
                this.$router.push("/alogin");
            })
        }
    }
}
</script>

<template>
    <div class="auth-main v2">
        <div class="bg-overlay bg-dark"></div>
        <div class="auth-wrapper">
            <div class="auth-sidecontent">

                <div class="auth-sidefooter">
                    <img src="@/assets/images/logo-white.svg" class="img-brand img-fluid" alt="images">
                    <hr class="mb-3 mt-4">
                    <BRow class="row">
                        <BCol class="col my-1">
                            <p class="m-0">Light Able ♥ crafted by Team <a href="#"
                                    target="_blank"> themes</a></p>
                        </BCol>
                        <BCol class="col-auto my-1">
                            <ul class="list-inline footer-link mb-0">
                                <li class="list-inline-item"><router-link to="/dashboard">Home</router-link></li>
                                <li class="list-inline-item"><a href="#"
                                        target="_blank">Documentation</a></li>
                                <li class="list-inline-item"><a href="#"
                                        target="_blank">Support</a></li>
                            </ul>
                        </BCol>
                    </BRow>
                </div>
            </div>
            <div class="auth-form">
                <div class="card my-5 mx-3">
                    <div class="card-body">
                        <h4 class="f-w-500 mb-1">Register with your email</h4>
                        <p class="mb-3">Already have an Account? <router-link to="/alogin" class="link-primary">Log
                                in</router-link></p>
                        <BRow class="row">
                            <BCol class="col-sm-6">
                                <div class="mb-3">
                                    <input v-model="user.first_name" type="text" class="form-control" placeholder="First Name">
                                </div>
                            </BCol>
                            <BCol class="col-sm-6">
                                <div class="mb-3">
                                    <input v-model="user.last_name" type="text" class="form-control" placeholder="Last Name">
                                </div>
                            </BCol>
                        </BRow>
                        <div class="mb-3">
                            <input v-model="user.email" type="email" class="form-control" placeholder="Email Address">
                        </div>
                        <div class="mb-3">
                            <input v-model="user.user_type" type="user_type" class="form-control" placeholder="User type">
                        </div>
                        <div class="mb-3">
                            <input v-model="user.password1" type="password" class="form-control" placeholder="Password">
                        </div>
                        <div class="mb-3">
                            <input v-model="user.password2" type="password" class="form-control" placeholder="Confirm Password">
                        </div>
                        <div class="d-flex mt-1 justify-content-between">
                            <div class="form-check">
                                <input class="form-check-input input-primary" type="checkbox" id="customCheckc1" checked="">
                                <label class="form-check-label text-muted" for="customCheckc1">I agree to all the Terms &
                                    Condition</label>
                            </div>
                        </div>
                        <div class="d-grid mt-4">
                            <button @click="addUser" type="button" class="btn btn-primary">Create Account</button>
                        </div>
                        <div class="saprator my-3">
                            <span>Or continue with</span>
                        </div>
                        <div class="text-center">
                            <ul class="list-inline mx-auto mt-3 mb-0">
                                <li class="list-inline-item">
                                    <a href="https://www.facebook.com/" class="avtar avtar-s rounded-circle bg-facebook"
                                        target="_blank">
                                        <i class="fab fa-facebook-f text-white"></i>
                                    </a>
                                </li>
                                <li class="list-inline-item">
                                    <a href="https://twitter.com/" class="avtar avtar-s rounded-circle bg-twitter"
                                        target="_blank">
                                        <i class="fab fa-twitter text-white"></i>
                                    </a>
                                </li>
                                <li class="list-inline-item">
                                    <a href="https://myaccount.google.com/"
                                        class="avtar avtar-s rounded-circle bg-googleplus" target="_blank">
                                        <i class="fab fa-google text-white"></i>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Rightbar />
</template>