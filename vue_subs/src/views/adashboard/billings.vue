<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"
import axios from "axios";
import Swal from "sweetalert2";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { useAuthStore } from '@/stores/auth';
// import { BoldIcon } from "@zhuowenli/vue-feather-icons";


export default {
    name: "BILLINGS",
    components: {
        Layout, pageheader, flatPickr,
    },
    setup() {
        const authStore = useAuthStore();
        return {
            authStore,
        };
    },
    data() {
        return {
            modalShow: false,
            operation: false,

            subscriptions: [],
            regions: [],
            provinces: [],
            municipalities: [],
            barangays: [],
            plans: [],
            modems: [],
            subs1: {},
            billing: {},
            bills: [],
            users: [],
        
            /* search */
            searchQuery: "", // Search input
            loading: false,
        }
    },
    created() {
        this.getUsers();
    },
    mounted() {
        const sub_id = this.$route.query.sub_id;
        this.getSubscription1(sub_id);
        this.getBills(sub_id);
    },
    methods: {
        async updateBill() {
            try {
                if (this.operation==false) {
                    await axios.post("/api/v1/billings/", { 
                        billed_by: this.authStore.user.id,
                        subscription: this.subs1.id,
                        collector: this.billing.collector,
                        amount_due:this.billing.amount_due,
                        bill_type:this.billing.bill_type,
                        notice: this.billing.notice,
                        remarks: this.billing.remarks
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
                        this.getBills(this.subs1.id);
                    });
                } else {
                    await axios.patch(`/api/v1/billings/${this.billing.id}/`, { 
                        billed_by: this.authStore.user.id,
                        subscription: this.subs1.id,
                        collector: this.billing.collector,
                        amount_due:this.billing.amount_due,
                        bill_type:this.billing.bill_type,
                        notice: this.billing.notice,
                        remarks: this.billing.remarks
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
                        this.getBills(this.subs1.id);
                    });
                }
            } catch(error) {
                console.error('Error updating bill:', error);
            }

        },
        async getSubscriptions() {
            try {
                await axios.get("/api/v1/subscriptions/").then((response)=> {
                    this.subscriptions = response.data;
                });
            } catch (error) {
                console.error('Error fetching subscriptions:', error);
            }
        },
        async getSubscription(subs_id) {
            this.modalShow = !this.modalShow;
            this.operation = true;
            await axios.get(`/api/v1/subscriptions/${subs_id}/`).then((response) => {
                    this.subscription = response.data;
                    this.subs1 = response.data;
                }).catch(error => {
                    console.log(JSON.stringify(error));
            });
        },
        async getSubscription1(subs_id) {
            await axios.get(`/api/v1/subscriptions/${subs_id}/`).then((response) => {
                    this.subs1 = response.data;
                }).catch(error => {
                    console.log(JSON.stringify(error));
            });
        },
        async deleteSubscription(subs_id) {
            await axios.delete(`/api/v1/subscriptions/${subs_id}/`).then(() => {
                this.subscriptions = this.subscriptions.filter((subs) => subs.id !== subs_id);
            });
        },
        showAddModalOpen() {
            this.billing = {};
            this.billing.amount_due = this.subs1.plan_amount;
            this.billing.billing_date = new Date();
            this.modalShow = !this.modalShow;
            this.operation = false;
        },
        showAddModalClose() {
            this.billing = {};
            this.modalShow = !this.modalShow;
            this.operation = false;
        },
        cancelDelete(subs_id) {
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
                        this.deleteSubscription(subs_id);
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
  
        formattedDateTime(date_time_field) {
            if (!date_time_field) return '';

            // Parse the date-time string
            const date = new Date(Date.parse(date_time_field));

            // Check if the parsed date is valid
            if (isNaN(date.getTime())) {
                console.error('Invalid date:', date_time_field);
                return 'Invalid date';
            }

            // Extract parts of the date
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const month = months[date.getMonth()];
            const day = String(date.getDate()).padStart(2, '0');
            const year = date.getFullYear();

            // Extract and format time
            const hours = date.getHours();
            const minutes = String(date.getMinutes()).padStart(2, '0');
            const period = hours >= 12 ? 'PM' : 'AM';
            const formattedHours = hours % 12 || 12; // Convert 24-hour to 12-hour format

            // Combine formatted parts
            return `${month}-${day}-${year} @ ${formattedHours}:${minutes} ${period}`;
        },
        formattedDateTimeDate(date_time_field) {
            if (!date_time_field) return '';

            // Parse the date-time string
            const date = new Date(Date.parse(date_time_field));

            // Check if the parsed date is valid
            if (isNaN(date.getTime())) {
                console.error('Invalid date:', date_time_field);
                return 'Invalid date';
            }

            // Extract parts of the date
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const month = months[date.getMonth()];
            const day = String(date.getDate()).padStart(2, '0');
            const year = date.getFullYear();

            // Combine formatted parts
            return `${month}-${day}-${year}`;
        },
        formattedBirthDate(date_time_field) {
            if (!date_time_field) return '';

            // Parse the date-time string
            const date = new Date(Date.parse(date_time_field));

            // Check if the parsed date is valid
            if (isNaN(date.getTime())) {
                console.error('Invalid date:', date_time_field);
                return 'Invalid date';
            }

            // Extract parts of the date
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const month = months[date.getMonth()];
            const day = String(date.getDate()).padStart(2, '0');
            const year = date.getFullYear();

            // Combine formatted parts
            return `${month}-${day}-${year}`;
        },
        async getBills(id) {
            try {
                this.loading = true;
                await axios.get(`/api/v1/billings/?id=${id}`).then((response) => {
                    this.bills = response.data;
                })
            } catch (error) {
                console.log("Error fetching bills", error);
            } finally {
                this.loading = false;
            }
        },
        async getBill(id) {
            try {
                this.operation = true;
                this.modalShow = !this.modalShow;
                await axios.get(`/api/v1/billings/${id}/`).then((response) => {
                    this.billing = response.data;
                })
            } catch (error) {
                console.log("Error fetching bills", error);
            } finally {
                this.loading = false;
            }
        },
        async deleteBill(id) {
            try {
                await axios.delete(`/api/v1/billings/${id}/`).then(() => {
                    this.bills = this.bills.filter((bill) => bill.id !== id);
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        cancelDeleteBill(id) {
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
                        this.deleteBill(id);
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

        /* search */
        // Apply search
        applySearch() {
            this.getSubscribersSearch(); // Fetch data with current search query
        },
        async getSubscribersSearch() {
            try {
                const params = {};
                this.loading = true;
                if (this.searchQuery) {
                    params.search = this.searchQuery; // Add search query to parameters
                }
                const response = await axios.get("/api/v1/subscriptions/", { params });
                this.subscriptions = response.data;
            } catch (error) {
                console.error("Error fetching subscribers:", error);
            } finally {
                this.loading=false;
            }
        },
        /* get users */
        async getUsers() {
            try {
                await axios.get("/api/v1/users/").then((response) => {
                    this.users = response.data;
                })
            } catch (error) {
                console.error('Error fetching users:', error);                
            }
        }
    }
}
</script>

<template>
    <Layout>
        <pageheader title="Billing list" pageTitle="Billings" />
        <BRow>
            <BCol class="col-sm-12">
                <BCard no-body class="table-card">
                    <BCardBody>
                        <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2">
                            <!-- Search Input with Magnifying Glass -->
                            <div class="">
                                <router-link to="/subscriptions" class="pc-link">
                                    <span class="pc-micon">
                                        <i class="ti ti-arrow-left f-18"> Back</i>
                                    </span>
                                </router-link>
                            </div>

                            <!-- Add Subscriber Button -->
                                <!-- <router-link to="/add-product" class="btn btn-primary"> <i class="ti ti-plus f-18"></i> Add Region </router-link>-->
                        </div>
                        <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2 mb-3">
                            <div>
                                <h5>{{subs1.first_name}} {{subs1.last_name}}</h5>
                                <span>Account: <strong>{{ subs1.no }}</strong> - <span class="ms-1"> {{ subs1.alias }}</span>
                                    <span v-if="subs1.bill_schedule=='start'" class="badge bg-success text-dark ms-1">1</span>
                                    <span v-else-if="subs1.bill_schedule=='end'" class="badge bg-primary text-dark ms-1">2</span>
                                    <span v-else class="badge bg-warning text-dark ms-1">0</span>
                                </span><br />
                                <span>Type: <strong>{{ subs1.sub_type }}</strong></span><br />
                                <span>Plan: <strong>{{ subs1.plan_name }}</strong></span>
                            </div>

                            <BButton variant="primary" class="btn btn-sm" @click="showAddModalOpen">Add Billing</BButton>
                        </div>
                        <div class="table-responsive fixed-height">
                            <!-- Show Spinner While Loading -->
                            <div v-if="loading" class="text-center p-4">
                                <BSpinner label="Loading..."></BSpinner>
                            </div>
                            <table v-else class="table table-hover table-sm tbl-product" id="pc-dt-simple-1">
                                <thead>
                                    <tr>
                                        <th class="text-end">#</th>
                                        <th>Billing #</th>
                                        <th>Date/Type</th>
                                        <th class="text-end">Amount</th>
                                        <th>Remarks</th>
                                        <th>Billed by</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(bill, index) in bills" :key="bill.id"
                                        :class="{ 'table-active': selectedRowBill === bill.id}"
                                        @dblclick="goToNextTabPay(bill.id)">
                                        <td class="text-end">{{index + 1}}</td>
                                        <td>
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">
                                                        {{ bill.billing_no }}
                                                        <span v-if="bill.is_paid" class="badge bg-success text-dark">Paid</span>
                                                        <span v-else class="badge bg-danger text-dark">Unpaid</span>
                                                        <span v-if="bill.is_partial" class="badge bg-warning ms-1">Partial</span>
                                                    </h6>
                                                    <p class="text-muted f-12 mb-0">{{ bill.collector_first_name }} {{ bill.collector_last_name }}</p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td>
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ formattedDateTime(bill.billing_date) }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ bill.bill_type }} </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td class="text-end">
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ bill.amount_due }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ bill.is_paid}}</p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td>
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ bill.notice }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ bill.remarks}}</p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td class="text-center">
                                            <h6 class="mb-1">{{bill.first_name}} {{ bill.last_name }}</h6>
                                            <p class="text-muted f-12 mb-0">
                                                {{ formattedDateTime(bill.updated_on)}}
                                            </p>
                                            <div class="prod-action-links">
                                                <ul class="list-inline me-auto mb-0">
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Edit">
                                                        <a href="#" @click="getBill(bill.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-edit-circle f-18"></i>
                                                        </a>
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Payment">
                                                        <a href="#" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-receipt f-18"></i>
                                                        </a>
                                                    </li>
                                                    <li class="list-inline-item align-bottom">
                                                        |
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                        <a href="#" @click="cancelDeleteBill(bill.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
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

        <!-- Billing modal -->
        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        <BModal v-model="modalShow" title="Billing" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-10">
                                    <BCol class="mb-1">
                                        <div class="col-sm-10 text-center">
                                            <h5 class="mb-1">{{ subs1.last_name }}, {{ subs1.first_name }}</h5>
                                            <span text-muted f-12 mb-0>{{ subs1.no }}</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <hr />
                                <BRow class=" mb-1">
                                    <label for="alias" class="col-sm-2 col-form-label form-control-sm">Billed by </label>
                                    <BCol class="col-sm-10">
                                        <h6>{{ authStore.user.last_name }}, {{ authStore.user.first_name }}</h6>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="collector" class="col-sm-2 col-form-label form-control-sm">Collector</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="billing.collector" name="collector" id="" class="form-control form-select-sm">
                                            <option v-for="user in users" :key="user.id" :value="user.id">{{ user.first_name }} {{ user.last_name }}</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="date_suspended">Date</label>
                                    <BCol class="col-sm-6">
                                        <flat-pickr v-model="billing.billing_date" :first-day-of-week="1" lang="en" confirm
                                    class="form-control form-control-sm"></flat-pickr>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="amount" class="col-sm-2 col-form-label form-control-sm">Due</label>
                                    <BCol class="col-sm-6">
                                        <div class="input-group input-group-sm mb-1">
                                            <span class="input-group-text">Php</span>
                                            <input v-model="billing.amount_due" type="text" class="form-control form-control-sm text-end" aria-label="Amount (to the nearest peso)" id="amount">
                                            <span class="input-group-text">.00</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="type">Type</label>
                                    <BCol class="col-sm-6">
                                        <select v-model="billing.bill_type" class="form-select form-select-sm" id="type">
                                            <option value="">---</option>
                                            <option value="net">Internet</option>
                                            <option value="foc">FOC</option>
                                            <option value="labor">Labor</option>
                                            <option value="others">Others</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="notice">Notice</label>
                                    <BCol class="col-sm-6">
                                        <select v-model="billing.notice" class="form-select form-select-sm" id="notice">
                                            <option value="">---</option>
                                            <option value="disconnection">Disconnection</option>
                                            <option value="updated">Updated</option>
                                            <option value="disconnected">Disconnected</option>
                                            <option value="warning">Warning</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="remarks" class="col-sm-2 col-form-label form-control-sm">Remarks</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="billing.remarks" class="form-control form-control-sm" id="remarks" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="showAddModalClose">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updateBill">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>
    </Layout>
</template>

<style lang="css">
    .fixed-height {
        max-height: 600px; /* Set the desired fixed height for the table container */
        overflow-y: auto; /* Enable vertical scrolling */
        border: 1px solid #ddd; /* Optional: Add a border for clarity */
    }

    .table-responsive {
        overflow-x: auto; /* Ensure horizontal scrolling is enabled for wide tables */
    }

    .search-bar {
        width: 400px;
    }

    .d-flex {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .input-group-text {
        background-color: #f8f9fa;
        border-right: none;
    }

    .form-control {
        border-left: none;
    }

    .table-active {
        background-color: #e9ecef !important; /* Bootstrap's active row color */
    }

</style>