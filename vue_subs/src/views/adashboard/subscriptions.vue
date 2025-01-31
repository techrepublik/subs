<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"
import axios from "axios";
import Swal from "sweetalert2";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { useAuthStore } from '@/stores/auth';


export default {
    name: "SUBSCRIPTIONS",
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
            modalShow1: false,
            subscribers: [],
            subscriber: {
                id:"",
                first_name: "",
                last_name: "",
                middle_name: "",
                ext_name: "",
                marital_status: "",
                gender: "",
                contact_no:"",
                address: "",
                birth_date:"",
                note: "",
                is_good: "",
                added_by: "",
            },
            operation: false,

            subscriptions: [],
            regions: [],
            provinces: [],
            municipalities: [],
            barangays: [],
            plans: [],
            modems: [],
            subscription:{
                id: "",
                subscriber:"",
                employee:"",
                no:"",
                alias: "",
                note: "",
                referred_by: "",
                region:"",
                province:"",
                municipality:"",
                barangay:"",
                latitude: 0.00,
                longitude: 0.00,
                plan: "",
                pon_no: "",
                nap_no: "",
                modem_serial: "",
                modem: "",
                sub_status: "",
                sub_type:"",
                date_activated:"",
                date_terminated: "",
                date_suspended: "",
                modem_username: "",
                modem_password: "",
                created_on: "",
                updated_by: "",
                region_name: "",
                province_name: "",
                municipality_name: "",
                barangay_name: "",
                plan_name: "",
                modem_name: "",
            },

            /* search */
            searchQuery: "", // Search input
            loading: false,

            marking: "+",
            expandedRows: [], // IDs of expanded subscription rows
            subs: {}
        }
    },
    created() {
        this.getSubscriptions();
        this.getRegions();
        this.getPlans();
        this.getModems();
    },
    methods: {
        async updateRecord() {
            try {
                if (this.operation==false) {
                    await axios.post("/api/v1/subscriptions/", { 
                        subscriber: this.subscriber.id,
                        employee: this.authStore.user.id,
                        alias: this.subscription.alias,
                        note: this.subscription.note,
                        referred_by: this.subscription.referred_by,
                        region: this.subscription.region,
                        province: this.subscription.province,
                        municipality: this.subscription.municipality,
                        barangay: this.subscription.barangay,
                        latitude: this.subscription.latitude,
                        longitude: this.subscription.longitude,
                        plan: this.subscription.plan,
                        pon_no: this.subscription.pon_no,
                        nap_no: this.subscription.nap_no,
                        modem_serial: this.subscription.modem_serial,
                        modem: this.subscription.modem,
                        sub_status: this.subscription.sub_status,
                        sub_type: this.subscription.sub_type,
                        date_activated: this.subscription.date_activated,
                        date_terminated: this.subscription.date_terminated,
                        data_suspended: this.subscription.date_suspended,
                        modem_username: this.subscription.modem_username,
                        modem_password: this.subscription.modem_password,
                        created_on: Date.now()
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
                        this.getSubscribers();
                    });
                } else {
                    await axios.patch(`/api/v1/subscriptions/${this.subscription.id}/`, { 
                        subscriber: this.subscriber.id,
                        employee: this.authStore.user.id,
                        alias: this.subscription.alias,
                        note: this.subscription.note,
                        referred_by: this.subscription.referred_by,
                        region: this.subscription.region,
                        province: this.subscription.province,
                        municipality: this.subscription.municipality,
                        barangay: this.subscription.barangay,
                        latitude: this.subscription.latitude,
                        longitude: this.subscription.longitude,
                        plan: this.subscription.plan,
                        pon_no: this.subscription.pon_no,
                        nap_no: this.subscription.nap_no,
                        modem_serial: this.subscription.modem_serial,
                        modem: this.subscription.modem,
                        sub_status: this.subscription.sub_status,
                        sub_type: this.subscription.sub_type,
                        date_activated: this.subscription.date_activated,
                        date_terminated: this.subscription.date_terminated,
                        data_suspended: this.subscription.date_suspended,
                        modem_username: this.subscription.modem_username,
                        modem_password: this.subscription.modem_password
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
                        this.getSubscribers();
                    });
                }
            } catch(error) {
                console.error('Error fetching subscribers:', error);
            }

        },
        async getSubscriptions() {
            try {
                await axios.get("/api/v1/subscriptions/").then((response)=> {
                    this.subscriptions = response.data;
                    console.log(this.subscriptions);
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
            this.subscription = {};
            this.modalShow1 = !this.modalShow1;
            this.operation = true;
        },
        showAddModalClose() {
            this.subscription = {};
            this.modalShow1 = !this.modalShow1;
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
        // formattedDateTime(date_time_field) {
        //     if (!date_time_field) return '';

        //     // Ensure correct parsing of ISO date with timezone
        //     const date = new Date(Date.parse(date_time_field));

        //     // Check if date is valid
        //     if (isNaN(date.getTime())) {
        //         console.error('Invalid date:', date_time_field);
        //         return 'Invalid date';
        //     }

        //     // Format date and time
        //     const formattedDate = date.toISOString().split('T')[0]; // YYYY-MM-DD
        //     const hours = date.getHours();
        //     const minutes = date.getMinutes();
        //     const period = hours >= 12 ? 'PM' : 'AM';

        //     // Convert 24-hour time to 12-hour time
        //     const formattedHours = hours % 12 || 12;

        //     // Pad minutes with leading zeros
        //     const formattedMinutes = minutes.toString().padStart(2, '0');

        //     // Combine formatted parts
        //     return `${formattedDate}:${formattedHours}:${formattedMinutes}${period}`;
        // },
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
        async getRegions() {
            try {
                const response = await axios.get('/api/v1/regions/');
                this.regions = response.data;
            } catch (error) {
                console.error('Error fetching regions:', error);
            }
        },
        async getProvinces() {
            if (!this.subscription.region) return;
            try {
                const response = await axios.get(`/api/v1/provinces/?region_id=${this.subscription.region}`);
                this.provinces = response.data;
                this.municipalities = [];
                this.barangays = [];
                this.selectedProvince = null;
                this.selectedMunicipality = null;
                this.selectedBarangay = null;
            } catch (error) {
                console.error('Error fetching provinces:', error);
            }
        },
        async getMunicipalities() {
            if (!this.subscription.province) return;
            try {
                const response = await axios.get(`/api/v1/municipalities/?province_id=${this.subscription.province}`);
                this.municipalities = response.data;
                this.barangays = [];
                this.selectedMunicipality = null;
                this.selectedBarangay = null;
            } catch (error) {
                console.error('Error fetching municipalities:', error);
            }
        },
        async getBarangays() {
            if (!this.subscription.municipality) return;
            try {
                const response = await axios.get(`/api/v1/barangays/?municipality_id=${this.subscription.municipality}`);
                this.barangays = response.data;
            } catch (error) {
                console.error('Error fetching barangays:', error);
            }
        },
        async getPlans() {
            try {
                const response = await axios.get("/api/v1/plans/");
                this.plans = response.data;
            } catch (error) {
                console.error('Error fetching barangays:', error);
            }
        },
        async getModems() {
            try {
                const response = await axios.get("/api/v1/modems/");
                this.modems = response.data;
            } catch (error) {
                console.error('Error fetching barangays:', error);
            }
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

        collapse() {
            if (this.marking=='+') {
                alert("Yo!");
                this.marking = '-';
            }
            else {
                this.marking = '+';
            }
        },

        // Toggles the collapsible row
        toggleCollapse(subscriptionId) {
            if (this.expandedRows.includes(subscriptionId)) {
                // Collapse the row
                this.expandedRows = this.expandedRows.filter(
                    (id) => id !== subscriptionId
                );
            } else {
                // Expand the row and load billing if not already loaded
                this.expandedRows.push(subscriptionId);
                this.loadBilling(subscriptionId);
            }
        },
        // Load billing information for a subscription
        async loadBilling(subscriptionId) {
            const subscription = this.subscriptions.find(
                (subs) => subs.id === subscriptionId
            );

            // Skip if billings are already loaded
            if (subscription.billings) {
                return;
            }

            try {
                this.loading = true;

                // Replace this URL with your actual API endpoint
                const response = await axios.get(`/api/billings/?subscription=${subscriptionId}`);
                subscription.billings = response.data; // Add billing data to subscription
            } catch (error) {
                console.error("Failed to load billing information:", error);
            } finally {
                this.loading = false;
            }
        },
    }
}
</script>

<template>
    <Layout>
        <pageheader title="Subscription list" pageTitle="Subscriptions" />
        <BRow>
            <BCol class="col-sm-12">
                <BCard no-body class="table-card">
                    <BCardBody>
                        <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2">
                            <!-- Search Input with Magnifying Glass -->
                            <div class="input-group input-group-sm search-bar">
                                <span class="input-group-text">
                                    <i class="ti ti-search"></i> <!-- Magnifying Glass Icon -->
                                </span>
                                <input
                                    v-model="searchQuery"
                                    type="text"
                                    placeholder="Search Subscriptions..."
                                    class="mb-0 form-control form-control-sm"
                                    @keydown.enter="applySearch"
                                />
                            </div>
                            <!-- Add Subscriber Button -->
                                <!-- <router-link to="/add-product" class="btn btn-primary"> <i class="ti ti-plus f-18"></i> Add Region </router-link>-->
                            <BButton variant="primary" class="btn btn-sm" @click="showAddModalOpen">Add Subscription</BButton>
                        </div>
                        <div class="table-responsive">
                            <!-- Show Spinner While Loading -->
                            <div v-if="loading" class="text-center p-4">
                                <BSpinner label="Loading..."></BSpinner>
                            </div>

                            <table v-else class="table table-hover table-sm tbl-product" id="pc-dt-simple">
                                <thead>
                                    <tr>
                                        <th class="text-end">#</th>
                                        <th>Name</th>
                                        <th>Account</th>
                                        <th>Address</th>
                                        <th>Modem</th>
                                        <th>Status/PON/NAP</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(subs, index) in subscriptions" :key="subs.id">
                                        <!-- Main Table Row -->
                                        <td class="text-end">
                                            {{ index + 1 }}
                                            <span
                                                class="ms-1"
                                                @click="toggleCollapse(subs.id)"
                                                style="cursor: pointer;"
                                            >
                                                {{ expandedRows.includes(subs.id) ? '-' : '+' }}
                                            </span>
                                        </td>
                                        <td width="15%">
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ subs.last_name }}, {{ subs.first_name }} {{ subs.middle_name }} {{ subscriber.ext_name }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ subs.id_no }} </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td width="20%">
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ subs.alias }}  
                                                        <span class="badge rounded-pill bg-info text-dark">{{ subs.plan_name }}</span> 
                                                        <span v-if="subs.bill_schedule=='start'" class="badge rounded-circle bg-success">1</span>
                                                        <span v-else-if="subs.bill_schedule=='end'" class="badge rounded-circle bg-primary">2</span>
                                                        <span v-else class="badge rounded-circle bg-warning">0</span>
                                                        <span v-if="subs.is_paid" class="badge bg-success">paid</span>
                                                        <span v-else class="badge bg-danger">unpaid</span>
                                                        <span v-if="subs.is_partial" class="badge bg-warning">partial</span>
                                                    </h6>
                                                    <p class="text-muted f-12 mb-0">{{ subs.no }} | {{ subs.sub_type }} </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td width="45%">
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ subs.purok }}, {{ subs.municipality_name }}, {{ subs.barangay_name }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ subs.region_name }}, {{ subs.province_name }} </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td width="10%">
                                            <BRow class="d-flex">
                                                <BCol>
                                                    <h6 class="mb-1">{{ subs.modem_name }}</h6>
                                                    <p class="text-muted f-12 mb-0">{{ subs.modem_serial}}</p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        
                                        <td class="text-center" width="10%">
                                            <h6 class="mb-1">{{ subs.sub_status }}  <span class="badge rounded-pill bg-warning text-dark">{{ subs.pon_no }}/{{ subs.nap_no }}</span> </h6>
                                            <p class="text-muted f-12 mb-0">{{ formattedDateTimeDate(subs.date_activated)}}<span v-if="subs.sub_status=='terminated'">/ {{ subs.date_terminated }}</span></p>
                                            <div class="prod-action-links">
                                                <ul class="list-inline me-auto mb-0">
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Subscriptions">
                                                        <a href="#" @click="showAddModal(subs.id)" class="avtar avtar-xs btn-link-secondary btn-pc-default">
                                                            <i class="ti ti-eye f-18"></i>
                                                        </a>
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Billing">
                                                        
                                                        <router-link :to="{name: 'billings', query: {sub_id: subs.id}}" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-file-plus f-18"></i>
                                                        </router-link> 
                                                        <!-- 
                                                        <a href="#" @click="getSubscription(subs.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-edit-circle f-18"></i>
                                                            <BoldIcon></BoldIcon>
                                                        </a>
                                                        -->
                                                      
                                                    </li>
                                                    <!--
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                        <a href="#" @click="cancelDelete(subs.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
                                                            <i class="ti ti-trash f-18"></i> 
                                                            
                                                        </a>
                                                    </li>
                                                    -->
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

        <!---Subscriber modal -->
        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        
                        <BModal v-model="modalShow" title="Subscriber" hide-footer class="v-modal-custom" size="lg">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-3">
                                    <label for="first_name" class="col-sm-2 col-form-label">First name</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.first_name" type="text" class="form-control" id="first_name">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-3">
                                    <label for="last_name" class="col-sm-2 col-form-label">Last name</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.last_name" type="text" class="form-control" id="last_name">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-3">
                                    <label for="middle_name" class="col-sm-2 col-form-label">Middle name</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.middle_name" type="text" class="form-control" id="middle_name">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-3">
                                    <label class="col-sm-2 col-form-label" for="ext_name">Name extention</label>
                                    <BCol class="col-sm-2">
                                        <select v-model="subscriber.ext_name" class="form-select" id="ext_name">
                                            <option value="">---</option>
                                            <option value="jr">JR</option>
                                            <option value="sr">SR</option>
                                        </select>
                                    </BCol>

                                    <label for="down" class="col-sm-2 col-form-label">Birth date</label>
                                    <BCol class="col-sm-6">
                                        <flat-pickr v-model="subscriber.birth_date" :first-day-of-week="1" lang="en" confirm
                                        class="form-control"></flat-pickr>
                                    </BCol>
                                </BRow>
                                <BRow class=" md-3">
                                    <label class="col-sm-2 col-form-label" for="marital_status">Marital Status</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="subscriber.marital_status" class="form-select" id="marital_status">
                                            <option value="">---</option>
                                            <option value="single" selected>Single</option>
                                            <option value="married">Married</option>
                                            <option value="widow">Widow</option>
                                            <option value="annulled">Annulled</option>
                                            <option value="separated">Separated</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <br />
                                <BRow class=" md-3">
                                    <label class="col-sm-2 col-form-label" for="gender">Gender</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="subscriber.gender" class="form-select" id="gender">
                                            <option value="">---</option>
                                            <option value="M" selected >Male</option>
                                            <option value="F">Female</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <br />
                                <BRow class=" mb-3">
                                    <label for="contact_no" class="col-sm-2 col-form-label">Contact #</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.contact_no" type="text" class="form-control" id="contact_no">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-3">
                                    <label for="address" class="col-sm-2 col-form-label">Address</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="subscriber.address" class="form-control" id="address" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-3">
                                    <label for="note" class="col-sm-2 col-form-label">Note</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="subscriber.note" class="form-control" id="note" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class="mb-3">
                                    <label for="good" class="col-sm-2 col-form-label">Good?</label>
                                    <BCol class="col-sm-2">
                                        <div class="input-group mb-6">
                                            <div class="form-group form-check">
                                                <input v-model="subscriber.is_good" type="checkbox" class="form-check-input" id="good">
                                            </div>
                                        </div>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="modalShow = !modalShow">Close</button>
                                <button type="button" class="btn btn-primary" @click="updatePlan">Save changes</button>
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