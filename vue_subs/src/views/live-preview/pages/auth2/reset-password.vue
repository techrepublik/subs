<script>
import Rightbar from "@/components/right-bar.vue"

export default {
    name: "RESET-PASSWORD",
    components: {
        Rightbar
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
                        <h4 class="f-w-500 mb-1">Reset password</h4>
                        <p class="mb-3">Back to <router-link to="/login-v2" class="link-primary">Log in</router-link></p>
                        <div class="mb-3">
                            <label class="form-label">Password</label>
                            <input type="password" class="form-control" id="floatingInput" placeholder="Password">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Confirm Password</label>
                            <input type="password" class="form-control" id="floatingInput1" placeholder="Confirm Password">
                        </div>
                        <div class="d-grid mt-4">
                            <button type="button" class="btn btn-primary">Reset Password</button>
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