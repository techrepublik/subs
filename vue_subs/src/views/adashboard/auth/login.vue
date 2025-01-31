<script>
import Rightbar from "@/components/right-bar.vue"
import { useAuthStore } from "@/stores/auth";
import { useRouter } from 'vue-router';
import { ref } from 'vue'; // Import `ref` for reactive variables

export default {
    name: "ALOGIN",
    components: {
        Rightbar
    },
    setup() {
        const email = ref('');
        const password = ref('');
        const errorMessage = ref('');
        const isLoading = ref(false);
        const authStore = useAuthStore();
        const router = useRouter();

        const handleLogin = async () => {
        if (!email.value || !password.value) {
            errorMessage.value = 'Email and password are required.';
            return;
        }

        isLoading.value = true;
        try {
            await authStore.login({ email: email.value, password: password.value });
            router.push('/subscription-plans');
        } catch (error) {
            errorMessage.value = 'Invalid email or password. Please try again.';
        } finally {
            isLoading.value = false;
        }
        };

        // Return all variables and functions to make them accessible in the template
        return {
            email,
            password,
            errorMessage,
            isLoading,
            handleLogin,
        };
    },
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
                        <h4 class="f-w-500 mb-1">Login with your email</h4>
                        <p class="mb-3">Don't have an Account? <router-link to="/aregister"
                                class="link-primary ms-1">Create Account</router-link></p>
                        
                        <form @submit.prevent="handleLogin">
                            <div class="mb-3">
                                <input v-model="email" type="email" class="form-control" id="floatingInput" placeholder="Email Address">
                            </div>
                            <div class="mb-3">
                                <input v-model="password" type="password" class="form-control" id="floatingInput1" placeholder="Password">
                            </div>
                            <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
                            <div class="d-flex mt-1 justify-content-between align-items-center">
                                <div class="form-check">
                                    <input class="form-check-input input-primary" type="checkbox" id="customCheckc1" checked="">
                                    <label class="form-check-label text-muted" for="customCheckc1">Remember me?</label>
                                </div>
                                <router-link to="/forgot-password-v2">
                                    <h6 class="text-secondary f-w-400 mb-0">Forgot Password?</h6>
                                </router-link>
                            </div>
                            <div class="d-grid mt-4">
                                <button type="submit" :disabled="isLoading" class="btn btn-primary">
                                    <span v-if="isLoading">Logging in...</span>
                                    <span v-else>Login</span>    
                                </button>
                            </div>
                        </form>

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