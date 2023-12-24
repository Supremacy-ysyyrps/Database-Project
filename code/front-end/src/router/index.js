import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Welcome from '../components/Welcome.vue'
import Info from '../components/Info.vue'
import Purchase from '../components/Purchase.vue'
import Product from '../components/Product.vue'
import Sales from '../components/Sales.vue'
import Inventory from '../components/Inventory.vue'


Vue.use(VueRouter)
const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  {
    path: '/home',
    component: Home,
    redirect: '/welcome',
    children: [
      { path: '/welcome', component: Welcome },
      { path: '/info', component: Info },

      { path: '/purchase', component: Purchase },
      { path: '/product', component: Product },
      { path: '/sales', component: Sales },
      { path: '/inventory', component: Inventory}
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router