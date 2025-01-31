<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"
import axios from "axios";
import Swal from "sweetalert2";

export default {
    name: "PLANS",
    components: {
        Layout, pageheader
    },
    data() {
        return {
            modalShow: false,
            plans: [],
            plan: {
                id:"",
                plan_name: "",
                plan_description: "",
                plan_up: "",
                plan_down: "",
                price: "",
            },
            operation: false,
        }
    },
    created() {
        this.getPlans();
    },
    methods: {
        updatePlan() {
            if (this.operation==false) {
                axios.post("/api/v1/plans/", { 
                    plan_name: this.plan.plan_name,
                    plan_description: this.plan.plan_description,
                    plan_up: this.plan.plan_up,
                    plan_down: this.plan.plan_down,
                    price: this.plan.price,
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow = !this.modalShow;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getPlans();
                });
            } else {
                axios.patch(`/api/v1/plans/${this.plan.id}/`, { 
                    plan_name: this.plan.plan_name,
                    plan_description: this.plan.plan_description,
                    plan_up: this.plan.plan_up,
                    plan_down: this.plan.plan_down,
                    price: this.plan.price,
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow = !this.modalShow;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getPlans();
                });
            }
        },
        getPlans() {
            axios.get("/api/v1/plans/").then((response)=> {
                this.plans = response.data;
            });
        },
        getPlan(plan_id) {
            this.modalShow = !this.modalShow;
            this.operation = true;
            axios.get(`/api/v1/plans/${plan_id}/`).then((response) => {
                this.plan = response.data;
            }).catch(error => {
                console.log(JSON.stringify(error));
            });
        },
        deletePlan(plan_id) {
            axios.delete(`/api/v1/plans/${plan_id}/`).then(() => {
                this.plans = this.plans.filter((plan) => plan.id !== plan_id);
            });
        },
        showAddModal() {
            this.plan = {};
            this.modalShow = !this.modalShow;
            this.operation = false;
        },
        cancelDelete(plan_id) {
            const swalWithBootstrapButtons = Swal.mixin({
                customClass: {
                    confirmButton: "btn btn-success",
                    cancelButton: "btn btn-danger ml-2",
                },
                buttonsStyling: false,
            });

            swalWithBootstrapButtons
                .fire({
                    title: "Are you sure?",
                    text: "You won't be able to revert this!",
                    icon: "warning",
                    confirmButtonText: "Yes, delete it!",
                    cancelButtonText: "No, cancel!",
                    showCancelButton: true,
                })
                .then((result) => {
                    if (result.value) {
                        this.deletePlan(plan_id);
                        swalWithBootstrapButtons.fire(
                            "Deleted!",
                            "Your file has been deleted.",
                            "success"
                        );
                    } else if (
                        /* Read more about handling dismissals below */
                        result.dismiss === Swal.DismissReason.cancel
                    ) {
                        swalWithBootstrapButtons.fire(
                            "Cancelled",
                            "Delete operation was cancelled.",
                            "error"
                        );
                    }
                });
        },
    }
}
</script>

<template>
    <Layout>
        <pageheader title="Subscription Plan list" pageTitle="Plans" />
        <BRow>
            <BCol class="col-sm-12">
                <BCard no-body class="table-card">
                    <BCardBody>
                        <div class="text-end p-sm-4 pb-sm-2">
                            <!-- <router-link to="/add-product" class="btn btn-primary"> <i class="ti ti-plus f-18"></i> Add Region </router-link>-->
                            <BButton variant="primary" class="btn btn-sm" @click="showAddModal">Add Plan</BButton>
                        </div>
                        <div class="table-responsive">
                            <table class="table table-hover table-sm tbl-product" id="pc-dt-simple">
                                <thead>
                                    <tr>
                                        <th class="text-end">#</th>
                                        <th>Plan Detail</th>
                                        <th>up/down - Mbps</th>
                                        <th>Description</th>
                                        <th class="text-end">Price</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(plan, index) in plans" :key="plan.id">
                                        <td class="text-end">{{index + 1}}</td>
                                        <td>
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ plan.plan_name }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ plan.plan_description }} </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td>{{ plan.plan_down }}/{{ plan.plan_up }}</td>
                                        <td>{{ plan.plan_description }}</td>
                                        <td class="text-end">
                                            {{ plan.price }}
                                            <div class="prod-action-links">
                                                <ul class="list-inline me-auto mb-0">
                                                    <!--
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="View">
                                                        <a href="#" class="avtar avtar-xs btn-link-secondary btn-pc-default" data-bs-toggle="offcanvas" data-bs-target="#productOffcanvas">
                                                            <i class="ti ti-eye f-18"></i>
                                                        </a>
                                                    </li>
                                                    -->
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Edit">
                                                        <!-- 
                                                        <router-link to="/add-product" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-edit-circle f-18"></i>
                                                        </router-link> 
                                                        -->
                                                        <a href="#" @click="getPlan(plan.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-edit-circle f-18"></i>
                                                        </a>
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                        <a href="#" @click="cancelDelete(plan.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
                                                            <i class="ti ti-trash f-18"></i>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </td>
                                    </tr>
                                    
                                </tbody>
                            </table>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        
                        <BModal v-model="modalShow" title="Subscription Plan" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-1">
                                    <label for="plan" class="col-sm-2 col-form-label form-control-sm">Plan</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="plan.plan_name" type="text" class="form-control form-control-sm" id="plan">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="description" class="col-sm-2 col-form-label form-control-sm">Description</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="plan.plan_description" class="form-control form-control-sm" id="description" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="down" class="col-sm-2 col-form-label form-control-sm">Download</label>
                                    <BCol class="col-sm-6">
                                        <input v-model="plan.plan_down" type="text" class="form-control form-control-sm" aria-label="Amount (to the nearest peso)">
                                        <!-- <span class="input-group-text">.00</span> -->
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="up" class="col-sm-2 col-form-label form-control-sm">Upload</label>
                                    <BCol class="col-sm-6">
                                        <input v-model="plan.plan_up" type="text" class="form-control form-control-sm" aria-label="Amount (to the nearest peso)">
                                        <!-- <span class="input-group-text">.00</span> -->
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="price" class="col-sm-2 col-form-label form-control-sm">Price</label>
                                    <BCol class="col-sm-6">
                                        <div class="input-group input-group-sm mb-3">
                                            <span class="input-group-text">Php</span>
                                            <input v-model="plan.price" type="text" class="form-control text-end" aria-label="Amount (to the nearest peso)">
                                            <span class="input-group-text">.00</span>
                                        </div>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="modalShow = !modalShow">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updatePlan">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>
    </Layout>
</template>