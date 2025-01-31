<script>
import Layout from "@/layout/main.vue"
import pageheader from "@/components/page-header.vue"

export default {
    name: "DASHBOARD",
    components: {
        Layout, pageheader
    },
}
</script>

<template>
    <Layout>
        <pageheader title="Josh" pageTitle="Forms" />
        <BRow>
            <h1>This is it.</h1>
        </BRow>
    </Layout>
</template>