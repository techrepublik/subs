<template>
    <Layout>
        <pageheader title="Notifications" pageTitle="Online Courses" />
        <!-- Your template content here -->

        <!-- [ Main Content ] start -->
        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <h5 class="mb-0">Payment</h5>
                    </div>
                    <div class="card-body">
                        <ul class="nav nav-tabs d-none" id="myTab" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" id="auth-tab-1" data-bs-toggle="tab" @click="changeTab('#auth-1')" href="#auth-1" role="tab" data-slide-index="1" aria-controls="auth-1" aria-selected="true">
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="auth-tab-2" data-bs-toggle="tab" @click="changeTab('#auth-2')" href="#auth-2" role="tab" data-slide-index="2" aria-controls="auth-2" aria-selected="true">
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="auth-tab-3" data-bs-toggle="tab" @click="changeTab('#auth-3')" href="#auth-3" role="tab" data-slide-index="3" aria-controls="auth-3" aria-selected="true">
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="auth-tab-4" data-bs-toggle="tab" @click="changeTab('#auth-4')" href="#auth-4" role="tab" data-slide-index="4" aria-controls="auth-4" aria-selected="true">
                                </a>
                            </li>
                        </ul>
                        <div class="tab-content">
                            <div class="tab-pane show active" id="auth-1" role="tabpanel" aria-labelledby="auth-tab-1">
                                <div class="row justify-content-center">
                                    <div class="col-md-10 col-lg-8 col-xxl-6">
                                        <div class="card border text-center">
                                            <div class="card-body">
                                                <img src="@/assets/images/admin/img-payment-1.png" alt="images" class="img-fluid mb-4">
                                                <h5>Establish your payment gateway</h5>
                                                <p class="text-muted">Able Pro: pay streamlines your payout process, facilitating faster payments while managing author and affiliate payouts on your behalf.</p>
                                                <div class="mb-3 text-start">
                                                    <label class="form-label">Mobile Phone</label>
                                                    <div class="d-flex align-items-center">
                                                        <div class="flex-grow-1 me-3">
                                                            <div class="input-group">
                                                                <span class="input-group-text">+91</span>
                                                                <input type="text" class="form-control" placeholder="https://admin123-20">
                                                            </div>
                                                        </div>
                                                        <div class="flex-shrink-0">
                                                            <button class="btn btn-primary" @click="changeTab('#auth-2')">Confirm</button>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane" id="auth-2" role="tabpanel" aria-labelledby="auth-tab-2">
                                <button class="btn btn-link-secondary d-flex align-items-center" @click="changeTab('#auth-1')"><i class="ti ti-chevron-left"></i> Back Step</button>
                                <div class="row justify-content-center">
                                    <div class="col-md-10 col-lg-8 col-xxl-6">
                                        <div class="card border text-center">
                                            <div class="card-body">
                                                <img src="@/assets/images/admin/img-payment-1.png" alt="images" class="img-fluid mb-4">
                                                <h5>Let's begin from the start</h5>
                                                <p class="text-muted">What is your current tax filing situation?</p>
                                                <div class="row g-3 justify-content-center">
                                                    <div class="col-auto">
                                                        <button class="btn btn-primary" @click="changeTab('#auth-3')">Confirm</button>
                                                    </div>
                                                    <div class="col-auto">
                                                        <button class="btn btn-primary" @click="changeTab('#auth-3')">Confirm</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane" id="auth-3" role="tabpanel" aria-labelledby="auth-tab-3">
                                <button class="btn btn-link-secondary d-flex align-items-center" @click="changeTab('#auth-2')"><i class="ti ti-chevron-left"></i> Back Step</button>
                                <div class="row justify-content-center">
                                    <div class="col-md-10 col-lg-8 col-xxl-6">
                                        <div class="card border text-center">
                                            <div class="card-body">
                                                <img src="@/assets/images/admin/img-payment-2.png" alt="images" class="img-fluid mb-4">
                                                <h5 class="mb-4">Inform us about your enterprise</h5>
                                                <div class="row justify-content-center text-start">
                                                    <div class="col-sm-10 col-md-8 col-xxl-6">
                                                        <div class="mb-3">
                                                            <label class="form-label">What is your current tax filing situation?</label>
                                                            <select class="form-select">
                                                                <option selected>LLC</option>
                                                                <option value="1">LLC 1</option>
                                                                <option value="2">LLC 2</option>
                                                                <option value="3">LLC 3</option>
                                                            </select>
                                                        </div>
                                                        <div class="mb-3">
                                                            <label class="form-label">What were your total sales for the previous year?</label>
                                                            <select class="form-select">
                                                                <option selected>$100-$1000</option>
                                                                <option value="1">$101-$2000</option>
                                                                <option value="2">$2001-$3000</option>
                                                                <option value="3">$3001-$4000</option>
                                                            </select>
                                                        </div>
                                                        <div class="mb-3">
                                                            <label class="form-label">What is your business name?</label>
                                                            <input type="email" class="form-control" placeholder="Business name">
                                                        </div>
                                                    </div>
                                                </div>
                                                <button class="btn btn-primary" @click="changeTab('#auth-4')">Confirm</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane" id="auth-4" role="tabpanel" aria-labelledby="auth-tab-4">
                                <button class="btn btn-link-secondary d-flex align-items-center" @click="changeTab('#auth-3')"><i class="ti ti-chevron-left"></i> Back Step</button>
                                <div class="row justify-content-center">
                                    <div class="col-md-10 col-lg-8 col-xxl-6">
                                        <div class="card border text-center">
                                            <div class="card-body">
                                                <img src="@/assets/images/admin/img-payment-2.png" alt="images" class="img-fluid mb-4">
                                                <h5 class="mb-2">Inform us about your enterprise</h5>
                                                <p class="text-muted mb-4">What is your current tax filing situation?</p>
                                                <button class="btn btn-primary">Confirm</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
</template>

<script>
import Layout from "@/layout/main.vue";
import pageheader from "@/components/page-header.vue";
import { Tab } from 'bootstrap'; // Import the Tab module from Bootstrap

export default {
    name: "Notifications",
    components: {
        Layout,
        pageheader
    },
    methods: {
        changeTab(tab_name) {
            const someTabTriggerEl = document.querySelector('a[href="' + tab_name + '"]');
            if (someTabTriggerEl) {
                const actTab = new Tab(someTabTriggerEl);
                actTab.show();
            }
        }
    }
}
</script>