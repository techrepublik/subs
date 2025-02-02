<script>
    import Layout from "@/layout/main.vue"
    import pageHeader from "@/components/page-header.vue";
    import axios from "axios";

    export default {
        name: "ADDRESS",
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
            };
        },
        created() {
            this.fetchRegions();
        },
        methods: {
            addRegion() {
                axios.post("http://localhost:8000/api/v1/regions/", { name: this.newRegion }).then((response) => {
                    this.regions.push(response.data);
                    this.newRegion = "";
                });
            },
            addProvince() {
                axios.post("http://localhost:8000/api/v1/provinces/", {
                    name: this.newProvince,
                    region: this.selectedRegion.id
                }).then((response) => {
                    this.provinces.push(response.data);
                    console.log(response.data)
                    this.newProvince = "";
                });
            },
            addMunicipality() {
                axios.post("http://localhost:8000/api/v1/municipalities/", {
                    name: this.newMunicipality,
                    province: this.selectedProvince.id
                }).then((response) => {
                        this.municipalities.push(response.data);
                        this.newMunicipality = "";
                });
            },
            addBarangay() {
                axios.post(`http://localhost:8000/api/v1/barangays/`, {
                    name: this.newBarangay,
                    municipality: this.selectedMunicipality.id
                }).then((response) => {
                    this.barangays.push(response.data);
                    this.newBarangay = "";
                });
            },
            fetchRegions() {
                axios.get("http://localhost:8000/api/v1/regions/").then((response) => {
                    this.regions = response.data;
                });
            },
            fetchProvinces(regionId) {
                axios.get(`http://localhost:8000/api/v1/provinces/?region_id=${regionId}`).then((response) => {
                    this.provinces = response.data;
                    console.log(this.provinces)
                });
            },
            fetchMunicipalities(provinceId) {
                axios.get(`http://localhost:8000/api/v1/municipalities/?province_id=${provinceId}`).then((response) => {
                    this.municipalities = response.data;
                });
            },
            fetchBarangays(municipalityId) {
                axios.get(`http://localhost:8000/api/v1/barangays/?municipality_id=${municipalityId}`).then((response) => {
                    this.barangays = response.data;
                });
            },
            selectRegion(region) {
                this.selectedRegion = region;
                this.fetchProvinces(region.id);
            },
            deselectRegion() {
                this.selectedRegion = null;
                this.provinces = [];
            },
            selectProvince(province) {
                this.selectedProvince = province;
                this.fetchMunicipalities(province.id);
            },
            deselectProvince() {
                this.selectedProvince = null;
                this.municipalities = [];
            },
            selectMunicipality(municipality) {
                this.selectedMunicipality = municipality;
                this.fetchBarangays(municipality.id);
            },
            deselectMunicipality() {
                this.selectedMunicipality = null;
                this.barangays = [];
            },
            editRecord( records, flagg) {
                if (flagg==0){
                    this.editedRegion = { ...records }; // Clone the region for editing
                } else if (flagg==1){
                    this.editedProvince = {...records};
                } else if (flagg==2) {
                    this.editedMunicipality = { ...records };
                } else {
                    this.editedBarangay = { ...records };
                }
            },
            updateRecord(recordId, flagg) {
                if (flagg == 0) {
                    axios.put(`http://localhost:8000/api/v1/regions/${recordId}/`, { 
                        name: this.editedRegion.name 
                    }).then(() => {
                        const index = this.regions.findIndex((r) => r.id === recordId);
                        if (index !== -1) {
                            this.regions[index].name = this.editedRegion.name; // Update the name
                        }
                        this.editedRegion = null; // Reset the edit state
                    });
                } else if (flagg==1) {
                    axios.patch(`http://localhost:8000/api/v1/provinces/${recordId}/`, { 
                        name: this.editedProvince.name 
                    }).then(() => {
                        const index = this.provinces.findIndex((r) => r.id === recordId);
                        if (index !== -1) {
                            this.provinces[index].name = this.editedProvince.name; // Update the name
                        }
                        this.editedProvince = null; // Reset the edit state
                    });
                } else if (flagg==2){
                    axios.patch(`http://localhost:8000/api/v1/municipalities/${recordId}/`, { 
                        name: this.editedMunicipality.name 
                    }).then(() => {
                        const index = this.municipalities.findIndex((r) => r.id === recordId);
                        if (index !== -1) {
                            this.municipalities[index].name = this.editedMunicipality.name; // Update the name
                        }
                        this.editedMunicipality = null; // Reset the edit state
                    });
                } else if (flagg==3) {
                    axios.patch(`http://localhost:8000/api/v1/barangays/${recordId}/`, { 
                        name: this.editedBarangay.name 
                    }).then(() => {
                        const index = this.barangays.findIndex((r) => r.id === recordId);
                        if (index !== -1) {
                            this.barangays[index].name = this.editedBarangay.name; // Update the name
                        }
                        this.editedBarangay= null; // Reset the edit state
                    });
                }
            },
            cancelEdit(flagg) {
                if (flagg == 0){
                    this.editedRegion = null; // Reset the edit state
                } else if (flagg == 1) {
                    this.editedProvince = null
                } else if (flagg == 2) {
                    this.editedMunicipality = null
                } else if (flagg == 3) {
                    this.editedBarangay = null
                }
            },
            deleteRegion(regionId) {
                    axios.delete(`http://localhost:8000/api/v1/regions/${regionId}/`).then(() => {
                        this.regions = this.regions.filter((region) => region.id !== regionId);
                });
            },
            deleteProvince(provinceId) {
                axios.delete(`http://localhost:8000/api/v1/provinces/${provinceId}/`).then(() => {
                    this.provinces = this.provinces.filter(
                    (province) => province.id !== provinceId
                    );
                });
            },
            deleteMunicipality(municipalityId) {
                axios.delete(`http://localhost:8000/api/v1/municipalities/${municipalityId}/`).then(() => {
                    this.municipalities = this.municipalities.filter(
                    (municipality) => municipality.id !== municipalityId
                    );
                });
            },
            deleteBarangay(barangayId) {
                axios.delete(`http://localhost:8000/api/v1/barangays/${barangayId}/`).then(() => {
                    this.barangays = this.barangays.filter(
                    (barangay) => barangay.id !== barangayId
                    );
                });
            },
        },
    }
</script>

<template>
    <Layout>
        <pageHeader title="Address List" PageTitle="Address" />
        <BRow>
            <BCol no-body class="table-card">
                 <!-- Regions Section -->
                <BRow class="">
                    <BCol class="col-lg-10">
                        
                            <h2>Regions</h2>
                            <form @submit.prevent="addRegion">
                                <BRow class="mb-6">
                                    <label for="region" class="col-sm-2 col-form-label">Region name</label>
                                    <BCol class="col-sm-4">
                                        <input v-model="newRegion" placeholder="Enter a region." class="form-control" id="region" required /> 
                                    </BCol>
                                    <button type="submit" class="col-sm-1 btn btn-primary">Add</button>
                                </BRow>            
                            </form>
                        
                            <BRow>
                                <BCol md="6">
                                    <BCard no-body>
                                        <BCardHeader>
                                            <h5 class="mb-2">Regions</h5><BRow class=" mb-3"></BRow>
                                            <small class="m-0">List of regions.</small>
                                        </BCardHeader>
                                        <BCardBody>
                                            <BListGroup v-for="region in regions" :key="region.id" class="d-flex mt-2">
                                                <BListGroupItem>
                                                    <div v-if="editedRegion?.id === region.id" class="d-flex w-100">
                                                        <input
                                                            v-model="editedRegion.name"
                                                            class="form-control me-2"
                                                            placeholder="Edit Region Name"
                                                        />
                                                        <button
                                                            class="btn btn-sm btn-success me-2"
                                                            @click="updateRecord(region.id, 0)"
                                                        >
                                                            Save
                                                        </button>
                                                        <button class="btn btn-sm btn-secondary" @click="cancelEdit(0)">
                                                            Cancel
                                                        </button>
                                                    </div>
                                                    <div v-else>
                                                        <span class="me-4"> {{ region.name }} </span>
                                                        <span class="float-end ms-2"><a href="#" @click="deleteRegion(region.id)" >Delete</a></span>
                                                        <span class="float-end me-2"><a href="#" @click="editRecord(region, 0)" >Edit</a></span>
                                                        <span class="float-end me-2"><a href="#"  @click="selectRegion(region)">Provinces</a></span>
                                                    </div>
                                                </BListGroupItem>
                                            </BListGroup>
                                        </BCardBody>
                                    </BCard>
                                </BCol>
                            </BRow>

                            <!-- Provinces Section -->
                            <BRow v-if="selectedRegion" class="mt-4">
                                <hr />
                                <form @submit.prevent="addProvince">
                                    <BRow class=" mb-6">
                                        <label for="province" class="col-sm-2 col-form-label">Province name</label>
                                        <BCol class="col-sm-4">
                                            <input v-model="newProvince" placeholder="Enter a province." class="form-control" id="province" required /> 
                                        </BCol>
                                        <button type="submit" class="col-sm-1 btn btn-primary">Add</button>
                                    </BRow>            
                                </form>
                                <BCol md="6">
                                    <BCard no-body>
                                        <BCardHeader>
                                            <h5 class="mb-2">Provinces in {{ selectedRegion.name }}</h5><BRow class=" mb-3"></BRow>
                                            <small class="m-0">List of provinces</small>
                                        </BCardHeader>
                                        <BCardBody>
                                            <BListGroup v-for="prov in provinces" :key="prov.id" class="d-flex mt-2">
                                                <BListGroupItem>
                                                    <div v-if="editedProvince?.id===prov.id" class="d-flex w-100">
                                                        <input
                                                            v-model="editedProvince.name"
                                                            class="form-control me-2"
                                                            placeholder="Edit Province Name"
                                                        />
                                                        <button
                                                            class="btn btn-sm btn-success me-2"
                                                            @click="updateRecord(prov.id,1)"
                                                        >
                                                            Save
                                                        </button>
                                                        <button class="btn btn-sm btn-secondary" @click="cancelEdit(1)">
                                                            Cancel
                                                        </button>
                                                    </div>
                                                    <div v-else>
                                                        <span class="me-4"> {{ prov.name }}</span>
                                                        <span class="float-end"><a href="#" @click="deleteProvince(prov.id)" >Delete</a></span>
                                                        <span class="float-end me-2"><a href="#" @click="editRecord(prov, 1)" >Edit</a></span>
                                                        <span class="float-end me-2"><a href="#" @click="selectProvince(prov)">Municipalities</a></span>
                                                    </div>
                                                </BListGroupItem>
                                            </BListGroup>
                                        </BCardBody>
                                        <button @click="deselectRegion" class="col-sm-4 btn btn-primary float-end m-2">Back to Regions</button>
                                    </BCard>
                                </BCol>
                            </BRow>

                            <!-- Municipalities Section -->
                            <BRow v-if="selectedProvince" class="mt-4">
                                <hr />
                                <form @submit.prevent="addMunicipality">
                                    <BRow class=" mb-6">
                                        <label for="municipality" class="col-sm-2 col-form-label">Municipality name</label>
                                        <BCol class="col-sm-4">
                                            <input v-model="newMunicipality" placeholder="Enter a municipality." class="form-control" id="municipality" required /> 
                                        </BCol>
                                        <button type="submit" class="col-sm-1 btn btn-primary">Add</button>
                                    </BRow>            
                                </form>
                                <BCol md="6" id="municipality">
                                    <BCard no-body>
                                        <BCardHeader>
                                            <h5 class="mb-2">Municipality in {{ selectedProvince.name }}</h5><BRow class=" mb-3"></BRow>
                                            <small class="m-0">List of municipalities</small>
                                        </BCardHeader>
                                        <BCardBody>
                                            <BListGroup v-for="muni in municipalities" :key="muni.id" class="d-flex mt-2">
                                                <BListGroupItem>
                                                    <div v-if="editedMunicipality?.id===muni.id" class="d-flex w-100">
                                                        <input
                                                            v-model="editedMunicipality.name"
                                                            class="form-control me-2"
                                                            placeholder="Edit Municipality Name"
                                                        />
                                                        <button
                                                            class="btn btn-sm btn-success me-2"
                                                            @click="updateRecord(muni.id,2)"
                                                        >
                                                            Save
                                                        </button>
                                                        <button class="btn btn-sm btn-secondary" @click="cancelEdit(2)">
                                                            Cancel
                                                        </button>
                                                    </div>
                                                    <div v-else>
                                                        <span class="me-4">{{ muni.name }}</span> 
                                                        <span class="float-end"><a href="#" @click="deleteMunicipality(muni.id)" >Delete</a></span>
                                                        <span class="float-end me-2"><a href="#" @click="editRecord(muni, 2)" >Edit</a></span>
                                                        <span class="float-end me-2"><a href="#"  @click="selectMunicipality(muni)">Barangays</a></span>
                                                    </div>
                                                </BListGroupItem>
                                            </BListGroup>
                                        </BCardBody>
                                        <button @click="deselectProvince" class="col-sm-4 btn btn-primary float-end m-2">Back to Province</button>
                                    </BCard>
                                </BCol>
                            </BRow>

                            <!-- Barangays Section -->
                            <BRow v-if="selectedMunicipality" class="mt-4">
                                <hr />
                                <form @submit.prevent="addBarangay">
                                    <BRow class=" mb-6">
                                        <label for="barangay" class="col-sm-2 col-form-label">Barangay name</label>
                                        <BCol class="col-sm-4">
                                            <input v-model="newBarangay" placeholder="Enter a barangay." class="form-control" id="barangay" required /> 
                                        </BCol>
                                        <button type="submit" class="col-sm-1 btn btn-primary">Add</button>
                                    </BRow>            
                                </form>
                                <BCol md="6" id="barangay">
                                    <BCard no-body>
                                        <BCardHeader>
                                            <h5 class="mb-2">Barangays in {{ selectedMunicipality.name }}</h5><BRow class=" mb-3"></BRow>
                                            <small class="m-0">List of barangays</small>
                                        </BCardHeader>
                                        <BCardBody>
                                            <BListGroup v-for="bara in barangays" :key="bara.id" class="d-flex mt-2">
                                                <BListGroupItem>
                                                    <div v-if="editedBarangay?.id===bara.id" class="d-flex w-100">
                                                        <input
                                                            v-model="editedBarangay.name"
                                                            class="form-control me-2"
                                                            placeholder="Edit Barangay Name"
                                                        />
                                                        <button
                                                            class="btn btn-sm btn-success me-2"
                                                            @click="updateRecord(bara.id,3)"
                                                        >
                                                            Save
                                                        </button>
                                                        <button class="btn btn-sm btn-secondary" @click="cancelEdit(3)">
                                                            Cancel
                                                        </button>
                                                    </div>
                                                    <div v-else>
                                                        <span class="me-4">{{ bara.name }}</span> 
                                                        <span class="float-end"><a href="#" @click="deleteBarangay(bara.id)" >Delete</a></span>
                                                        <span class="float-end me-2"><a href="#" @click="editRecord(bara, 3)" >Edit</a></span>
                                                    </div>
                                                </BListGroupItem>
                                            </BListGroup>
                                        </BCardBody>
                                        <button @click="deselectMunicipality" class="col-sm-4 btn btn-primary float-end m-2">Back to Municipality</button>
                                    </BCard>
                                </BCol>
                            </BRow>
                    </BCol>
                </BRow>

            </BCol>
        </BRow>
    </Layout>
</template>