<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"

export default {
    name: "SAMPLE-PAGE",
    components: {
        Layout, pageheader
    },
    data() {
        return {
            modalShow: false,
        }
    }
}
</script>

<template>
    <Layout>
        <pageheader title="Sample Page" pageTitle="Other" />

        <BRow>
            <BCol sm="12">
                <BCard no-body>
                    <BCardHeader>
                        <h5>Hello card</h5>
                    </BCardHeader>
                    <BCardBody>
                        <BRow>
                            <div>
                            <BButton variant="primary" @click="modalShow = !modalShow">Launch demo modal</BButton>
                            <BModal v-model="modalShow" title="Modal Title" class="v-modal-custom" size="lg">
                                <div class="modal-body  p-0">
                                    <p>Woohoo, you're reading this text in a modal!</p>
                                    <form>
                                        <div class="form-group">
                                            <label class="form-label" for="exampleInputEmail1">Email address</label>
                                            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                                            <small id="emailHelp" class="form-text text-muted">We'll never share your email with
                                                anyone
                                                else.</small>
                                        </div>
                                        <div class="form-group">
                                            <label class="form-label" for="exampleInputPassword1">Password</label>
                                            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="exampleCheck1">
                                            <label for="exampleCheck1">Check me out</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary mb-4">Submit</button>
                                    </form>
                                </div>
                            </BModal>
                        </div>
                        <div class="pc-modal-content">
                            <pre style="display: none;">
                                </pre>
                            <BLink class="md-pc-modal-copy copy"><i class="ph-duotone ph-copy"></i></BLink>
                            <BLink class="pc-collapse"><i class="ph-duotone ph-code"></i></BLink>
                        </div>

                            <BCol class="col-md-6">
                                <button class="btn btn-primary mb-4">Add Region</button>
                                <form>
                                    <div class="form-group">
                                        <label class="form-label" for="exampleInputEmail1">Email address</label>
                                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                                        <small id="emailHelp" class="form-text text-muted">We'll never share your email with
                                            anyone
                                            else.</small>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label" for="exampleInputPassword1">Password</label>
                                        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                                        <label for="exampleCheck1">Check me out</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary mb-4">Submit</button>
                                </form>
                            </BCol>
                            
                        </BRow>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
    </Layout>
</template>