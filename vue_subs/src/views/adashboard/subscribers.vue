<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"
import axios from "axios";
import Swal from "sweetalert2";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { useAuthStore } from '@/stores/auth';
// import bootstrapBundle from "bootstrap/dist/js/bootstrap.bundle";
// import modules from "@/state/modules";


export default {
    name: "SUBSCRIPTIONS",
    components: {
        Layout, pageheader, flatPickr
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
            modalShow2: false,
            modalShow3: false,
            modalShow4: false,
            subscribers: [],
            subscriptions: [],
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
            operationSub: false,
            operationBill: false,
            operationPay: false,
            operationTicket: false,
            genderChoices: [],
            maritalStatusChoices: [],

            regions: [],
            provinces: [],
            municipalities: [],
            barangays: [],
            plans: [],
            modems: [],
            selectedRegion: null,
            selectedProvince: null,
            selectedMunicipality: null,
            selectedBarangay: null,
            subscription:{
                id:"",
                subscriber:"",
                employee:"",
                alias: "",
                bill_schedule: "",
                note: "",
                referred_by: "",
                region:"",
                province:"",
                municipality:"",
                barangay:"",
                purok: "",
                latitude: 0.00,
                longitude: 0.00,
                landmark: "",
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
            },
            searchQuery: "", // Search input
            selectedRow: null, // ID of the selected row
            selectedRowSubs: null,
            selectedRowBill: null,
            bills: [],
            bill: {
                id:"",
                billed_by:"",
                collector: "",
                subscription:"",
                amount_due:"",
                billing_date: "",
                is_paid:"",
                is_partial:"",
                bill_type:"",
                sub_schedule: "",
                notice:"",
                remarks:"",
                billing_no: "",
            },
            payments: [],
            payment: {
                id: "",
                subscription: "",
                bill_no: "",
                amount_paid: "",
                payment_date: "",
                is_paid: false,
                is_partial: false,
                is_cancelled: false,
                remarks: "",
                or_no: "",
                or_ref_no: "",
                payment_type: "",
                cheque_no: "",
                reference_no: "",
                reference_picture: "",
            },
            tickets: [],
            ticket: {
                id: "",
                prepared_by: "",
                assigned_to: "",
                subscription: "",
                subject: "",
                description: "",
                issue: "",
                ticket_date: "",
                ticket_no: "",
                priority: "",
                status: "",
                remarks: "",
                created_on: "",
            },
            users: [],

            /* seard */
            loading: false,
            loading1: false,
            loading2: false,
            loading3: false,
            loading4: false,
        }
    },
    created() {
        this.getSubscribers();
        this.getRegions();
        this.getProvincesAll()
        this.getMunicipalitiesAll();
        this.getBarangaysAll();
        this.getPlans();
        this.getModems();
        this.getIssues();
        this.subscriber={};
    },
    methods: {
        async updatePlan() {
            if (this.operation==false) {
                await axios.post("/api/v1/subscribers/", { 
                    first_name: this.subscriber.first_name,
                    last_name: this.subscriber.last_name,
                    middle_name: this.subscriber.middle_name,
                    ext_name: this.subscriber.ext_name,
                    marital_status: this.subscriber.marital_status,
                    gender: this.subscriber.gender,
                    contact_no: this.subscriber.contact_no,
                    address: this.subscriber.address,
                    birth_date: this.subscriber.birth_date,
                    note: this.subscriber.note,
                    is_good: this.subscriber.is_good,
                    added_by: this.authStore.user.id
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
                await axios.patch(`/api/v1/subscribers/${this.subscriber.id}/`, { 
                    first_name: this.subscriber.first_name,
                    last_name: this.subscriber.last_name,
                    middle_name: this.subscriber.middle_name,
                    ext_name: this.subscriber.ext_name,
                    marital_status: this.subscriber.marital_status,
                    gender: this.subscriber.gender,
                    contact_no: this.subscriber.contact_no,
                    address: this.subscriber.address,
                    birth_date: this.subscriber.birth_date,
                    note: this.subscriber.note,
                    is_good: this.subscriber.is_good,
                    added_by: this.authStore.user.id
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
        },
        async updateSubscription() {
            if (this.operationSub==false){
                await axios.post("/api/v1/subscriptions/", { 
                    subscriber: this.subscriber.id,
                    employee: this.authStore.user.id,
                    alias: this.subscription.alias,
                    bill_schedule: this.subscription.bill_schedule,
                    note: this.subscription.note,
                    referred_by: this.subscription.referred_by,
                    region: this.subscription.region,
                    province: this.subscription.province,
                    municipality: this.subscription.municipality,
                    barangay: this.subscription.barangay,
                    purok: this.subscription.purok,
                    latitude: this.subscription.latitude,
                    longitude: this.subscription.longitude,
                    landmark: this.subscription.landmark,
                    plan: this.subscription.plan,
                    pon_no: this.subscription.pon_no,
                    nap_no: this.subscription.nap_no,
                    modem_serial: this.subscription.modem_serial,
                    modem: this.subscription.modem,
                    sub_status: this.subscription.sub_status,
                    sub_type: this.subscription.sub_type,
                    date_activated: this.subscription.date_activated,
                    date_tetminated: this.subscription.date_terminated,
                    date_suspended: this.subscription.date_suspended,
                    modem_username: this.subscription.modem_username,
                    modem_password: this.subscription.modem_password,
                    created_on: this.getDate()
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow1 = !this.modalShow1;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getSubscriptions(this.subscriber.id);
                });
            }else {
                await axios.patch(`/api/v1/subscriptions/${this.subscription.id}/`, { 
                    subscriber: this.subscriber.id,
                    employee: this.authStore.user.id,
                    alias: this.subscription.alias,
                    bill_schedule: this.subscription.bill_schedule,
                    note: this.subscription.note,
                    referred_by: this.subscription.referred_by,
                    region: this.subscription.region,
                    province: this.subscription.province,
                    municipality: this.subscription.municipality,
                    barangay: this.subscription.barangay,
                    purok: this.subscription.purok,
                    latitude: this.subscription.latitude,
                    longitude: this.subscription.longitude,
                    landmark: this.subscription.landmark,
                    plan: this.subscription.plan,
                    pon_no: this.subscription.pon_no,
                    nap_no: this.subscription.nap_no,
                    modem_serial: this.subscription.modem_serial,
                    modem: this.subscription.modem,
                    sub_status: this.subscription.sub_status,
                    sub_type: this.subscription.sub_type,
                    date_activated: this.subscription.date_activated,
                    date_tetminated: this.subscription.date_terminated,
                    date_suspended: this.subscription.date_suspended,
                    modem_username: this.subscription.modem_username,
                    modem_password: this.subscription.modem_password,
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow1 = !this.modalShow1;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getSubscriptions(this.subscriber.id);
                });
            }
        },
        updateBill() {
            if (this.operationBill==false) {
                axios.post("/api/v1/billings/", { 
                    billed_by: this.authStore.user.id,
                    subscription: this.subscription.id,
                    collector: this.bill.collector,
                    amount_due:this.bill.amount_due,
                    bill_type:this.bill.bill_type,
                    notice: this.bill.notice,
                    remarks: this.bill.remarks
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow2 = !this.modalShow2;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getBills(this.subscription.id);
                });
            } else {
                axios.patch(`/api/v1/billings/${this.bill.id}/`, { 
                    billed_by: this.authStore.user.id,
                    subscription: this.subscription.id,
                    collector: this.bill.collector,
                    amount_due:this.bill.amount_due,
                    bill_type:this.bill.bill_type,
                    notice: this.bill.notice,
                    remarks: this.bill.remarks
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow2 = !this.modalShow2;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getBills(this.subscription.id);
                });
            }
        },
        async updatePayment() {
            if (this.operationPay==false) {
                await axios.post("/api/v1/payments/", { 
                    received_by: this.authStore.user.id,
                    subscription: this.subscription.id,
                    bill_no: this.bill.id,
                    amount_paid: this.payment.amount_paid,
                    payment_date: this.payment.payment_date,
                    is_paid: this.payment.is_paid,
                    is_partial: this.payment.is_partial,
                    is_cancelled: this.payment.is_cancelled,
                    remarks: this.payment.remarks,
                    or_ref_no: this.payment.or_ref_no,
                    payment_type: this.payment.payment_type,
                    cheque_no: this.payment.cheque_no,
                    reference_no: this.payment.reference_no
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow3 = !this.modalShow3;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getPayments(this.bill.id);
                });
            } else {
                await axios.patch(`/api/v1/payments/${this.payment.id}/`, { 
                    received_by: this.authStore.user.id,
                    subscription: this.subscription.id,
                    bill_no: this.bill.id,
                    amount_paid: this.payment.amount_paid,
                    payment_date: this.payment.payment_date,
                    is_paid: this.payment.is_paid,
                    is_partial: this.payment.is_partial,
                    is_cancelled: this.payment.is_cancelled,
                    remarks: this.payment.remarks,
                    or_ref_no: this.payment.or_ref_no,
                    payment_type: this.payment.payment_type,
                    cheque_no: this.payment.cheque_no,
                    reference_no: this.payment.reference_no
                }).then((response) => {
                    console.log(response.data);
                    this.modalShow3 = !this.modalShow3;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getPayments(this.bill.id);
                });
            }
        },
        async updatePayment1() {
            this.payment.is_paid = false;
            this.payment.is_partial = false;
            this.payment.is_cancelled = false;
            if (this.payment.amount_paid >= this.bill.amount_due) {
                this.payment.is_paid = true 
            } else {
                if (this.payment.amount_paid > 0)
                    this.payment.is_partial = true;
            }

            const formData = new FormData();

            // Add all fields to FormData
            formData.append("received_by", this.authStore.user.id);
            formData.append("subscription", this.subscription.id);
            formData.append("bill_no", this.bill.id);
            formData.append("amount_paid", this.payment.amount_paid);
            formData.append("payment_date", this.payment.payment_date);
            formData.append("is_paid", this.payment.is_paid);
            formData.append("is_partial", this.payment.is_partial);
            formData.append("is_cancelled", this.payment.is_cancelled);
            formData.append("remarks", this.payment.remarks);
            formData.append("or_ref_no", this.payment.or_ref_no);
            formData.append("payment_type", this.payment.payment_type);
            formData.append("cheque_no", this.payment.cheque_no);
            formData.append("reference_no", this.payment.reference_no);

            // Add the file (if selected)
            if (this.payment.reference_picture) {
                formData.append("reference_picture", this.payment.reference_picture);
            }

            // Use POST or PATCH based on the operation
            const url = this.operationPay
                ? `/api/v1/payments/${this.payment.id}/`
                : "/api/v1/payments/";

            const method = this.operationPay ? "patch" : "post";

            try {
                const response = await axios({
                    method,
                    url,
                    data: formData,
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                });

                console.log(response.data);
                this.modalShow3 = !this.modalShow3;
                Swal.fire({
                    position: "top-end",
                    icon: "success",
                    title: "Your work has been saved",
                    showConfirmButton: false,
                    timer: 1500,
                });
                this.getPayments(this.bill.id);
            } catch (error) {
                console.error("Error during update:", error);
                Swal.fire({
                    position: "top-end",
                    icon: "error",
                    title: "Failed to save your work",
                    showConfirmButton: false,
                    timer: 1500,
                });
            }
        },
        async updateTicket() {
            console.log(this.ticket.issue);
            if (this.operationTicket==false) {
                await axios.post("/api/v1/tickets/", { 
                    prepared_by: this.authStore.user.id,
                    assigned_to: this.ticket.assigned_to,
                    subscription: this.subscription.id,
                    subject: this.ticket.subject,
                    description: this.ticket.description,
                    ticket_date: this.ticket.ticket_date,
                    priority: this.ticket.priority,
                    status: this.ticket.status,
                    remarks: this.ticket.remarks,
                    created_on: new Date()
                }).then(() => {
                    this.modalShow4 = !this.modalShow4;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getTickets(this.subscription.id);
                });
            } else {
                await axios.patch(`/api/v1/tickets/${this.ticket.id}/`, { 
                    prepared_by: this.authStore.user.id,
                    assigned_to: this.ticket.assigned_to,
                    subscription: this.subscription.id,
                    subject: this.ticket.subject,
                    description: this.ticket.description,
                    ticket_date: this.ticket.ticket_date,
                    priority: this.ticket.priority,
                    status: this.ticket.status,
                    remarks: this.ticket.remarks
                }).then(() => {
                    this.modalShow4 = !this.modalShow4;
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getTickets(this.subscription.id);
                });
            }
        },
        handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                this.payment.reference_picture = file;
            }
            // } else {
            //     this.payment.reference_picture = null;
            // }
        },

        async fetchChoices() {
            try {
                const response = await axios.get('/api/subscriber/choices/');
                this.genderChoices = response.data.gender;
                this.maritalStatusChoices = response.data.marital_status;
            } catch (error) {
                console.error('Error fetching choices:', error);
            }
        },
        async getSubscribers() {
            try {
                await axios.get("/api/v1/subscribers/").then((response)=> {
                    this.subscribers = response.data;
                });
            } catch (error) {
                console.error('Error fetching subscribers:', error);
            }
        },
        async getSubscribersSearch() {
            try {
                const params = {};
                this.loading = true;
                if (this.searchQuery) {
                    params.search = this.searchQuery; // Add search query to parameters
                }
                console.log(params);
                const response = await axios.get("/api/v1/subscribers/", { params });
                this.subscribers = response.data;
            } catch (error) {
                console.error("Error fetching subscribers:", error);
            } finally {
                this.loading = false;
            }
        },
        getDate() {
            let d = new Date();
            return d;
        },
        // Apply search
        applySearch() {
            this.getSubscribersSearch(); // Fetch data with current search query
        },
            // Reset search and fetch all data
        resetSearch() {
            this.searchQuery = ""; // Clear the search input
            this.getSubscribersSearch(); // Fetch all data
        },
        getSubscriber(subs_id) {
            this.modalShow = !this.modalShow;
            this.operation = true;
            axios.get(`/api/v1/subscribers/${subs_id}/`).then((response) => {
                    this.subscriber = response.data;
                }).catch(error => {
                    console.log(JSON.stringify(error));
            });
        },
        async getSubscriber1(subs_id) {
            await axios.get(`/api/v1/subscribers/${subs_id}/`).then((response) => {
                    this.subscriber = response.data;
                }).catch(error => {
                    console.log(JSON.stringify(error));
            });
        },
        getSubscriberSubs(subs_id) {
            axios.get(`/api/v1/subscribers/${subs_id}/`).then((response) => {
                    this.subscriber = response.data;
                }).catch(error => {
                    console.log(JSON.stringify(error));
            });
        },
        async deleteSubscriber(subs_id) {
            try {
                await axios.delete(`/api/v1/subscribers/${subs_id}/`).then(() => {
                    this.subscribers = this.subscribers.filter((subs) => subs.id !== subs_id);
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async deleteSubscription(id) {
            try {
                await axios.delete(`/api/v1/subscriptions/${id}/`).then(() => {
                    this.subscriptions = this.subscriptions.filter((subs) => subs.id !== id);
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        showAddModal() {
            this.subscriber = {};
            this.modalShow = !this.modalShow;
            this.operation = false;
        },
        showAddModalOpen() {
            // this.getSubscriberSubs(id_no);
            this.subscription = {};
            this.modalShow1 = true;
            this.operationSub = false;
        },
        showAddModalClose() {
            // this.subscriber = {};
            this.subscription = {};
            this.modalShow1 = false;
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
                        this.deleteSubscriber(subs_id);
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
        cancelDeleteSubs(id) {
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
                        this.deleteSubscription(id);
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
        async getProvincesAll() {
            try {
                const response = await axios.get('/api/v1/provinces/');
                this.provinces = response.data;
            } catch (error) {
                console.error('Error fetching probinces:', error);
            }
        },
        async getMunicipalitiesAll() {
            try {
                const response = await axios.get('/api/v1/municipalities/');
                this.municipalities = response.data;
            } catch (error) {
                console.error('Error fetching municipalities:', error);
            }
        },
        async getBarangaysAll() {
            try {
                const response = await axios.get('/api/v1/barangays/');
                this.barangays = response.data;
            } catch (error) {
                console.error('Error fetching barangays:', error);
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
        selectRow(rowId) {
            this.loading1=false;
            this.selectedRow = rowId; // Set the selected row's ID
            this.getSubscriber1(rowId);
            this.getSubscriptions(rowId);
            this.goToStartTab();
        },
        selectRowSubs(rowId) {
            this.selectedRowSubs = rowId; // Set the selected row's ID
            this.subscription={};
            // this.getSubscriber1(rowId);
            // this.getSubscriptions(rowId);
        },
        selectRowBills(rowId) {
            this.selectedRowBill = rowId; // Set the selected row's ID
            this.bill={};
            // this.getSubscriber1(rowId);
            // this.getSubscriptions(rowId);
        },

        // Fetch data with optional search query
        async getSubscriptions(id) {
            try {
                this.loading1=true;
                const response = await axios.get(`/api/v1/subscriptions/?id=${id}`);
                this.subscriptions = response.data;
            } catch (error) {
                console.error("Error fetching subscriptions:", error);
            } finally {
                this.loading1=false;
            }
        },
        async getSubscription(id){
            try {
                const response = await axios.get(`/api/v1/subscriptions/${id}/`);
                this.subscription = response.data;
                this.modalShow1 = !this.modalShow1;
                this.operationSub = true;
            } catch (error) {
                console.error("Error fetching subscription:", error);
            }
        },
        async goToNextTab(id) {
            // Select the second tab
            
            const secondTab = document.querySelector('#analytics-tab-2');
            // Trigger a click event on the tab button to activate it
            if (secondTab) {
                secondTab.click();
                try {
                    const response = await axios.get(`/api/v1/subscriptions/${id}/`);
                    this.subscription = response.data;
                    this.getBills(id);
                    this.getTickets(id);
                } catch (error) {
                    console.error("Error fetching billing:", error);
                }
            }
        },
        goToStartTab(){
            const startTab = document.querySelector('#analytics-tab-1');
            if (startTab){
                startTab.click();
            }
        },
        async goToNextTabPay(id) {
            // Select the second tab
            
            const thirdTab = document.querySelector('#analytics-tab-3');
            // Trigger a click event on the tab button to activate it
            if (thirdTab) {
                thirdTab.click();
                try {
                    this.loading3=true;
                    const response = await axios.get(`/api/v1/billings/${id}/`);
                    this.bill = response.data;
                    this.getPayments(id);
                } catch (error) {
                    console.error("Error fetching payments:", error);
                } finally {
                    this.loading3=false;
                }
            }
        },
        
        // billing
        showAddModalBillOpen() {
            this.bill={};
            this.getUsers();
            this.bill.billing_date = new Date();
            if (this.subscription) {
                this.bill.amount_due = this.subscription.plan_amount;
            }
            this.modalShow2=!this.modalShow2;
            this.operationBill = false;
        },
        showAddModalBillClose() {
            this.modalShow2=!this.modalShow2;
            this.operationBill=false;
            this.bill = {};
        },
        async getBill(id) {
            try {
                this.getUsers();
                this.modalShow2=!this.modalShow2;
                this.operationBill=true;
                await axios.get(`/api/v1/billings/${id}/`).then((response) => {
                        this.bill = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async getBill1(id) {
            try {
                await axios.get(`/api/v1/billings/${id}/`).then((response) => {
                        this.bill = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async getBills(id) {
            try {
                this.loading2=true;
                await axios.get(`/api/v1/billings/?id=${id}`).then((response) => {
                        this.bills = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            } finally {
                this.loading2=false;
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

        // payment
        showAddModalPaymentOpen() {
            this.payment={};
            if (this.bill){
                this.payment.amount_paid = this.bill.amount_due;
            }
            this.modalShow3=!this.modalShow3;
            this.operationPay = false;
        },
        showAddModalPaymentClose() {
            this.modalShow3=!this.modalShow3;
            this.operationBill=false;
            this.payment = {};
        },
        async getPayment(id) {
            try {
                this.modalShow3=!this.modalShow3;
                this.operationPay=true;
                await axios.get(`/api/v1/payments/${id}/`).then((response) => {
                        this.payment = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async getPayment1(id) {
            try {
                await axios.get(`/api/v1/payments/${id}/`).then((response) => {
                        this.payment = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async getPayments(id) {
            try {
                this.loading3=true;
                await axios.get(`/api/v1/payments/?id=${id}`).then((response) => {
                        this.payments = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            } finally {
                this.loading3=false;
            }
        },
        async deletePayment(id) {
            try {
                await axios.delete(`/api/v1/payments/${id}/`).then(() => {
                    this.payments = this.payments.filter((pay) => pay.id !== id);
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        cancelDeletePayment(id) {
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
                        this.deletePayment(id);
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

        /* ticket */
        showAddModalTicketOpen() {
            this.ticket={};
            this.getUsers();
            this.ticket.ticket_date = new Date();
            this.modalShow4=!this.modalShow4;
            this.operationTicket = false;
        },
        showAddModalTicketClose() {
            this.modalShow4=!this.modalShow4;
            this.operationTicket=false;
            this.ticket = {};
        },
        async getIssues() {
            try {
                await axios.get("/api/v1/issues/").then((response) => { this.issues = response.data });
            } catch (error) {
                console.error("Error fetching issues:", error);
            }
        },
        async getTicket(id) {
            try {
                this.getUsers();
                this.modalShow4=!this.modalShow4;
                this.operationTicket=true;
                await axios.get(`/api/v1/tickets/${id}/`).then((response) => {
                        this.ticket = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async getTicket1(id) {
            try {
                await axios.get(`/api/v1/tickets/${id}/`).then((response) => {
                        this.ticket = response.data;
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        async getTickets(id) {
            try {
                this.loading4 = true;
                await axios.get(`/api/v1/tickets/?id=${id}`).then((response) => {
                        this.tickets = response.data;
                        console.log(this.tickets);
                    }).catch(error => {
                        console.log(JSON.stringify(error));
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            } finally {
                this.loading4 = false;
            }
        },
        async deleteTicket(id) {
            try {
                await axios.delete(`/api/v1/tickets/${id}/`).then(() => {
                    this.tickets = this.tickets.filter((ticket) => ticket.id !== id);
                });
            } catch(error) {
                console.log(JSON.stringify(error));
            }
        },
        cancelDeleteTicket(id) {
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
                        this.deleteTicket(id);
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
        <pageheader title="Subscribers list" pageTitle="Subscribers" />
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
                                        placeholder="Search Subscribers..."
                                        class="form-control form-control-sm"
                                        @keydown.enter="applySearch"
                                    />
                                </div>
                                <!-- Add Subscriber Button -->
                                <BButton variant="primary" class="btn btn-sm" @click="showAddModal">Add Subscriber</BButton>
                            </div>
                            <!-- Fixed height and scrollable table -->
                            <div class="table-responsive fixed-height">
                                <!-- Show Spinner While Loading -->
                                <div v-if="loading" class="text-center p-4">
                                    <BSpinner label="Loading..."></BSpinner>
                                </div>
                                <table v-else class="table table-hover table-sm tbl-product" id="pc-dt-simple">
                                    <thead>
                                    <tr>
                                        <th class="text-end">#</th>
                                        <th>Name</th>
                                        <th>Marital/Gender</th>
                                        <th>Contact</th>
                                        <th>Address</th>
                                        <th>birth_date</th>
                                        <th>Good?</th>
                                        <th class="text-end">Added/Updated</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="(subscriber, index) in subscribers" 
                                        :key="subscriber.id" 
                                        :class="{ 'table-active': selectedRow === subscriber.id }"
                                        @click="selectRow(subscriber.id)">

                                        <td class="text-end">{{ index + 1 }}</td>
                                        <td>
                                        <BRow class="d-flex">
                                            <BCol>
                                            <h6 class="mb-1">
                                                {{ subscriber.last_name }}, {{ subscriber.first_name }}
                                                {{ subscriber.middle_name }} {{ subscriber.ext_name }}
                                            </h6>
                                            <p class="text-muted f-12 mb-0">
                                                {{ subscriber.id_no }} - {{ subscriber.added_by }}
                                            </p>
                                            </BCol>
                                        </BRow>
                                        </td>
                                        <td>{{ subscriber.marital_status }}/{{ subscriber.gender }}</td>
                                        <td>{{ subscriber.contact_no }}</td>
                                        <td>{{ subscriber.address }}</td>
                                        <td>{{ formattedBirthDate(subscriber.birth_date) }}</td>
                                        <td class="text-start">
                                        <i
                                            v-if="subscriber.is_good"
                                            class="ph-duotone ph-check-circle text-success f-24"
                                            data-bs-toggle="tooltip"
                                            data-bs-title="success"
                                        ></i>
                                        <i
                                            v-else
                                            class="ph-duotone ph-x-circle text-danger f-24"
                                            data-bs-toggle="tooltip"
                                            data-bs-title="danger"
                                        ></i>
                                        </td>
                                        <td class="text-center">
                                        {{ formattedDateTime(subscriber.added_on) }}
                                        <div class="prod-action-links">
                                            <ul class="list-inline me-auto mb-0">
                                            <li
                                                class="list-inline-item align-bottom"
                                                data-bs-toggle="tooltip"
                                                title="Subscriptions"
                                            >
                                                <a
                                                href="#"
                                                @click="showAddModalOpen(subscriber.id)"
                                                class="avtar avtar-xs btn-link-secondary btn-pc-default"
                                                >
                                                <i class="ti ti-eye f-18"></i>
                                                </a>
                                            </li>
                                            <li
                                                class="list-inline-item align-bottom"
                                                data-bs-toggle="tooltip"
                                                title="Edit"
                                            >
                                                <a
                                                href="#"
                                                @click="getSubscriber(subscriber.id)"
                                                class="avtar avtar-xs btn-link-success btn-pc-default"
                                                >
                                                <i class="ti ti-edit-circle f-18"></i>
                                                </a>
                                            </li>
                                            <li
                                                class="list-inline-item align-bottom"
                                                data-bs-toggle="tooltip"
                                                title="Delete"
                                            >
                                                <a
                                                href="#"
                                                @click="cancelDelete(subscriber.id)"
                                                class="avtar avtar-xs btn-link-danger btn-pc-default"
                                                >
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


        <!---Subscriber modal -->
        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        
                        <BModal v-model="modalShow" title="Subscriber" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-1">
                                    <label for="first_name" class="col-sm-2 col-form-label form-control-sm">First</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.first_name" type="text" class="form-control form-control-sm" id="first_name">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="last_name" class="col-sm-2 col-form-label form-control-sm">Last</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.last_name" type="text" class="form-control form-control-sm" id="last_name">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="middle_name" class="col-sm-2 col-form-label form-control-sm">Middle</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.middle_name" type="text" class="form-control form-control-sm" id="middle_name">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="ext_name">Ext.</label>
                                    <BCol class="col-sm-3">
                                        <select v-model="subscriber.ext_name" class="form-select form-select-sm" id="ext_name">
                                            <option value="">---</option>
                                            <option value="jr">JR</option>
                                            <option value="sr">SR</option>
                                        </select>
                                    </BCol>

                                    <label for="down" class="col-sm-2 col-form-label form-control-sm">Birth date</label>
                                    <BCol class="col-sm-5">
                                        <flat-pickr v-model="subscriber.birth_date" :first-day-of-week="1" lang="en" confirm
                                        class="form-control form-control-sm"></flat-pickr>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="marital_status">Status</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="subscriber.marital_status" class="form-select form-select-sm" id="marital_status">
                                            <option value="">---</option>
                                            <option value="single" selected>Single</option>
                                            <option value="married">Married</option>
                                            <option value="widow">Widow</option>
                                            <option value="annulled">Annulled</option>
                                            <option value="separated">Separated</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="gender">Gender</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="subscriber.gender" class="form-select form-select-sm" id="gender">
                                            <option value="">---</option>
                                            <option value="M" selected >Male</option>
                                            <option value="F">Female</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="contact_no" class="col-sm-2 col-form-label form-control-sm">Contact #</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscriber.contact_no" type="text" class="form-control form-control-sm" id="contact_no">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="address" class="col-sm-2 col-form-label form-control-sm">Address</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="subscriber.address" class="form-control form-control-sm" id="address" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="note" class="col-sm-2 col-form-label form-control-sm">Note</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="subscriber.note" class="form-control form-control-sm" id="note" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class="mb-1">
                                    <label for="good" class="col-sm-2 col-form-label form-control-sm">Good?</label>
                                    <BCol class="col-sm-2">
                                        <div class="input-group mb-6">
                                            <div class="form-group form-check">
                                                <input v-model="subscriber.is_good" type="checkbox" class="form-check-input form-check-sm" id="good">
                                            </div>
                                        </div>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal" @click="modalShow = !modalShow">Close</button>
                                <button type="button" class="btn btn-primary btn-sm" @click="updatePlan">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>

        <!---Subscription modal -->
        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        <BModal v-model="modalShow1" title="Subscription Plan" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-10">
                                    <BCol class="mb-1">
                                        <div class="col-sm-10 text-center">
                                            <h5 class="mb-1">{{ subscriber.last_name }}, {{ subscriber.first_name }}</h5>
                                            <span text-muted f-12 mb-0>{{ subscriber.id_no }}</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <hr />
                                <BRow class=" mb-1">
                                    <label for="alias" class="col-sm-2 col-form-label form-control-sm">Account</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscription.alias" type="text" class="form-control form-select-sm" id="alias">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="plan" class="col-sm-2 col-form-label form-control-sm">Plan</label>
                                    <BCol class="col-sm-3">
                                        <select id="region" v-model="subscription.plan" class="form-select form-select-sm">
                                            <option v-for="plan in plans" :key="plan.id" :value="plan.id">{{ plan.plan_name }}</option>
                                        </select>
                                    </BCol>
                                    <label for="sub_type" class="col-sm-2 col-form-label form-control-sm">Type</label>
                                    <BCol class="col-sm-5">
                                        <select id="sub_type" v-model="subscription.sub_type" class="form-select form-select-sm">
                                            <option value="">---</option>
                                            <option value="government">Government</option>
                                            <option value="vendo">Vendo</option>\
                                            <option value="residential">Residential</option>
                                            <option value="business">Business</option>
                                            <option value="vip">VIP</option>
                                            <option value="test">Testing</option>
                                            <option value="employee">Employee</option>
                                            <option value="stations">Station</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="modem" class="col-sm-2 col-form-label form-control-sm">Modem</label>
                                    <BCol class="col-sm-3">
                                        <select id="modem" v-model="subscription.modem" class="form-select form-select-sm">
                                            <option v-for="modem in modems" :key="modem.id" :value="modem.id">{{ modem.modem_brand }}</option>
                                        </select>
                                    </BCol>
                                    <label for="serial_no" class="col-sm-2 col-form-label form-control-sm">Serial #</label>
                                    <BCol class="col-sm-5">
                                        <input v-model="subscription.modem_serial" type="text" class="form-control form-control-sm" id="serial_no">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="pon_no" class="col-sm-2 col-form-label form-control-sm">PON #</label>
                                    <BCol class="col-sm-3">
                                        <input v-model="subscription.pon_no" type="text" class="form-control form-control-sm" id="pon_no">
                                    </BCol>
                                    <label for="nap_no" class="col-sm-2 col-form-label form-control-sm">NAP #</label>
                                    <BCol class="col-sm-5">
                                        <input v-model="subscription.nap_no" type="text" class="form-control form-control-sm" id="nap_no">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="region" class="col-sm-2 col-form-label form-control-sm">Region</label>
                                    <BCol class="col-sm-10">
                                        <select id="region" v-model="subscription.region" @change="getProvinces" class="form-select form-select-sm">
                                            <option v-for="region in regions" :key="region.id" :value="region.id">{{ region.name }}</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <div v-if="provinces.length | subscription?.province">
                                    <BRow class=" mb-1">
                                        <label for="province" class="col-sm-2 col-form-label form-control-sm">Province</label>
                                        <BCol class="col-sm-10">
                                            <select id="province" v-model="subscription.province" @change="getMunicipalities" class="form-select form-select-sm">
                                                <option v-for="province in provinces" :key="province.id" :value="province.id">{{ province.name }}</option>
                                            </select>
                                        </BCol>
                                    </BRow>
                                </div>
                                <div v-if="municipalities.length">
                                    <BRow class=" mb-1">
                                        <label for="municipality" class="col-sm-2 col-form-label form-control-sm">Municipality</label>
                                        <BCol class="col-sm-10">
                                            <select id="municipality" v-model="subscription.municipality" @change="getBarangays" class="form-select form-select-sm">
                                                <option v-for="municipality in municipalities" :key="municipality.id" :value="municipality.id">{{ municipality.name }}</option>
                                            </select>
                                        </BCol>
                                    </BRow>
                                </div>
                                <div v-if="barangays.length">
                                    <BRow class=" mb-1">
                                        <label for="barangay" class="col-sm-2 col-form-label form-control-sm">Barangay</label>
                                        <BCol class="col-sm-10">
                                            <select id="barangay" v-model="subscription.barangay" class="form-select form-select-sm">
                                                <option v-for="barangay in barangays" :key="barangay.id" :value="barangay.id">{{ barangay.name }}</option>
                                            </select>
                                        </BCol>
                                    </BRow>
                                </div>
                                <BRow class=" mb-1">
                                    <label for="purok" class="col-sm-2 col-form-label form-control-sm">Purok</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscription.purok" type="text" class="form-control form-control-sm" id="purok" />
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="latitude">Latitude</label>
                                    <BCol class="col-sm-4">
                                        <input v-model="subscription.latitude" type="text" class="form-control form-control-sm" id="latitude">
                                    </BCol>

                                    <label for="longitude" class="col-sm-2 col-form-label form-control-sm">Longitude</label>
                                    <BCol class="col-sm-4">
                                        <input v-model="subscription.longitude" class="form-control form-control-sm" id="longitude">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="schedule">Schedule</label>
                                    <BCol class="col-sm-6">
                                        <select v-model="subscription.bill_schedule" class="form-select form-select-sm" id="schedule">
                                            <option value="">---</option>
                                            <option value="start">Sart</option>
                                            <option value="end">End</option>
                                            <option value="others">Others</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="landmark" class="col-sm-2 col-form-label form-control-sm">Landmark</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="subscription.landmark" type="text" class="form-control form-control-sm" id="landmark" rows="2"></textarea>
                                    </BCol>
                                </BRow>
                                <BRow class=" md-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="sub_status">Status</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="subscription.sub_status" class="form-select form-select-sm" id="sub_status">
                                            <option value="">---</option>
                                            <option value="active">Active</option>
                                            <option value="suspended">Suspended</option>
                                            <option value="terminated">Terminated</option>
                                            <option value="pending">Pending</option>
                                            <option value="warning">Warning</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <br />
                                <div v-if="subscription.sub_status=='active'" class="mb-1"> 
                                    <BRow class=" md-1">
                                        <label class="col-sm-2 col-form-label form-control-sm" for="date_activated">Activated on?</label>
                                        <BCol class="col-sm-10">
                                            <flat-pickr v-model="subscription.date_activated" :first-day-of-week="1" lang="en" confirm class="form-control form-control-sm"></flat-pickr>
                                        </BCol>
                                    </BRow>
                                </div>
                                <div v-if="subscription.sub_status=='suspended'" class="mb-1">
                                    <BRow class=" md-1">
                                        <label class="col-sm-2 col-form-label form-control-sm" for="date_suspended">Suspended on?</label>
                                        <BCol class="col-sm-10">
                                            <flat-pickr v-model="subscription.date_suspended" :first-day-of-week="1" lang="en" confirm
                                        class="form-control form-control-sm"></flat-pickr>
                                        </BCol>
                                    </BRow>
                                </div>
                                <div v-if="subscription.sub_status=='terminated'" class="mb-1">
                                    <BRow class=" md-1">
                                        <label class="col-sm-2 col-form-label form-control-sm" for="date_terminated">Terminated on?</label>
                                        <BCol class="col-sm-10">
                                            <flat-pickr v-model="subscription.date_terminated" :first-day-of-week="1" lang="en" confirm
                                        class="form-control form-control-sm"></flat-pickr>
                                        </BCol>
                                    </BRow>
                                </div>
                                <BRow class=" mb-1">
                                    <label for="modem_username" class="col-sm-2 col-form-label form-control-sm">User</label>
                                    <BCol class="col-sm-4">
                                        <input v-model="subscription.modem_username" type="text" class="form-control form-control-sm" id="modem_username">
                                    </BCol>
                                    <label for="modem_password" class="col-sm-2 col-form-label form-control-sm">Password</label>
                                    <BCol class="col-sm-4">
                                        <input v-model="subscription.modem_password" type="text" class="form-control form-control-sm" id="modem_password">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="reffered_by" class="col-sm-2 col-form-label form-control-sm">Ref. by</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="subscription.referred_by" class="form-control form-control-sm" id="reffered_by" />
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="note" class="col-sm-2 col-form-label form-control-sm">Note</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="subscription.note" class="form-control form-control-sm" id="note" rows="2"></textarea>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="showAddModalClose">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updateSubscription">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>
        <!-- Subscription modal-->

        <!-- Billing modal -->
        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        <BModal v-model="modalShow2" title="Billing" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-10">
                                    <BCol class="mb-1">
                                        <div class="col-sm-10 text-center">
                                            <h5 class="mb-1">{{ subscriber.last_name }}, {{ subscriber.first_name }}</h5>
                                            <span text-muted f-12 mb-0>{{ subscription.no }}</span>
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
                                        <select v-model="bill.collector" name="collector" id="" class="form-control form-select-sm">
                                            <option v-for="user in users" :key="user.id" :value="user.id">{{ user.first_name }} {{ user.last_name }}</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="date_suspended">Date</label>
                                    <BCol class="col-sm-6">
                                        <flat-pickr v-model="bill.billing_date" :first-day-of-week="1" lang="en" confirm
                                    class="form-control form-control-sm"></flat-pickr>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="amount" class="col-sm-2 col-form-label form-control-sm">Due</label>
                                    <BCol class="col-sm-6">
                                        <div class="input-group input-group-sm mb-1">
                                            <span class="input-group-text">Php</span>
                                            <input v-model="bill.amount_due" type="text" class="form-control form-control-sm text-end" aria-label="Amount (to the nearest peso)" id="amount">
                                            <span class="input-group-text">.00</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="type">Schedule</label>
                                    <BCol class="col-sm-6">
                                        <select v-model="bill.bill_type" class="form-select form-select-sm" id="type">
                                            <option value="">---</option>
                                            <option value="start">Sart</option>
                                            <option value="end">End</option>
                                            <option value="others">Others</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="notice">Notice</label>
                                    <BCol class="col-sm-6">
                                        <select v-model="bill.notice" class="form-select form-select-sm" id="notice">
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
                                        <textarea v-model="bill.remarks" class="form-control form-control-sm" id="remarks" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="showAddModalBillClose">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updateBill">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>

         <!-- Payment modal -->
         <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        <BModal v-model="modalShow3" title="Payment" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-10">
                                    <BCol class="mb-1">
                                        <div class="col-sm-10 text-center">
                                            <h5 class="mb-1">{{ subscriber.last_name }}, {{ subscriber.first_name }}</h5>
                                            <span text-muted f-12 mb-0>{{ subscription.no }} - {{ subscription.alias }} | {{ bill.billing_no }}</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <hr />
                                <BRow class=" mb-1">
                                    <label for="alias" class="col-sm-2 col-form-label form-control-sm">Cashier</label>
                                    <BCol class="col-sm-10">
                                        <h5>{{ authStore.user.last_name }}, {{ authStore.user.first_name }}</h5>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="date_payment">Date</label>
                                    <BCol class="col-sm-6">
                                        <flat-pickr v-model="payment.payment_date" :first-day-of-week="1" lang="en" confirm
                                    class="form-control form-control-sm"></flat-pickr>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="or_ref" class="col-sm-2 col-form-label form-control-sm">OR #</label>
                                    <BCol class="col-sm-6">
                                        <input v-model="payment.or_ref_no" class="form-control form-control-sm" id="or_ref">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="amount" class="col-sm-2 col-form-label form-control-sm">Due</label>
                                    <BCol class="col-sm-6">
                                        <div class="input-group input-group-sm">
                                            <span class="input-group-text">Php</span>
                                            <input v-model="payment.amount_paid" type="text" class="form-control form-control-sm text-end" aria-label="Amount (to the nearest peso)" id="amount">
                                            <span class="input-group-text">.00</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="type">Type</label>
                                    <BCol class="col-sm-6">
                                        <select v-model="payment.payment_type" class="form-select form-select-sm" id="type">
                                            <option value="">---</option>
                                            <option value="cash">Cash</option>
                                            <option value="cheque">Cheque</option>
                                            <option value="gcash">GCash</option>
                                            <option value="maya">Maya</option>
                                            <option value="bank">Bank</option>
                                        </select>
                                    </BCol>
                                    <div v-if="payment.payment_type=='cheque'" class="mt-2">
                                        <BRow class=" mb-1">
                                            <label for="cheque" class="col-sm-2 col-form-label form-control-sm">Cheque #</label>
                                            <BCol class="col-sm-5">
                                                <input v-model="payment.cheque_no" type="text" class="form-control form-control-sm" id="cheque">
                                            </BCol>
                                        </BRow>
                                    </div>
                                    <div v-if="payment.payment_type=='gcash' || payment.payment_type=='maya' || payment.payment_type=='bank'" class="mt-2 ">
                                        <BRow class=" mb-1">
                                            <label for="gcash" class="col-sm-2 col-form-label form-control-sm">Ref. #</label>
                                            <BCol class="col-sm-5">
                                                <input v-model="payment.reference_no" type="text" class="form-control form-control-sm" id="gcash">
                                            </BCol>
                                        </BRow>
                                    </div>
                                    <div v-if="payment.payment_type=='gcash' || payment.payment_type=='maya' || payment.payment_type=='bank'" class="form-file mt-2">
                                        <BRow class="mb-1">
                                            <label for="gcash" class="col-sm-2 col-form-label form-control-sm">Image</label>
                                            <BCol class="col-sm-10">
                                                <input @change="handleFileUpload" type="file" accept="image/*" class="form-control form-control-sm" aria-label="file example">
                                                <div class="invalid-feedback">Example invalid form file feedback</div>
                                            </BCol>
                                        </BRow>
                                    </div>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="remarks" class="col-sm-2 col-form-label">Remarks</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="payment.remarks" class="form-control form-control-sm" id="remarks" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="showAddModalPaymentClose">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updatePayment1">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>

        <!-- Ticket modal -->
        <BRow>
            <BCol sm="12">
                <BCardBody class="pc-component">
                    <div>
                        <BModal v-model="modalShow4" title="Ticket" hide-footer class="v-modal-custom" size="md">
                            <div class="modal-body  p-0">
                                <BRow class=" mb-10">
                                    <BCol class="mb-1">
                                        <div class="col-sm-10 text-center">
                                            <h5 class="mb-1">{{ subscriber.last_name }}, {{ subscriber.first_name }}</h5>
                                            <span text-muted f-12 mb-0>{{ subscription.no }}</span>
                                        </div>
                                    </BCol>
                                </BRow>
                                <hr />
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm">User</label>
                                    <BCol class="col-sm-10">
                                        <h6>{{ authStore.user.last_name }}, {{ authStore.user.first_name }}</h6>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="assigned_to">To</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="ticket.assigned_to" class="form-select form-select-sm" id="assigned_to">
                                            <option v-for="user in users" :key="user.id" :value="user.id">{{ user.first_name }} {{ user.last_name }}</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="date_ticket">Date</label>
                                    <BCol class="col-sm-6">
                                        <flat-pickr v-model="ticket.ticket_date" :first-day-of-week="1" lang="en" confirm
                                    class="form-control form-control-sm" id="date_ticket"></flat-pickr>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="or_ref" class="col-sm-2 col-form-label form-control-sm" id="subject">Subject</label>
                                    <BCol class="col-sm-10">
                                        <input v-model="ticket.subject" class="form-control form-control-sm" id="or_ref">
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="or_ref" class="col-sm-2 col-form-label form-control-sm" id="description">Description</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="ticket.description" class="form-control form-control-sm" id="description"></textarea>
                                    </BCol>
                                </BRow>
                                <!--
                                <BRow class=" mb-3">
                                    <label for="issue" class="col-sm-2 col-form-label">Issue</label>
                                    <BCol class="col-sm-10">
                                        <select v-model="ticket.issue" class="form-select" id="issue">
                                            <option v-for="issue in issues" :key="issue.id" :value="issue.id">{{ issue.name }}</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                -->
                                <BRow class=" mb-1">
                                    <label class="col-sm-2 col-form-label form-control-sm" for="priority">Priority</label>
                                    <BCol class="col-sm-4">
                                        <select v-model="ticket.priority" class="form-select form-select-sm" id="priority">
                                            <option value="">---</option>
                                            <option value="low">Low</option>
                                            <option value="medium">Medium</option>
                                            <option value="high">High</option>
                                        </select>
                                    </BCol>
                                    <label for="status" class="col-sm-2 col-form-label form-select-sm">Status</label>
                                    <BCol class="col-sm-4">
                                        <select v-model="ticket.status" class="form-select form-select-sm" id="status">
                                            <option value="">---</option>
                                            <option value="pending">Pending</option>
                                            <option value="inprogress">In progress</option>
                                            <option value="resolved">Resolved</option>
                                        </select>
                                    </BCol>
                                </BRow>
                                <BRow class=" mb-1">
                                    <label for="remarks" class="col-sm-2 form-control-sm col-form-label">Remarks</label>
                                    <BCol class="col-sm-10">
                                        <textarea v-model="ticket.remarks" class="form-control form-control-sm" id="remarks" rows="3"></textarea>
                                    </BCol>
                                </BRow>
                            </div>
                            <div class="modal-footer pb-0">
                                <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal" @click="showAddModalTicketClose">Close</button>
                                <button type="button" class="btn btn-sm btn-primary" @click="updateTicket">Save changes</button>
                            </div>
                        </BModal>
                    </div>

                </BCardBody>
            </BCol>
        </BRow>

            <div v-if="subscriber.id > 0" class="col-12">
                <div class="card">
                    <div class="card-body">
                        <ul class="nav nav-tabs invoice-tab border-bottom mb-3" id="myTab" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button class="nav-link active" id="analytics-tab-1" data-bs-toggle="tab" data-bs-target="#analytics-tab-1-pane" type="button" role="tab" aria-controls="analytics-tab-1-pane" aria-selected="true">
                                    <span class="d-flex align-items-center gap-2">Subscriptions <span class="avtar rounded-circle bg-light-primary">{{ subscriptions.length }}</span></span>
                                </button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="analytics-tab-2" data-bs-toggle="tab" data-bs-target="#analytics-tab-2-pane" type="button" role="tab" aria-controls="analytics-tab-2-pane" aria-selected="false">
                                    <span class="d-flex align-items-center gap-2">Billings <span class="avtar rounded-circle bg-light-success">{{ bills.length }}</span></span>
                                </button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="analytics-tab-3" data-bs-toggle="tab" data-bs-target="#analytics-tab-3-pane" type="button" role="tab" aria-controls="analytics-tab-3-pane" aria-selected="false">
                                    <span class="d-flex align-items-center gap-2">Payments <span class="avtar rounded-circle bg-light-warning">{{ payments.length }}</span></span>
                                </button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="analytics-tab-4" data-bs-toggle="tab" data-bs-target="#analytics-tab-4-pane" type="button" role="tab" aria-controls="analytics-tab-4-pane" aria-selected="false">
                                    <span class="d-flex align-items-center gap-2">Tickets <span class="avtar rounded-circle bg-light-danger">{{ tickets.length }}</span></span>
                                </button>
                            </li>
                        </ul>
                        <div class="tab-content" id="myTabContent">
                            <div class="tab-pane fade show active" id="analytics-tab-1-pane" role="tabpanel" aria-labelledby="analytics-tab-1" tabindex="0">
                                <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2">
                                    <!-- Search Input with Magnifying Glass -->
                                    <div class="input-group search-bar">
                                        <div class="col-sm-12">
                                            <h5>{{ subscriber.last_name }}, {{ subscriber.first_name }} 
                                                {{ subscriber.middle_name }} {{ subscriber.ext_name }}</h5>
                                        </div>
                                        <p text-muted f-12 mb-0>{{ subscriber.id_no }}</p>
                                    </div>
                                    
                                    <!-- Add Subscriber Button -->
                                    <BButton variant="primary" class="btn btn-sm" @click="showAddModalOpen">Add Subscriptions</BButton>
                                </div>
                                <div class="table-responsive fixed-height">
                                    <!-- Show Spinner While Loading -->
                                    <div v-if="loading1" class="text-center p-4">
                                        <BSpinner label="Loading..."></BSpinner>
                                    </div>
                                    <table v-else class="table table-hover table-sm tbl-product" id="pc-dt-simple-1">
                                        <thead>
                                            <tr>
                                                <th class="text-end">#</th>
                                                <th>Account</th>
                                                <th>Address</th>
                                                <th>Plan/Type</th>
                                                <th>Modem</th>
                                                <th>PON/NAP</th>
                                                <th>Status/Date</th>
                                                <th class="text-end">Refererence</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(subs, index) in subscriptions" :key="subs.id" 
                                                :class="{ 'table-active': selectedRowSubs === subs.id}"
                                                @click="selectRowSubs(subs.id)"
                                                @dblclick="goToNextTab(subs.id)">

                                                <td class="text-end">{{index + 1}}</td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">
                                                                {{ subs.alias }}
                                                                <span v-if="subs.bill_schedule=='start'" class="badge rounded-circle bg-success">1</span>
                                                                <span v-else-if="subs.bill_schedule=='end'" class="badge rounded-circle bg-primary">2</span>
                                                                <span v-else class="badge rounded-circle bg-warning">0</span>
                                                            </h6>
                                                            <p class="text-muted f-12 mb-0">{{ subs.no }} </p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ subs.municipality_name }}, {{ subs.barangay_name }}, {{ subs.purok }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ subs.region_name }}, {{ subs.province_name }} </p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ subs.plan_name }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ subs.sub_type}}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ subs.modem_name }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ subs.modem_serial}}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ subs.pon_no }}/{{ subs.nap_no }}</h6>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ subs.sub_status }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ formattedDateTime(subs.date_activated)}}/
                                                                <span v-if="subs.sub_status=='terminated'"> 
                                                                   ({{ formattedDateTime(subs.date_terminated) }})
                                                                </span>
                                                            </p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td class="text-center">
                                                    {{ subs.referred_by }}
                                                    <div class="prod-action-links">
                                                        <ul class="list-inline me-auto mb-0">
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Subscriptions">
                                                                <a href="#" @click="showAddModal(subs.id)" class="avtar avtar-xs btn-link-secondary btn-pc-default">
                                                                    <i class="ti ti-eye f-18"></i>
                                                                </a>
                                                            </li>
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Edit">
                                                                <!-- 
                                                                <router-link to="/add-product" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                                    <i class="ti ti-edit-circle f-18"></i>
                                                                </router-link> 
                                                                -->
                                                                <a href="#" @click="getSubscription(subs.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                                    <i class="ti ti-edit-circle f-18"></i>
                                                                </a>
                                                            </li>
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                                <a href="#" @click="cancelDeleteSubs(subs.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
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
                            </div>

                            <!-- Billing list -->
                            <div class="tab-pane fade show active" id="analytics-tab-2-pane" role="tabpanel" aria-labelledby="analytics-tab-2" tabindex="0"> 
                                <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2">
                                    <div class="input-group search-bar">
                                        <div class="col-sm-12">
                                            <h5>{{ subscriber.last_name }}, {{ subscriber.first_name }} 
                                                {{ subscriber.middle_name }} {{ subscriber.ext_name }}</h5>
                                        </div>
                                        <p text-muted f-12 mb-0>{{ subscription.no }} - {{ subscription.alias }} </p>
                                    </div>
                                    
                                    <!-- Add Billing Button -->
                                    <BButton variant="primary" class="btn btn-sm" @click="showAddModalBillOpen">Add Billing</BButton>
                                </div>
                                <div class="table-responsive fixed-height">
                                    <!-- Show Spinner While Loading -->
                                    <div v-if="loading2" class="text-center p-4">
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
                                                @click="selectRowBills(bill.id)"
                                                @dblclick="goToNextTabPay(bill.id)">
                                                <td class="text-end">{{index + 1}}</td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ bill.billing_no }}</h6>
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
                                                            <!--
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Subscriptions">
                                                                <a href="#" @click="showAddModal(bill.id)" class="avtar avtar-xs btn-link-secondary btn-pc-default">
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
                                                                <a href="#" @click="getBill(bill.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                                    <i class="ti ti-edit-circle f-18"></i>
                                                                </a>
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
                            </div>

                            <!-- Payment list -->
                            <div class="tab-pane fade" id="analytics-tab-3-pane" role="tabpanel" aria-labelledby="analytics-tab-3" tabindex="0">
                                <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2">
                                    <div class="input-group search-bar">
                                        <div class="col-sm-12">
                                            <h5>{{ subscriber.last_name }}, {{ subscriber.first_name }} 
                                                {{ subscriber.middle_name }} {{ subscriber.ext_name }}</h5>
                                        </div>
                                        <p text-muted f-12 mb-0>{{ subscription.no }} - {{ subscription.alias }} | {{ bill.billing_no }}</p>
                                    </div>
                                    
                                    <!-- Add Paymment Button -->
                                    <BButton variant="primary" class="btn btn-sm" @click="showAddModalPaymentOpen">Add Payment</BButton>
                                </div>
                                <div class="table-responsive fixed-height">
                                    <!-- Show Spinner While Loading -->
                                    <div v-if="loading3" class="text-center p-4">
                                        <BSpinner label="Loading..."></BSpinner>
                                    </div>
                                    <table v-else class="table table-hover table-sm tbl-product" id="pc-dt-simple-1">
                                        <thead>
                                            <tr>
                                                <th class="text-end">#</th>
                                                <th>No #</th>
                                                <th>Date/Payment</th>
                                                <th>Type</th>
                                                <th class="text-end">Amount</th>
                                                <th>Received by</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(pay, index) in payments" :key="pay.id">
                                                <td class="text-end">{{index + 1}}</td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ pay.or_no }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ pay.or_ref_no }}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ formattedDateTime(pay.payment_date) }}</h6>
                                                            <p class="text-muted f-12 mb-0">
                                                                <span v-if="pay.is_paid" class="badge rounded-pill bg-success text-dark">paid</span>
                                                                <span v-if="pay.is_partial" class="badge rounded-pill bg-warning text-dark"> partial</span>
                                                                <span v-if="pay.is_cancelled" class="badge rounded-pill bg-danger text-dark"> cancelled</span>
                                                            </p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td class="d-flex">
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ pay.payment_type }}</h6>
                                                            <p class="text-muted f-12 mb-0">
                                                                <span v-if="pay.cheque_no.length"> {{ pay.cheque_no}} </span> 
                                                                <span v-if="pay.reference_no.length"> | {{ pay.reference_no }}</span>
                                                            </p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td class="text-end">
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ pay.amount_paid }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ pay.remarks }}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td class="text-center">
                                                    <h6 class="mb-1">{{ pay.first_name }} {{ pay.last_name }}</h6>
                                                    <p class="text-muted f-12 mb-0">
                                                        {{ formattedDateTime(pay.updated_on)}}
                                                    </p>
                                                    <div class="prod-action-links">
                                                        <ul class="list-inline me-auto mb-0">
                                                            <!--
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Subscriptions">
                                                                <a href="#" @click="showAddModal(bill.id)" class="avtar avtar-xs btn-link-secondary btn-pc-default">
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
                                                                <a href="#" @click="getPayment(pay.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                                    <i class="ti ti-edit-circle f-18"></i>
                                                                </a>
                                                            </li>
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                                <a href="#" @click="cancelDeletePayment(pay.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
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
                            </div>

                            <!-- ticket list -->
                            <div class="tab-pane fade" id="analytics-tab-4-pane" role="tabpanel" aria-labelledby="analytics-tab-4" tabindex="0">
                                <div class="d-flex justify-content-between align-items-center p-sm-4 pb-sm-2">
                                    <div class="input-group search-bar">
                                        <div class="col-sm-12">
                                            <h5>{{ subscriber.last_name }}, {{ subscriber.first_name }} 
                                                {{ subscriber.middle_name }} {{ subscriber.ext_name }}</h5>
                                        </div>
                                        <p text-muted f-12 mb-0>{{ subscription.no }}</p>
                                    </div>
                                    
                                    <!-- Add Ticket Button -->
                                    <BButton variant="primary" class="btn btn-sm" @click="showAddModalTicketOpen">Add Ticket</BButton>
                                </div>
                                <div class="table-responsive fixed-height">
                                    <!-- Show Spinner While Loading -->
                                    <div v-if="loading4" class="text-center p-4">
                                        <BSpinner label="Loading..."></BSpinner>
                                    </div>
                                    <table v-else class="table table-hover table-sm tbl-product" id="pc-dt-simple-1">
                                        <thead>
                                            <tr>
                                                <th class="text-end">#</th>
                                                <th>No #</th>
                                                <th>Subject</th>
                                                <th>Priority/To</th>
                                                <th>StatusRemarks</th>
                                                <th>Prepared by</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(ticket, index) in tickets" :key="ticket.id">
                                                <td class="text-end">{{index + 1}}</td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ ticket.ticket_no }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ formattedDateTime(ticket.ticket_date) }}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ ticket.subject }}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ticket.description}}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td>
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">{{ticket.priority}}</h6>
                                                            <p class="text-muted f-12 mb-0">{{ticket.first_name_to}} {{ ticket.last_name_to }}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td class="d-flex">
                                                    <BRow class="d-flex">
                                                        <BCol>
                                                            <h6 class="mb-1">
                                                                <span v-if="ticket.status=='resolved'" class="badge bg-success text-dark">Resolved</span>
                                                                <span v-if="ticket.status=='inprogress'" class="badge bg-info text-dark">In progress</span>
                                                                <span v-if="ticket.status=='pending'" class="badge bg-warning text-dark">Pending</span>
                                                            </h6>
                                                            <p class="text-muted f-12 mb-0">{{ ticket.remarks }}</p>
                                                        </BCol>
                                                    </BRow>
                                                </td>
                                                <td class="text-center">
                                                    <h6 class="mb-1">{{ ticket.first_name }} {{ ticket.last_name }}</h6>
                                                    <p class="text-muted f-12 mb-0">
                                                        {{ formattedDateTime(ticket.updated_on)}}
                                                    </p>
                                                    <div class="prod-action-links">
                                                        <ul class="list-inline me-auto mb-0">
                                                            <!--
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Subscriptions">
                                                                <a href="#" @click="showAddModal(bill.id)" class="avtar avtar-xs btn-link-secondary btn-pc-default">
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
                                                                <a href="#" @click="getTicket(ticket.id)" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                                    <i class="ti ti-edit-circle f-18"></i>
                                                                </a>
                                                            </li>
                                                            <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                                <a href="#" @click="cancelDeleteTicket(ticket.id)" class="avtar avtar-xs btn-link-danger btn-pc-default">
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
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </Layout>
</template>
<style lang="css">
    .fixed-height {
        max-height: 350px; /* Set the desired fixed height for the table container */
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