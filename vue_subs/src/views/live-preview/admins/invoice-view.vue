<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"

export default {
    name: "Ticket list",
    components: {
        Layout, pageheader
    },
    mounted() {
        document.querySelector('.btn-print-invoice').addEventListener('click', this.printInvoice);
    },
    beforeUnmount() {
        document.querySelector('.btn-print-invoice').removeEventListener('click', this.printInvoice);
    },
    methods: {
        printInvoice() {
            var link2 = document.createElement('link');
            link2.innerHTML =
                '<style>@media print{*,::after,::before{text-shadow:none!important;box-shadow:none!important}a:not(.btn){text-decoration:none}abbr[title]::after{content:" ("attr(title) ")"}pre{white-space:pre-wrap!important}blockquote,pre{border:1px solid #adb5bd;page-break-inside:avoid}thead{display:table-header-group}img,tr{page-break-inside:avoid}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}@page{size:a3}body{min-width:992px!important}.container{min-width:992px!important}.page-header,.pc-sidebar,.pc-mob-header,.pc-header,.pct-customizer,.modal,.navbar{display:none}.pc-container{top:0;}.invoice-contact{padding-top:0;}@page,.card-body,.card-header,body,.pcoded-content{padding:0;margin:0}.badge{border:1px solid #000}.table{border-collapse:collapse!important}.table td,.table th{background-color:#fff!important}.table-bordered td,.table-bordered th{border:1px solid #dee2e6!important}.table-dark{color:inherit}.table-dark tbody+tbody,.table-dark td,.table-dark th,.table-dark thead th{border-color:#dee2e6}.table .thead-dark th{color:inherit;border-color:#dee2e6}}</style>';
            document.getElementsByTagName('head')[0].appendChild(link2);
            window.print();
        }
    }
}
</script>

<template>
    <Layout>
        <pageheader title="Ticket list" pageTitle="Helpdesk" />
        <!-- [ Main Content ] start -->
        <div class="row">
            <div class="col-sm-12">
                <div class="d-print-none card mb-3">
                    <div class="card-body p-3">
                        <ul class="list-inline ms-auto mb-0 d-flex justify-content-end flex-wrap">
                            <li class="list-inline-item align-bottom me-2">
                                <a href="#" class="avtar avtar-s btn-link-secondary">
                                    <i class="ph-duotone ph-pencil-simple-line f-22"></i>
                                </a>
                            </li>
                            <li class="list-inline-item align-bottom me-2">
                                <a href="#" class="avtar avtar-s btn-link-secondary">
                                    <i class="ph-duotone ph-eye f-22"></i>
                                </a>
                            </li>
                            <li class="list-inline-item align-bottom me-2">
                                <a href="#" class="avtar avtar-s btn-link-secondary">
                                    <i class="ph-duotone ph-download-simple f-22"></i>
                                </a>
                            </li>
                            <li class="list-inline-item align-bottom me-2">
                                <a href="#" class="avtar avtar-s btn-link-secondary">
                                    <i class="ph-duotone ph-printer f-22"></i>
                                </a>
                            </li>
                            <li class="list-inline-item align-bottom me-2">
                                <a href="#" class="avtar avtar-s btn-link-secondary">
                                    <i class="ph-duotone ph-paper-plane-tilt f-22"></i>
                                </a>
                            </li>
                            <li class="list-inline-item align-bottom me-2">
                                <a href="#" class="avtar avtar-s btn-link-secondary">
                                    <i class="ph-duotone ph-share-network f-22"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <div class="row g-3">
                            <div class="col-12">
                                <div class="row align-items-center g-3">
                                    <div class="col-sm-6">
                                        <div class="d-flex align-items-center mb-2">
                                            <img src="@/assets/images/logo-dark.svg" class="img-fluid" alt="images">
                                            <span class="badge bg-light-secondary rounded-pill ms-2">Paid</span>
                                        </div>
                                        <p class="mb-0">INV - 000457</p>
                                    </div>
                                    <div class="col-sm-6 text-sm-end">
                                        <h6>Date <span class="text-muted f-w-400">03/8/2023</span></h6>
                                        <h6>Due Date <span class="text-muted f-w-400">10/8/2023</span></h6>
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="border rounded p-3">
                                    <h6 class="mb-0">From:</h6>
                                    <h5>Garcia-Cameron and Sons</h5>
                                    <p class="mb-0">8534 Saunders Hill Apt. 583</p>
                                    <p class="mb-0">(970) 982-3353</p>
                                    <p class="mb-0">brandon07@pierce.com</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="border rounded p-3">
                                    <h6 class="mb-0">To:</h6>
                                    <h5>Dickinson-Cummerata</h5>
                                    <p class="mb-0">55D Leatha Way Ernaburgh, NT 2146</p>
                                    <p class="mb-0">75-9079921</p>
                                    <p class="mb-0">kasandra.conn@borer.com</p>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="table-responsive">
                                    <table class="table table-hover mb-0">
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th>Name</th>
                                                <th>Description</th>
                                                <th class="text-end">Qty</th>
                                                <th class="text-end">Price</th>
                                                <th class="text-end">Total Amount</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>1</td>
                                                <td>Mauris</td>
                                                <td>Malesuada adipiscing</td>
                                                <td class="text-end">2</td>
                                                <td class="text-end">$80.00</td>
                                                <td class="text-end">$160.00</td>
                                            </tr>
                                            <tr>
                                                <td>2</td>
                                                <td>Vitae</td>
                                                <td>Hac egestas</td>
                                                <td class="text-end">3</td>
                                                <td class="text-end">$40.00</td>
                                                <td class="text-end">$120.00</td>
                                            </tr>
                                            <tr>
                                                <td>3</td>
                                                <td>Mauris</td>
                                                <td>Malesuada adipiscing</td>
                                                <td class="text-end">4</td>
                                                <td class="text-end">$80.00</td>
                                                <td class="text-end">$320.00</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="text-start">
                                    <hr class="mb-2 mt-1 border-secondary border-opacity-50">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="invoice-total ms-auto">
                                    <div class="row">
                                        <div class="col-6">
                                            <p class="text-muted mb-1 text-start">Sub Total :</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="mb-1 text-end">$20.00</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="text-muted mb-1 text-start">Discount :</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="mb-1 text-end text-success">$10.00</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="text-muted mb-1 text-start">Taxes :</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="mb-1 text-end">$5.000</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="f-w-600 mb-1 text-start">Grand Total :</p>
                                        </div>
                                        <div class="col-6">
                                            <p class="f-w-600 mb-1 text-end">$25.00</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <label class="form-label">Note</label>
                                <p class="mb-0">It was a pleasure working with you and your team. We hope you will keep us in mind for future freelance
                                    projects. Thank You!</p>
                            </div>
                            <div class="col-12 text-end d-print-none">
                                <button class="btn btn-outline-secondary btn-print-invoice">Download</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
</template>