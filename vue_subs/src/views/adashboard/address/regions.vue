<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"

export default {
    name: "REGIONS",
    components: {
        Layout, pageheader
    },
}
</script>

<template>
    <Layout>
        <pageheader title="Region list" pageTitle="Regions" />
        <BRow>
            <BCol class="col-sm-12">
                <BCard no-body class="table-card">
                    <BCardBody>
                        <div class="text-end p-sm-4 pb-sm-2">
                            <router-link to="/add-product" class="btn btn-primary"> <i class="ti ti-plus f-18"></i> Add Region </router-link>
                        </div>
                        <div class="table-responsive">
                            <table class="table table-hover tbl-product" id="pc-dt-simple">
                                <thead>
                                    <tr>
                                        <th class="text-end">#</th>
                                        <th>Plan Detail</th>
                                        <th>Bandwidth (up/down)</th>
                                        <th class="text-end">Price</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td class="text-end">7</td>
                                        <td>
                                            <BRow class="d-flex">
                                                <BCol class="col-auto pe-5">
                                                    <img src="@/assets/images/application/img-prod-1.jpg" alt="user-image" class="wid-40 rounded">
                                                </BCol>
                                                <BCol>
                                                    <h6 class="mb-1">Apple Series 4 GPS A38 MM Space</h6>
                                                    <p class="text-muted f-12 mb-0">Apple Watch SE Smartwatch </p>
                                                </BCol>
                                            </BRow>
                                        </td>
                                        <td>Electronics, Laptop</td>
                                        <td class="text-end">$14.59</td>
                                        <td class="text-center">
                                            <img src="@/assets/images/application/img-prod-brand-1.png" alt="user-image" class="wid-40">
                                            <div class="prod-action-links">
                                                <ul class="list-inline me-auto mb-0">
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="View">
                                                        <a href="#" class="avtar avtar-xs btn-link-secondary btn-pc-default" data-bs-toggle="offcanvas" data-bs-target="#productOffcanvas">
                                                            <i class="ti ti-eye f-18"></i>
                                                        </a>
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Edit">
                                                        <router-link to="/add-product" class=" avtar avtar-xs btn-link-success btn-pc-default">
                                                            <i class="ti ti-edit-circle f-18"></i>
                                                        </router-link>
                                                    </li>
                                                    <li class="list-inline-item align-bottom" data-bs-toggle="tooltip" title="Delete">
                                                        <a href="#" class="avtar avtar-xs btn-link-danger btn-pc-default">
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
    </Layout>
</template>