<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"
import axios from "axios";
import Swal from "sweetalert2";

export default {
    name: "MODEMS",
    components: {
        Layout, pageheader
    },
    data() {
        return {
            modalShow: false,
            modems: [],
            modem: {
                id:"",
                modem_brand: "",
                modem_description: "",
                modem_supplier: "",
                is_gigabit: false,
                price: "",
            },
            operation: false,
        }
    },
    created() {
        this.getModems();
    },
    methods: {
        updateModem() {
            if (this.operation==false) {
                axios.post("/api/v1/modems/", { 
                    modem_brand: this.modem.modem_brand,
                    modem_description: this.modem.modem_description,
                    is_gigabit: this.modem.is_gigabit,
                    modem_supplier: this.modem.modem_supplier,
                    price: this.modem.price,
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
                    this.getModems();
                });
            } else {
                axios.patch(`/api/v1/modems/${this.modem.id}/`, { 
                    modem_brand: this.modem.modem_brand,
                    modem_description: this.modem.modem_description,
                    is_gigabit: this.modem.is_gigabit,
                    modem_supplier: this.modem.modem_supplier,
                    price: this.modem.price,
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
                    this.getModems();
                });
            }
        },
        getModems() {
            axios.get("/api/v1/modems/").then((response)=> {
                this.modems = response.data;
            });
        },
        getModem(modem_id) {
            this.modalShow = !this.modalShow;
            this.operation = true;
            axios.get(`/api/v1/modems/${modem_id}/`).then((response) => {
                this.modem = response.data;
            }).catch(error => {
                console.log(JSON.stringify(error));
            });
        },
        deleteModem(modem_id) {
            axios.delete(`/api/v1/modems/${modem_id}/`).then(() => {
                this.modems = this.modems.filter((modem) => modem.id !== modem_id);
            });
        },
        showAddModal() {
            this.modem = {};
            this.modalShow = !this.modalShow;
            this.operation = false;
        },
        cancelDelete(modem_id) {
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
                        this.deletePlan(modem_id);
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
        <pageheader title="Modem list" pageTitle="Modems" />
        <BRow>
            <BCol class="col-sm-12">
                <BCard no-body class="table-card">
                    <BCardBody>
                        <div class="text-end p-sm-4 pb-sm-2">
                            <!-- <router-link to="/add-product" class="btn btn-primary"> <i class="ti ti-plus f-18"></i> Add Region </router-link>-->
                            <BButton variant="primary" class="btn btn-sm" @click="showAddModal">Add Modem</BButton>
                        </div>
                        <div class="table-responsive">
                            <table class="table table-hover table-sm tbl-product" id="pc-dt-simple">
                                <thead>
                                    <tr>
                                        <th class="text-end">#</th>
                                        <th>Modem</th>
                                        <th>Type (Gigabit?)</th>
                                        <th>Supplier</th>
                                        <th>Description</th>
                                        <th class="text-end">Price</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(modem, index) in modems" :key="modem.id">
                                        <td class="text-end">{{index + 1}}</td>
                                        <td>
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ modem.modem_brand }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ modem.modem_description }} </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td>{{ modem.is_gigabit }}</td>
                                        <td class="text-start">{{ modem.modem_supplier }}</td>
                                        <td>{{ modem.modem_description }}</td>
                                        <td class="text-end">
                                            {{ modem.price }}
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
                                                        <a href="#" @click="getModem(modem.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-edit-circle f-18"></i>
                                                        </a>
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                        <a href="#" @click="cancelDelete(modem.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
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
                        
                        <BModal v-model="modalShow" title="Modem Management" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-1">
                                    <label for="brand" class="col-sm-2 col-form-label form-control-sm">Brand</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="modem.modem_brand" type="text" class="form-control form-control-sm" id="brand">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="description" class="col-sm-2 col-form-label form-control-sm">Description</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="modem.modem_description" class="form-control form-control-sm" id="description" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="supplier" class="col-sm-2 col-form-label form-control-sm">Supplier</label>
                                    <BCol class="col-sm-10">
                                        <div class="input-group input-group-sm mb-1">
                                            <input v-model="modem.modem_supplier" type="text" class="form-control form-control-sm" id="supplier">
                                            <!-- <span class="input-group-text">.00</span> -->
                                        </div>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="price" class="col-sm-2 col-form-label form-control-sm">Price</label>
                                    <BCol class="col-sm-6">
                                        <div class="input-group input-group-sm mb-1">
                                            <span class="input-group-text">Php</span>
                                            <input v-model="modem.price" type="text" class="form-control form-control-sm text-end" aria-label="Amount (to the nearest peso)">
                                            <span class="input-group-text">.00</span>
                                        </div>
                                    </BCol>
                                </BRow>

                                <BRow class=" mb-1">
                                    <label for="gigabit" class="col-sm-2 col-form-label form-control-sm"></label>
                                    <BCol class="col-sm-4">
                                        <div class="form-group form-check">
                                            <input v-model="modem.is_gigabit" type="checkbox" class="form-check-input form-check-sm" id="gigabit">
                                            <label for="gigabit">Check if modem is gigabit.</label>
                                        </div>
                                    </BCol>
                                </BRow>


                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="modalShow = !modalShow">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updateModem">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>
    </Layout>
</template>