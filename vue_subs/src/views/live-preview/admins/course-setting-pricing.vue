<script>
import Layout from "@/layout/main.vue";
import pageheader from "@/components/page-header.vue";

export default {
    name: "Pricing",
    components: {
        Layout,
        pageheader
    }
};
</script>
<template>
    <Layout>
        <pageheader title="Pricing" pageTitle="Online Courses" />
        <!-- [ Main Content ] start -->
        <div class="row">
            <div class="col-12">
                <BCard no-body class="border-0 shadow-none bg-transparent mb-1">
                    <BCardBody class=" p-2">
                        <div class="row align-items-center mb-3">
                            <div class="col">
                                <h5>Plans & Pricing</h5>
                                <p>Every paid plan comes with educational resources and training to support you on your journey, along with a 30-day money-back guarantee.</p>
                            </div>
                            <div class="col-auto">
                                <ul class="nav nav-pills nav-price" id="pills-tab" role="tablist">
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link active" id="pills-home-tab" data-bs-toggle="pill" data-bs-target="#pills-home" type="button" role="tab" aria-controls="pills-home" aria-selected="true">Monthly</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link" id="pills-profile-tab" data-bs-toggle="pill" data-bs-target="#pills-profile" type="button" role="tab" aria-controls="pills-profile" aria-selected="false">Yearly <span class="badge bg-primary ms-2">Save 30%</span></button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
                <div class="tab-content" id="pills-tabContent">
                    <div class="tab-pane fade show active" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab" tabindex="0">
                        <div class="row justify-content-center align-items-center">
                            <!-- [ sample-page ] start -->
                            <div class="col-md-6 col-lg-4">
                                <BCard no-body class="price-card">
                                    <BCardBody class="">
                                        <div class="price-head v2">
                                            <h5 class="mb-0">Basic</h5>
                                            <p class="text-muted">03 Services</p>
                                            <div class="price-price mt-4">$69 <span class="text-muted"> Lifetime</span></div>
                                            <div class="d-grid"><a class="btn btn-outline-secondary mt-4" href="#">Buy Now</a></div>
                                        </div>
                                        <ul class="list-group list-group-flush product-list">
                                            <li class="list-group-item enable">One End Product</li>
                                            <li class="list-group-item enable">No attribution required</li>
                                            <li class="list-group-item enable">TypeScript</li>
                                            <li class="list-group-item">Figma Design Resources</li>
                                            <li class="list-group-item">Create Multiple Products</li>
                                            <li class="list-group-item">Create a SaaS Project</li>
                                            <li class="list-group-item">Resale Product</li>
                                            <li class="list-group-item">Separate sale of our UI Elements?</li>
                                        </ul>
                                    </BCardBody>
                                </BCard>
                            </div>
                            <div class="col-md-6 col-lg-4">
                                <BCard no-body class="price-card price-popular">
                                    <BCardBody class="">
                                        <div class="price-head v2">
                                            <span class="badge f-12 bg-success mb-3">Popular</span>
                                            <h5 class="mb-0">Standard</h5>
                                            <p class="text-muted">05 Services</p>
                                            <div class="price-price mt-4">$129 <span class="text-muted"> Lifetime</span></div>
                                            <div class="d-grid"><a class="btn btn-primary mt-4" href="#">Buy Now</a></div>
                                        </div>
                                        <ul class="list-group list-group-flush product-list">
                                            <li class="list-group-item enable">One End Product</li>
                                            <li class="list-group-item enable">No attribution required</li>
                                            <li class="list-group-item enable">TypeScript</li>
                                            <li class="list-group-item enable">Figma Design Resources</li>
                                            <li class="list-group-item enable">Create Multiple Products</li>
                                            <li class="list-group-item">Create a SaaS Project</li>
                                            <li class="list-group-item">Resale Product</li>
                                            <li class="list-group-item">Separate sale of our UI Elements?</li>
                                        </ul>
                                    </BCardBody>
                                </BCard>
                            </div>
                            <div class="col-md-6 col-lg-4">
                                <BCard no-body class="price-card">
                                    <BCardBody class="">
                                        <div class="price-head v2">
                                            <h5 class="mb-0">Premium</h5>
                                            <p class="text-muted">08 Services</p>
                                            <div class="price-price mt-4">$599 <span class="text-muted"> Lifetime</span></div>
                                            <div class="d-grid"><a class="btn btn-outline-secondary mt-4" href="#">Buy Now</a></div>
                                        </div>
                                        <ul class="list-group list-group-flush product-list">
                                            <li class="list-group-item enable">One End Product</li>
                                            <li class="list-group-item enable">No attribution required</li>
                                            <li class="list-group-item enable">TypeScript</li>
                                            <li class="list-group-item enable">Figma Design Resources</li>
                                            <li class="list-group-item enable">Create Multiple Products</li>
                                            <li class="list-group-item enable">Create a SaaS Project</li>
                                            <li class="list-group-item enable">Resale Product</li>
                                            <li class="list-group-item enable">Separate sale of our UI Elements?</li>
                                        </ul>
                                    </BCardBody>
                                </BCard>
                            </div>
                            <!-- [ sample-page ] end -->
                        </div>
                    </div>
                    <div class="tab-pane fade" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab" tabindex="0">
                        <div class="row justify-content-center align-items-center">
                            <!-- [ sample-page ] start -->
                            <div class="col-md-6 col-lg-4">
                                <BCard no-body class="price-card">
                                    <BCardBody class="">
                                        <div class="price-head v2">
                                            <h5 class="mb-0">Basic</h5>
                                            <p class="text-muted">03 Services</p>
                                            <div class="price-price mt-4">$269 <span class="text-muted"> Lifetime</span></div>
                                            <div class="d-grid"><a class="btn btn-outline-secondary mt-4" href="#">Buy Now</a></div>
                                        </div>
                                        <ul class="list-group list-group-flush product-list">
                                            <li class="list-group-item enable">One End Product</li>
                                            <li class="list-group-item enable">No attribution required</li>
                                            <li class="list-group-item enable">TypeScript</li>
                                            <li class="list-group-item">Figma Design Resources</li>
                                            <li class="list-group-item">Create Multiple Products</li>
                                            <li class="list-group-item">Create a SaaS Project</li>
                                            <li class="list-group-item">Resale Product</li>
                                            <li class="list-group-item">Separate sale of our UI Elements?</li>
                                        </ul>
                                    </BCardBody>
                                </BCard>
                            </div>
                            <div class="col-md-6 col-lg-4">
                                <BCard no-body class="price-card price-popular">
                                    <BCardBody class="">
                                        <div class="price-head v2">
                                            <span class="badge f-12 bg-success mb-3">Popular</span>
                                            <h5 class="mb-0">Standard</h5>
                                            <p class="text-muted">05 Services</p>
                                            <div class="price-price mt-4">$529 <span class="text-muted"> Lifetime</span></div>
                                            <div class="d-grid"><a class="btn btn-primary mt-4" href="#">Buy Now</a></div>
                                        </div>
                                        <ul class="list-group list-group-flush product-list">
                                            <li class="list-group-item enable">One End Product</li>
                                            <li class="list-group-item enable">No attribution required</li>
                                            <li class="list-group-item enable">TypeScript</li>
                                            <li class="list-group-item enable">Figma Design Resources</li>
                                            <li class="list-group-item enable">Create Multiple Products</li>
                                            <li class="list-group-item">Create a SaaS Project</li>
                                            <li class="list-group-item">Resale Product</li>
                                            <li class="list-group-item">Separate sale of our UI Elements?</li>
                                        </ul>
                                    </BCardBody>
                                </BCard>
                            </div>
                            <div class="col-md-6 col-lg-4">
                                <BCard no-body class="price-card">
                                    <BCardBody class="">
                                        <div class="price-head v2">
                                            <h5 class="mb-0">Premium</h5>
                                            <p class="text-muted">08 Services</p>
                                            <div class="price-price mt-4">$1299 <span class="text-muted"> Lifetime</span></div>
                                            <div class="d-grid"><a class="btn btn-outline-secondary mt-4" href="#">Buy Now</a></div>
                                        </div>
                                        <ul class="list-group list-group-flush product-list">
                                            <li class="list-group-item enable">One End Product</li>
                                            <li class="list-group-item enable">No attribution required</li>
                                            <li class="list-group-item enable">TypeScript</li>
                                            <li class="list-group-item enable">Figma Design Resources</li>
                                            <li class="list-group-item enable">Create Multiple Products</li>
                                            <li class="list-group-item enable">Create a SaaS Project</li>
                                            <li class="list-group-item enable">Resale Product</li>
                                            <li class="list-group-item enable">Separate sale of our UI Elements?</li>
                                        </ul>
                                    </BCardBody>
                                </BCard>
                            </div>
                            <!-- [ sample-page ] end -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
</template>