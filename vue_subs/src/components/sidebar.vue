<script>
import { ref, onMounted, onUnmounted } from 'vue';
import { ChevronDownIcon } from "@zhuowenli/vue-feather-icons";
import simplebar from "simplebar-vue";
import logoWhite from "@/assets/images/logo-white.svg";
import logoDark from "@/assets/images/logo-dark.svg";

export default {
    data() {
        return {
            logoDark: logoDark,
            logoWhite: logoWhite,
           }
    },
    setup() {
        const currentLogo = ref(logoDark);

        const updateLogo = () => {
            const isDarkTheme = document.body.getAttribute("data-pc-theme") === "dark";
            currentLogo.value = isDarkTheme ? logoWhite : logoDark;
        };
        

        onMounted(() => {
            updateLogo();

            const observer = new MutationObserver(() => {
                updateLogo();
            });

            observer.observe(document.body, {
                attributes: true,
                attributeFilter: ['data-pc-theme']
            });

            onUnmounted(() => {
                observer.disconnect();
            });
        });

        return { currentLogo };
    },
    components: {
        ChevronDownIcon, simplebar
    },
    methods: {
        changeLayoutType(layoutType) {
            // Update the layout type in the store
            this.$store.commit('changeLayoutType', { layoutType });
            // Set the layout attribute based on the layout type
            document.body.setAttribute('data-pc-layout', layoutType);
        },
    },
    computed: {
        layoutType: {
            get() {
                return this.$store.state.layout.layoutType;
            },
            set(layoutType) {
                this.$store.commit('changeLayoutType', { layoutType });
            },
        },
    },
    watch: {
        layoutType: {
            immediate: true,
            deep: true,
            handler(newVal, oldVal) {
                if (newVal !== oldVal) {
                    switch (newVal) {
                        case "horizontal":
                            document.body.setAttribute(
                                "data-pc-layout",
                                "horizontal"
                            );
                            break;
                        case "vertical":
                            document.body.setAttribute("data-pc-layout", "vertical");
                    }
                }
            },
        },
    },
    mounted() {
        const activeListItem = document.querySelector("li.active");
        if (activeListItem) {
            const parentElementOrSelf = activeListItem?.parentElement ? activeListItem.parentElement : activeListItem;
            if (parentElementOrSelf && !parentElementOrSelf.classList.contains("pc-navbar")) {
                const closestItem = parentElementOrSelf.parentElement.closest(".pc-item");
                if (closestItem) {
                    closestItem.classList.add("active");
                    closestItem.children[1].classList.add('show')
                }
            }
          
            /**
             * Sidebar menu collapse
             */
            if (document.querySelectorAll(".navbar-content .collapse")) {
                let collapses = document.querySelectorAll(".navbar-content .collapse");

                collapses.forEach((collapse) => {
                    // Hide sibling collapses on `show.bs.collapse`
                    collapse.addEventListener("show.bs.collapse", (e) => {
                        e.stopPropagation();
                        let closestCollapse = collapse.parentElement.closest(".collapse");
                        if (closestCollapse) {
                            let siblingCollapses =
                                closestCollapse.querySelectorAll(".collapse");
                            siblingCollapses.forEach((siblingCollapse) => {
                                if (siblingCollapse.classList.contains("show")) {
                                    siblingCollapse.classList.remove("show");
                                    siblingCollapse.parentElement.firstChild.setAttribute("aria-expanded", "false");
                                }
                            });
                        } else {
                            let getSiblings = (elem) => {
                                // Setup siblings array and get the first sibling
                                let siblings = [];
                                let sibling = elem.parentNode.firstChild;
                                // Loop through each sibling and push to the array
                                while (sibling) {
                                    if (sibling.nodeType === 1 && sibling !== elem) {
                                        siblings.push(sibling);
                                    }
                                    sibling = sibling.nextSibling;
                                }
                                return siblings;
                            };
                            let siblings = getSiblings(collapse.parentElement);
                            siblings.forEach((item) => {
                                if (item.childNodes.length > 2) {
                                    item.firstElementChild.setAttribute("aria-expanded", "false");
                                    item.firstElementChild.classList.remove("active");
                                }
                                let ids = item.querySelectorAll("*[id]");
                                ids.forEach((item1) => {
                                    item1.classList.remove("show");
                                    item1.parentElement.firstChild.setAttribute("aria-expanded", "false");
                                    item1.parentElement.firstChild.classList.remove("active");
                                    if (item1.childNodes.length > 2) {
                                        let val = item1.querySelectorAll("ul li a");

                                        val.forEach((subitem) => {
                                            if (subitem.hasAttribute("aria-expanded"))
                                                subitem.setAttribute("aria-expanded", "false");
                                        });
                                    }
                                });
                            });
                        }
                    });

                    // Hide nested collapses on `hide.bs.collapse`
                    collapse.addEventListener("hide.bs.collapse", (e) => {
                        e.stopPropagation();
                        let childCollapses = collapse.querySelectorAll(".collapse");
                        childCollapses.forEach((childCollapse) => {
                            let childCollapseInstance = childCollapse;
                            childCollapseInstance.classList.remove("show");
                            childCollapseInstance.parentElement.firstChild.setAttribute("aria-expanded", "false");
                        });
                    });
                });
            }


        } else {
            console.error("No list item with class 'active' found.");
        }
    }
};
</script>

<template>
    <div class="navbar-wrapper" id="navbar-wrapper">
        <div class="m-header">
            <router-link to="/" class="b-brand text-primary">
                <!-- ========   Change your logo from here   ============ -->
                <img v-if="currentLogo === logoDark" :src="logoDark" alt="logo image" class="logo-lg custom_logo">
                <img v-else :src="logoWhite" alt="logo image" class="logo-lg custom_logo">
                <img src="@/assets/images/favicon.svg" alt="" class="logo logo-sm"> <span class="badge bg-brand-color-2 rounded-pill ms-2 theme-version">v1.0</span>
            </router-link>
        </div>
        <simplebar data-simplebar class="navbar-content pc-trigger">
            <ul class="pc-navbar">
                <li class="pc-item pc-caption">
                    <label>Navigation</label>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse1" role="button" aria-expanded="false" aria-controls="collapse1">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-gauge"></i>
                        </span> <span class="pc-mtext"> Dashboard</span>
                        <span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                        <span class="pc-badge">2</span>
                    </BLink>
                    <div class="collapse" id="collapse1">
                        <ul class="pc-submenu">
                            <li class="pc-item" :class="{ 'active': $route.path === '/dashboard' }">
                                <router-link class="pc-link" to="/dashboard">Analytics</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/affiliate-dashboard' }">
                                <router-link class="pc-link" to="/affiliate-dashboard">Affiliate</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/finance' }">
                                <router-link class="pc-link" to="/finance">Finance</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/helpdesk-dashboard' }">
                                <router-link class="pc-link" to="/helpdesk-dashboard">Helpdesk</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/invoice' }">
                                <router-link class="pc-link" to="/invoice">Invoice</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse2" role="button" aria-expanded="false" aria-controls="collapse2">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-layout"></i></span><span class="pc-mtext">Layouts</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse2">
                        <ul class="pc-submenu">
                            <li class="pc-item" :class="{ 'active': $route.path === '/layout/horizontal' }">
                                <router-link class="pc-link" @click="changeLayoutType('horizontal')" to="/layout/horizontal">Horizontal</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/layout/layout-2' }">
                                <router-link class="pc-link" target="_blank" to="/layout/layout-2">Creative</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/layout/layout-moduler' }">
                                <router-link class="pc-link" target="_blank" to="/layout/layout-moduler">Moduler</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/dashboard' }">
                                <router-link class="pc-link" @click="changeLayoutType('vertical')" to="/dashboard">Vertical</router-link>
                            </li>
                        </ul>
                    </div>
                </li>

                <!-- Widget -->
                <li class="pc-item pc-caption">
                    <label> Widget</label>
                    <i class="ph-duotone ph-chart-pie"></i>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/josh' }">
                    <router-link to="/josh" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Josh</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/regions' }">
                    <router-link to="/regions" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Regions</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/address' }">
                    <router-link to="/address" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Address</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/subscription-plans' }">
                    <router-link to="/subscription-plans" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Subscription Plans</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/modems' }">
                    <router-link to="/modems" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Modems</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/issues' }">
                    <router-link to="/issues" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Issues</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/subscribers' }">
                    <router-link to="/subscribers" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Subscribers</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/subscriptions' }">
                    <router-link to="/subscriptions" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Subscriptions</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/collections' }">
                    <router-link to="/collections" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Collections</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/aregister' }">
                    <router-link to="/aregister" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Register</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/alogin' }">
                    <router-link to="/alogin" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Login</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/statistics' }">
                    <router-link to="/statistics" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-projector-screen-chart"></i>
                        </span>
                        <span class="pc-mtext"> Statistics</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/user' }">
                    <router-link to="/user" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-identification-card"></i>
                        </span>
                        <span class="pc-mtext"> User</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/data' }">
                    <router-link to="/data" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-database"></i>
                        </span>
                        <span class="pc-mtext"> Data</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/chart' }">
                    <router-link to="/chart" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-chart-pie"></i>
                        </span>
                        <span class="pc-mtext"> Chart</span>
                    </router-link>
                </li>

                <!-- App -->
                <li class="pc-item pc-caption">
                    <label> Application</label>
                    <i class="ph-duotone ph-buildings"></i>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/calendar' }">
                    <router-link to="/calendar" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-calendar-blank"></i>
                        </span>
                        <span class="pc-mtext"> Calendar</span></router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/chat' }">
                    <router-link to="/chat" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-chats-circle"></i>
                        </span>
                        <span class="pc-mtext"> Chat</span></router-link>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse3" role="button" aria-expanded="false" aria-controls="collapse3">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-image"></i>
                        </span>
                        <span class="pc-mtext">Gallery</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse3">
                        <ul class="pc-submenu">
                            <li class="pc-item" :class="{ 'active': $route.path === '/gallery-grid' }"><router-link class="pc-link" to="/gallery-grid">Grid</router-link></li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/gallery-masonry' }"><router-link class="pc-link" to="/gallery-masonry">Masonry</router-link></li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse4" role="button" aria-expanded="false" aria-controls="collapse4">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-shopping-cart"></i>
                        </span>
                        <span class="pc-mtext"> E-commerce</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse4">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/product' }"><router-link class="pc-link" to="/product">Product</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/product-details' }">
                                <router-link class="pc-link" to="/product-details"> Product
                                    details</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/product-list' }"><router-link class="pc-link" to="/product-list">Product
                                    List</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/add-product' }"><router-link class="pc-link" to="/add-product">Add New
                                    Product</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/checkout' }"><router-link class="pc-link" to="/checkout">Checkout</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse5" role="button" aria-expanded="false" aria-controls="collapse5">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-lifebuoy"></i>
                        </span>
                        <span class="pc-mtext">Helpdesk</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse5">
                        <ul class="pc-submenu">
                            <li class="pc-item pc-hasmenu" :class="{ 'active': this.$route.path === '/admins/helpdesk-create-ticket' || this.$route.path === '/admins/helpdesk-ticket' || this.$route.path === '/admins/helpdesk-ticket-details' }">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse35" role="button" aria-expanded="false" aria-controls="collapse35">
                                    <span class="pc-mtext">Ticket</span><span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse35">
                                    <ul class="pc-submenu">
                                        <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/helpdesk-create-ticket' }"><router-link class="pc-link" to="/admins/helpdesk-create-ticket">Create</router-link></li>
                                        <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/helpdesk-ticket' }"><router-link class="pc-link" to="/admins/helpdesk-ticket">List</router-link></li>
                                        <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/helpdesk-ticket-details' }"><router-link class="pc-link" to="/admins/helpdesk-ticket-details">Details</router-link></li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/admins/helpdesk-customer' }"><router-link class="pc-link" to="/admins/helpdesk-customer">Customer</router-link></li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse6" role="button" aria-expanded="false" aria-controls="collapse6">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-newspaper"></i>
                        </span>
                        <span class="pc-mtext"> Invoice 1</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse6">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/invoice-list' }"><router-link class="pc-link" to="/invoice-list">Invoice
                                    List</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/create' }"><router-link class="pc-link" to="/create">Create</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/preview' }"><router-link class="pc-link" to="/preview">Preview</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse7" role="button" aria-expanded="false" aria-controls="collapse7">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-newspaper"></i>
                        </span>
                        <span class="pc-mtext"> Invoice 2</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse7">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/invoice-create' }"><router-link class="pc-link" to="/admins/invoice-create">Create</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/invoice-view' }"><router-link class="pc-link" to="/admins/invoice-view">Details</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/invoice-list' }"><router-link class="pc-link" to="/admins/invoice-list">List</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/invoice-edit' }"><router-link class="pc-link" to="/admins/invoice-edit">Edit</router-link></li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/mail' }">
                    <router-link to="/mail" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-envelope-open"></i>
                        </span>
                        <span class="pc-mtext"> Mail</span></router-link>
                </li>

                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse8" role="button" aria-expanded="false" aria-controls="collapse8">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-identification-badge"></i>
                        </span>
                        <span class="pc-mtext">Membership</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse8">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/membership-dashboard' }"><router-link class="pc-link" to="/admins/membership-dashboard">Dashboard</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/membership-list' }"><router-link class="pc-link" to="/admins/membership-list">List</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/membership-pricing' }"><router-link class="pc-link" to="/admins/membership-pricing">Pricing</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/admins/membership-setting' }"><router-link class="pc-link" to="/admins/membership-setting">Setting</router-link></li>
                        </ul>
                    </div>
                </li>

                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse9" role="button" aria-expanded="false" aria-controls="collapse9">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-identification-badge"></i>
                        </span>
                        <span class="pc-mtext">Online Courses</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse9">
                        <ul class="pc-submenu">
                            <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-dashboard' }"><router-link class="pc-link" to="/admins/course-dashboard">Dashboard</router-link></li>
                            <li class="pc-item pc-hasmenu" :class="{ 'active': this.$route.path === '/admins/course-teacher-list' || this.$route.path === '/admins/course-teacher-apply' || this.$route.path === '/admins/course-teacher-add' }">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse10" role="button" aria-expanded="false" aria-controls="collapse10">
                                    Teacher
                                    <span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse10">
                                    <ul class="pc-submenu">
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-teacher-list' }"><router-link class="pc-link" to="/admins/course-teacher-list">List</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-teacher-apply' }"><router-link class="pc-link" to="/admins/course-teacher-apply">Apply</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-teacher-add' }"><router-link class="pc-link" to="/admins/course-teacher-add">Add</router-link></li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item pc-hasmenu" :class="{ 'active': this.$route.path === '/admins/course-student-list' || this.$route.path === '/admins/course-student-apply' || this.$route.path === '/admins/course-student-add' }">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse11" role="button" aria-expanded="false" aria-controls="collapse11">
                                    Student
                                    <span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse11">
                                    <ul class="pc-submenu">
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-student-list' }"><router-link class="pc-link" to="/admins/course-student-list">List</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-student-apply' }"><router-link class="pc-link" to="/admins/course-student-apply">Apply</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-student-add' }"><router-link class="pc-link" to="/admins/course-student-add">Add</router-link></li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item pc-hasmenu" :class="{ 'active': this.$route.path === '/admins/course-course-view' || this.$route.path === '/admins/course-course-add' }">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse12" role="button" aria-expanded="false" aria-controls="collapse12">
                                    Courses
                                    <span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse12">
                                    <ul class="pc-submenu">
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-course-view' }"><router-link class="pc-link" to="/admins/course-course-view">View</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-course-add' }"><router-link class="pc-link" to="/admins/course-course-add">Add</router-link></li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-pricing' }"><router-link class="pc-link" to="/admins/course-pricing">Pricing</router-link></li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-site' }"><router-link class="pc-link" to="/admins/course-site">Site</router-link></li>
                            <li class="pc-item pc-hasmenu" :class="{ 'active': this.$route.path === '/admins/course-setting-payment' || this.$route.path === '/admins/course-setting-pricing' || this.$route.path === '/admins/course-setting-notifications' }">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse13" role="button" aria-expanded="false" aria-controls="collapse13">
                                    Setting
                                    <span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse13">
                                    <ul class="pc-submenu">
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-setting-payment' }"><router-link class="pc-link" to="/admins/course-setting-payment">Payment</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-setting-pricing' }"><router-link class="pc-link" to="/admins/course-setting-pricing">Pricing</router-link></li>
                                        <li class="pc-item" :class="{ 'active': $route.path === '/admins/course-setting-notifications' }"><router-link class="pc-link" to="/admins/course-setting-notifications">Notifications</router-link></li>
                                    </ul>
                                </div>
                            </li>
                        </ul>
                    </div>

                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/application/plans' }">
                    <router-link to="/application/plans" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-envelope-open"></i>
                        </span>
                        <span class="pc-mtext"> Plans</span></router-link>
                </li>

                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse14" role="button" aria-expanded="false" aria-controls="collapse14">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-user-circle"></i>
                        </span>
                        <span class="pc-mtext"> Users</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse14">
                        <ul class="pc-submenu">
                            <li class="pc-item" :class="{ 'active': $route.path === '/account-profile' }">
                                <router-link class="pc-link" to="/account-profile">Account
                                    Profile</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/social-media' }"><router-link class="pc-link" to="/social-media">Social
                                    media</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/user-card' }"><router-link class="pc-link" to="/user-card">User
                                    Card</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/user-list' }"><router-link class="pc-link" to="/user-list">User
                                    List</router-link>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/team' }"><router-link class="pc-link" to="/team">Team</router-link>
                            </li>
                        </ul>
                    </div>
                </li>

                <!-- Pages -->
                <li class="pc-item pc-caption">
                    <label>Pages</label>
                    <i class="ph-duotone ph-devices"></i>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse15" role="button" aria-expanded="false" aria-controls="collapse15">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-shield-checkered"></i>
                        </span>
                        <span class="pc-mtext"> Authentication</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse15">
                        <ul class="pc-submenu">
                            <li class="pc-item pc-hasmenu">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse16" role="button" aria-expanded="false" aria-controls="collapse16">
                                    Authentication 1<span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse16">
                                    <ul class="pc-submenu">
                                        <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/login-v1">Login</router-link>
                                        </li>
                                        <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/register-v1">Register</router-link>
                                        </li>
                                        <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/forgot-password-v1">Forgot
                                                Password</router-link></li>
                                        <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/reset-password-v1">reset
                                                password</router-link> </li>
                                        <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/code-verification-v1">code
                                                verification</router-link></li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item pc-hasmenu">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse17" role="button" aria-expanded="false" aria-controls="collapse17">
                                    Authentication 2<span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span>
                                </BLink>
                                <div class="collapse" id="collapse17">
                                    <ul class="pc-submenu">
                                        <li class="pc-item"><router-link class="pc-link" target="_blank" to="/login-v2">Login</router-link>
                                        </li>
                                        <li class="pc-item"><router-link class="pc-link" target="_blank" to="/register-v2">Register</router-link>
                                        </li>
                                        <li class="pc-item"><router-link class="pc-link" target="_blank" to="/forgot-password-v2">Forgot
                                                password</router-link> </li>
                                        <li class="pc-item"><router-link class="pc-link" target="_blank" to="/reset-password-v2">reset
                                                password</router-link> </li>
                                        <li class="pc-item"><router-link class="pc-link" target="_blank" to="/code-verification-v2">code
                                                verification</router-link></li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item" :class="{ 'active': $route.path === '/login-modal' }"><router-link class="pc-link" to="/login-modal">Login Modal</router-link></li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse18" role="button" aria-expanded="false" aria-controls="collapse18">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-wrench"></i>
                        </span>
                        <span class="pc-mtext"> Maintenance</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse18">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/error-404">Error
                                    404</router-link>
                            </li>
                            <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/connection-lost">Connection
                                    lost</router-link></li>
                            <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/under-construction">Under
                                    Construction</router-link></li>
                            <li class="pc-item ms-4"><router-link class="pc-link" target="_blank" to="/comming-soon">Coming
                                    soon</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/contact-us' }"><router-link to="/contact-us" class="pc-link"><span class="pc-micon"><i class="ph-duotone ph-target"></i> </span><span class="pc-mtext">Contact Us</span></router-link></li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/' }"><router-link to="/" class="pc-link" target="_blank"><span class="pc-micon">
                            <i class="ph-duotone ph-rocket"></i> </span><span class="pc-mtext pc-icon-link">Landing <i class="ti ti-link text-primary f-14"></i></span></router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/loading' }"><router-link to="/loading" class="pc-link"><span class="pc-micon">
                            <i class="ph-duotone ph-fan"></i> </span><span class="pc-mtext">Loading</span></router-link>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse19" role="button" aria-expanded="false" aria-controls="collapse19">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-magnifying-glass"></i>
                        </span>
                        <span class="pc-mtext">Search</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse19">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/search-page' }"><router-link class="pc-link" to="/search-page">Search Page</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/contact-search' }"><router-link class="pc-link" to="/contact-search">Contact Search</router-link></li>
                        </ul>
                    </div>

                </li>
                <li class="pc-item" :class="{ 'active': $route.path === '/setting' }"><router-link class="pc-link" to="/setting">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-globe"></i>
                        </span>
                        <span class="pc-mtext">Site Settings</span>
                    </router-link>
                </li>
                <!-- UI Components -->
                <li class="pc-item pc-caption">
                    <label> UI Components</label>
                    <i class="ph-duotone ph-compass-tool"></i>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/components' }">
                    <router-link to="/components" class="pc-link" target="_blank">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-compass-tool"></i>
                        </span><span class="pc-mtext">Components <i class="ti ti-link text-primary f-14"></i></span></router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/animation' }">
                    <router-link to="/animation" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-flower"></i>
                        </span><span class="pc-mtext">Animation</span></router-link>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse20" role="button" aria-expanded="false" aria-controls="collapse20">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-flower-lotus"></i></span><span class="pc-mtext"> Icons</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse20">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/feather' }"><router-link class="pc-link" to="/feather">Feather</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/tabler' }"><router-link class="pc-link" to="/tabler">Tabler</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/phosphor' }"><router-link class="pc-link" to="/phosphor">Phosphor</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <!-- Forms -->
                <li class="pc-item pc-caption">
                    <label> Forms</label>
                    <i class="ph-duotone ph-textbox"></i>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse21" role="button" aria-expanded="false" aria-controls="collapse21">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-textbox"></i>
                        </span>
                        <span class="pc-mtext"> Forms Elements</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse21">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/form-element' }"><router-link class="pc-link" to="/form-element"> Form
                                    Basic</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/floating' }"><router-link class="pc-link" to="/floating">Form
                                    Floating</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/form-option' }"><router-link class="pc-link" to="/form-option">Form
                                    Options</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/input-group' }"><router-link class="pc-link" to="/input-group">Input
                                    Groups</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/checkbox' }"><router-link class="pc-link" to="/checkbox">Checkbox</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/radio' }"><router-link class="pc-link" to="/radio">Radio</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/switch' }"><router-link class="pc-link" to="/switch">Switch</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/mega-option' }"><router-link class="pc-link" to="/mega-option">Mega
                                    option</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse22" role="button" aria-expanded="false" aria-controls="collapse22">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-windows-logo"></i>
                        </span>
                        <span class="pc-mtext"> Form Layouts</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse22">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/layouts' }"><router-link class="pc-link" to="/layouts">Layouts</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/multicolumn' }"><router-link class="pc-link" to="/multicolumn">Multicolumn</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/actionbars' }"><router-link class="pc-link" to="/actionbars">Actionbars</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/sticky-action' }">
                                <router-link class="pc-link" to="/sticky-action"> Sticky Action bars</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse23" role="button" aria-expanded="false" aria-controls="collapse23">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-cloud-arrow-up"></i>
                        </span>
                        <span class="pc-mtext"> File upload</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse23">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/dropzone' }"><router-link class="pc-link" to="/dropzone">Dropzone</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item" :class="{ 'active': $route.path === '/form2_wizard' }">
                    <router-link to="/form2_wizard" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-tabs"></i>
                        </span>
                        <span class="pc-mtext">wizard</span></router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/validation' }">
                    <router-link to="/validation" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-password"></i>
                        </span>
                        <span class="pc-mtext"> Form Validation</span>
                    </router-link>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/image-croper' }"><router-link to="/image-croper" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-crop"></i>
                        </span>
                        <span class="pc-mtext"> Image cropper</span></router-link>
                </li>
                <!-- Table -->
                <li class="pc-item pc-caption">
                    <label>table</label>
                    <i class="ph-duotone ph-table"></i>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse24" role="button" aria-expanded="false" aria-controls="collapse24">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-table"></i>
                        </span>
                        <span class="pc-mtext"> Bootstrap Table</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse24">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/basic-table' }"><router-link class="pc-link" to="/basic-table">Basic
                                    table</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/sizing-table' }"><router-link class="pc-link" to="/sizing-table">Sizing
                                    table</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/border-table' }"><router-link class="pc-link" to="/border-table">Border
                                    table</router-link></li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/styling-table' }">
                                <router-link class="pc-link" to="/styling-table">Styling
                                    table</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse25" role="button" aria-expanded="false" aria-controls="collapse25">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-grid-nine"></i>
                        </span>
                        <span class="pc-mtext"> Vanilla Table</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse25">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/basic' }"><router-link class="pc-link" to="/basic">Basic
                                    initialization</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/method' }"><router-link class="pc-link" to="/method">Methods</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/row' }"><router-link class="pc-link" to="/row">Add
                                    Rows</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <!-- chart & Map -->
                <li class="pc-item pc-caption">
                    <label> Charts &amp; Maps</label>
                    <i class="ph-duotone ph-chart-pie-slice"></i>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse26" role="button" aria-expanded="false" aria-controls="collapse26">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-chart-donut"></i>
                        </span>
                        <span class="pc-mtext">Charts</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse26">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/apexchart' }"><router-link class="pc-link" to="/apexchart">Apex Chart</router-link></li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse27" role="button" aria-expanded="false" aria-controls="collapse27">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-map-trifold"></i>
                        </span>
                        <span class="pc-mtext"> Maps</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse27">
                        <ul class="pc-submenu">
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/v-maps' }"><router-link class="pc-link" to="/v-maps">Vector Map</router-link>
                            </li>
                            <li class="pc-item ms-4" :class="{ 'active': $route.path === '/maps' }"><router-link class="pc-link" to="/maps">Google Map</router-link>
                            </li>
                        </ul>
                    </div>
                </li>


                <!-- other -->
                <li class="pc-item pc-caption">
                    <label> Other</label>
                    <i class="ph-duotone ph-suitcase"></i>
                </li>
                <li class="pc-item pc-hasmenu">
                    <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse28" role="button" aria-expanded="false" aria-controls="collapse28">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-tree-structure"></i> </span><span class="pc-mtext"> Menu levels</span><span class="pc-arrow">
                            <ChevronDownIcon></ChevronDownIcon>
                        </span>
                    </BLink>
                    <div class="collapse" id="collapse28">
                        <ul class="pc-submenu">
                            <li class="pc-item">
                                <BLink class="pc-link"> Level 2.1</BLink>
                            </li>
                            <li class="pc-item pc-hasmenu">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse29" role="button" aria-expanded="false" aria-controls="collapse29">
                                    Level 2.2<span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span></BLink>
                                <div class="collapse" id="collapse29">
                                    <ul class="pc-submenu">
                                        <li class="pc-item">
                                            <BLink class="pc-link"> Level 3.1</BLink>
                                        </li>
                                        <li class="pc-item">
                                            <BLink class="pc-link"> Level 3.2</BLink>
                                        </li>
                                        <li class="pc-item pc-hasmenu">
                                            <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse30" role="button" aria-expanded="false" aria-controls="collapse30">
                                                Level 3.3<span class="pc-arrow">
                                                    <ChevronDownIcon></ChevronDownIcon>
                                                </span></BLink>
                                            <div class="collapse" id="collapse30">
                                                <ul class="pc-submenu">
                                                    <li class="pc-item">
                                                        <BLink class="pc-link"> Level 4.1</BLink>
                                                    </li>
                                                    <li class="pc-item">
                                                        <BLink class="pc-link"> Level 4.2</BLink>
                                                    </li>
                                                </ul>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </li>
                            <li class="pc-item pc-hasmenu">
                                <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse31" role="button" aria-expanded="false" aria-controls="collapse31">
                                    Level 2.3<span class="pc-arrow">
                                        <ChevronDownIcon></ChevronDownIcon>
                                    </span></BLink>
                                <div class="collapse" id="collapse31">
                                    <ul class="pc-submenu">
                                        <li class="pc-item">
                                            <BLink class="pc-link"> Level 3.1</BLink>
                                        </li>
                                        <li class="pc-item">
                                            <BLink class="pc-link"> Level 3.2</BLink>
                                        </li>
                                        <li class="pc-item pc-hasmenu">
                                            <BLink class="pc-link" data-bs-toggle="collapse" href="#collapse32" role="button" aria-expanded="false" aria-controls="collapse32">
                                                Level 3.3<span class="pc-arrow">
                                                    <ChevronDownIcon></ChevronDownIcon>
                                                </span></BLink>
                                            <div class="collapse" id="collapse32">
                                                <ul class="pc-submenu">
                                                    <li class="pc-item">
                                                        <BLink class="pc-link"> Level 4.1</BLink>
                                                    </li>
                                                    <li class="pc-item">
                                                        <BLink class="pc-link"> Level 4.2</BLink>
                                                    </li>
                                                </ul>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="pc-item" :class="{ 'active': this.$route.path === '/sample-page' }"><router-link to="/sample-page" class="pc-link">
                        <span class="pc-micon">
                            <i class="ph-duotone ph-desktop"></i>
                        </span>
                        <span class="pc-mtext"> Sample page</span></router-link>
                </li>
            </ul>

            <div class="card nav-action-card bg-brand-color-4">
                <div class="card-body" :style="{ 'background-image': 'url(' + require('@/assets/images/layout/nav-card-bg.svg') + ')' }">
                    <h5 class="text-dark">Help Center</h5>
                    <p class="text-dark text-opacity-75">Please contact us for more questions.</p>
                    <BLink href="#" class="btn btn-primary" target="_blank">Go to help
                        Center</BLink>
                </div>
            </div>
        </simplebar>
        <BCard no-body class="pc-user-card">
            <BCardBody>
                <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                        <img src="@/assets/images/user/avatar-1.jpg" alt="user-image" class="user-avtar wid-45 rounded-circle">
                    </div>
                    <div class="flex-grow-1 ms-3 me-2">
                        <h6 class="mb-0">Jonh Smith</h6>
                        <small>Administrator</small>
                    </div>
                    <BDropdown variant="purple" dropup no-caret toggle-class="p-0">
                        <template v-slot:button-content>
                            <span class="btn btn-icon btn-link-secondary avtar arrow-none p-0 dropdown-toggle">
                                <i class="ph-duotone ph-windows-logo"></i>
                            </span>
                        </template>
                        <BRow xl="6">
                            <BCol xl="6">
                                <BDropdownItem class="pc-user-links p-0">
                                        <i class="ph-duotone ph-user"></i>
                                        <br>
                                        <span>My Account</span>
                                </BDropdownItem>
                                <BDropdownDivider />
                                <BDropdownItem class="pc-user-links p-0">
                                    <i class="ph-duotone ph-lock-key"></i> <br>
                                    <span>Lock Screen</span>
                                </BDropdownItem>
                                <BDropdownDivider />
                            </BCol>
                            <BCol xl="6">
                                <BDropdownItem class="pc-user-links p-0">
                                    <i class="ph-duotone ph-gear"></i> <br>
                                    <span>Settings</span>
                                </BDropdownItem>
                                <BDropdownDivider />
                                <BDropdownItem class="pc-user-links p-0">
                                    <i class="ph-duotone ph-power"></i> <br>
                                    <span>Logout</span>
                                </BDropdownItem>
                                <BDropdownDivider />
                            </BCol>
                        </BRow>
                    </BDropdown>
                </div>
            </BCardBody>
        </BCard>
    </div>
</template>

