import { createWebHistory, createRouter } from "vue-router";
import routes from './routes';
import appConfig from "../../app.config";
import { useAuthStore } from '../stores/auth';


const router = createRouter({
    history: createWebHistory("/vue/"),
    routes,
  
});

router.beforeResolve(async (routeTo, routeFrom, next) => {
    // Create a `beforeResolve` hook, which fires whenever
    // `beforeRouteEnter` and `beforeRouteUpdate` would. This
    // allows us to ensure data is fetched even when params change,
    // but the resolved route does not. We put it in `meta` to
    // indicate that it's a hook we created, rather than part of
    // Vue Router (yet?).
    try {
        // For each matched route...
        for (const route of routeTo.matched) {
            await new Promise((resolve, reject) => {
                // If a `beforeResolve` hook is defined, call it with
                // the same arguments as the `beforeEnter` hook.
                if (route.meta && route.meta.beforeResolve) {
                    route.meta.beforeResolve(routeTo, routeFrom, (...args) => {
                        // If the user chose to redirect...
                        if (args.length) {
                            // If redirecting to the same route we're coming from...
                            // Complete the redirect.
                            next(...args);
                            reject(new Error('Redirected'));
                        } else {
                            resolve();
                        }
                    });
                } else {
                    // Otherwise, continue resolving the route.
                    resolve();
                }
            });
        }
        // If a `beforeResolve` hook chose to redirect, just return.
    } catch (error) {
        return;
    }
    document.title = routeTo.meta.title + ' | ' + appConfig.title;
    // If we reach this point, continue resolving the route.
    next();
});

router.beforeEach(async (to) => {
    // clear alert on route change
    // const alertStore = useAlertStore();
    // alertStore.clear();

    // redirect to login page if not logged in and trying to access a restricted page 
    const publicPages = ['/alogin', '/aregister'];
    const authRequired = !publicPages.includes(to.path);
    const authStore = useAuthStore();

    if (authRequired && !authStore.user) {
        authStore.returnUrl = to.fullPath;
        return '/alogin';
    }
});

export default router;