<script>
    import Layout from "@/layout/main.vue"
    import pageHeader from "@/components/page-header.vue";
    import Swal from "sweetalert2";
    import axios from "axios";

    export default {
        name: "ISSUES",
        components: {
            Layout, pageHeader
        },
        data() {
            return {
                regions: [],
                newRegion:"",
                provinces: [],
                municipalities: [],
                barangays: [],
                selectedRegion: null,
                selectedProvince: null,
                selectedMunicipality: null,
                newProvince: "",
                newMunicipality: "",
                newBarangay: "",
                editedRegion: null,
                editedProvince: null,
                editedMunicipality: null,
                editedBarangay: null,

                operation: false,
                editedIssue: {
                    id: "",
                    name: "",
                    description: ""
                },
                issues: [],
                issue: {
                    id: "",
                    name: "",
                    description: "",
                }

            };
        },
        created() {
            this.getIssues();
        },
        methods: {
            async updateIssue(){
                try {
                    if (this.operation==false) {
                        await axios.post("/api/v1/issues/", {
                            name: this.issue.name,
                            description: this.issue.description
                        });  
                    } else {
                        await axios.post("/api/v1/issues/", {
                            name: this.issue.name,
                            description: this.issue.description
                        });  
                    }
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: "Your work has been saved",
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    this.getIssues();
                    this.operation = false;
                } catch (error) {
                    console.error('Error updating issues:', error);
                }
            },
            async getIssues() {
                try {
                    await axios.get("/api/v1/issues/").then((response) =>  {this.issues = response.data});
                } catch (error) {
                    console.error('Error fetching issues:', error);
                }
            },
            async getIssue() {
                try {
                    await axios.get(`/api/v1/issues/${this.issue.id}/`).then((response) => {
                        this.issue = response.data
                    });
                } catch (error) {
                    console.error('Error fetching issues:', error);
                }
            },
            async deleteIssue() {
                try {
                    await axios.delete(`/api/v1/issues/${this.issue.id}/`).then(() => {
                        this.issues = this.issues.filter((issue) => issue.id !== this.issue.id);
                    });
                } catch (error) {
                    console.error('Error fetching issues:', error);
                }
            },
            editIssue(issue) {
                this.editedIssue.id=issue.id;
                this.editedIssue.name = issue.name;
                this.editedIssue.description=issue.description;
                this.operation = true;
            },
        },
    }
</script>

<template>
    <Layout>
        <pageHeader title="Issues" PageTitle="Issues" />
        <BRow>
            <BCol no-body class="table-card">
                 <!-- Regions Section -->
                <BRow class="">
                    <BCol class="col-lg-12">
                        <BRow>
                            <BCol md="12">
                                <BCard no-body>
                                    <BCardHeader>
                                        <h5 class="mb-2">Issues</h5><BRow class=" mb-3"></BRow>
                                        <small class="m-0">The most basic list group is an unordered list with list items and the proper
                                            classes</small>
                                    </BCardHeader>
                                    <BCardBody>
                                        <div class="mt-3">
                                            <form @submit.prevent="updateIssue">
                                                <BRow class=" mb-2">
                                                    <label for="issue" class="col-sm-1 ms-3 col-form-label">Issue</label>
                                                    <BCol class="col-sm-3">
                                                        <input v-model="issue.name" placeholder="Enter issue" class="form-control" id="issue" required /> 
                                                    </BCol>
                                                    <label for="desciption" class="col-sm-1 col-form-label">Description</label>
                                                    <BCol class="col-sm-5">
                                                        <input v-model="issue.description" placeholder="Description" class="form-control" id="description" required /> 
                                                    </BCol>
                                                    <button type="submit" class="col-sm-1 btn btn-primary">Add</button>
                                                </BRow>
                                            </form>
                                        </div>
                                        <hr />
                                        <BListGroup v-for="issue in issues" :key="issue.id" class="d-flex">
                                            <BListGroupItem>
                                                <div v-if="editedIssue?.id===issue.id" class="d-flex w-100">
                                                    <input
                                                        v-model="editedIssue.name"
                                                        class="form-control me-2"
                                                        placeholder="Edit issue name"
                                                    />
                                                    <input
                                                        v-model="editedIssue.description"
                                                        class="form-control me-2"
                                                        placeholder="Edit issue description"
                                                    />
                                                    <button
                                                        class="btn btn-sm btn-success me-2"
                                                        @click="updateIssue(issue.id)"
                                                    >
                                                        Save
                                                    </button>
                                                    <button class="btn btn-sm btn-secondary" @click="this.editedIssue=null">
                                                        Cancel
                                                    </button>
                                                </div>
                                                <div v-else class="mx-3">
                                                    <span>{{ issue.name }}</span><span>{{ issue.description }}</span> 
                                                    <span class="float-end"><a href="#" @click="deleteIssue(issue.id)" >Delete</a></span>
                                                    <span class="float-end me-2"><a href="#" @click="editIssue(issue)" >Edit</a></span>
                                                </div>
                                            </BListGroupItem>
                                        </BListGroup>
                                    </BCardBody>
                                </BCard>
                            </BCol>
                        </BRow>
                    </BCol>
                </BRow>

            </BCol>
        </BRow>
    </Layout>
</template>