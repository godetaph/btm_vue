import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import LogIn from '../views/dashboard/Login.vue'
import SignUp from '../views/dashboard/Signup.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Preferences from '../views/dashboard/Preferences.vue'
import Categories from '../views/dashboard/Categories.vue'
import Users from '../views/dashboard/Users.vue'
import Businesses from '../views/dashboard/Businesses.vue'
import Business from '../views/dashboard/Business.vue'
import AddBusiness from '../views/dashboard/AddBusiness.vue'
import EditBusiness from '../views/dashboard/EditBusiness.vue'
import Payments from '../views/dashboard/Payments.vue'
import AddPayment from '../views/dashboard/AddPayment.vue'
import EditPayment from '../views/dashboard/EditPayment.vue'
import DeletePayment from '../views/dashboard/DeletePayment.vue'
import AddCategory from '../views/dashboard/AddCategory.vue'
import EditCategory from '../views/dashboard/EditCategory.vue'
import DeleteCategory from '../views/dashboard/DeleteCategory.vue'
import Barangays from '../views/dashboard/Barangays.vue'
import AddBarangay from '../views/dashboard/AddBarangay.vue'
import EditBarangay from '../views/dashboard/EditBarangay.vue'
import DeleteBarangay from '../views/dashboard/DeleteBarangay.vue'
import BusinessCategories from '../views/dashboard/BusinessCategories.vue'
import AddBusinessCategory from '../views/dashboard/AddBusinessCategory.vue'
import EditBusinessCategory from '../views/dashboard/EditBusinessCategory.vue'
import DeleteBusinessCategory from '../views/dashboard/DeleteBusinessCategory.vue'
import Notifications from '../views/dashboard/Notifications.vue'
import DeleteNotification from '../views/dashboard/DeleteNotification.vue'
import Periods from '../views/dashboard/Periods.vue'
import AddPeriod from '../views/dashboard/AddPeriod.vue'
import EditPeriod from '../views/dashboard/EditPeriod.vue'
import DeletePeriod from '../views/dashboard/DeletePeriod.vue'
import Map from '../views/dashboard/Map.vue'
import BusinessPeriods from '../views/dashboard/BusinessPeriods'
import AddBusinessPeriod from '../views/dashboard/AddBusinessPeriod'
import EditBusinessPeriod from '../views/dashboard/EditBusinessPeriod'
import UploadCollection from '../views/dashboard/UploadCollection'

import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/map',
    name: 'Map',
    component: Map,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/preferences',
    name: 'Preferences',
    component: Preferences,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/users',
    name: 'Users',
    component: Users,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/categories',
    name: 'Categories',
    component: Categories,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/categories/add',
    name: 'AddCategory',
    component: AddCategory,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/categories/:id/edit',
    name: 'EditCategory',
    component: EditCategory,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/categories/:id/delete',
    name: 'DeleteCategory',
    component: DeleteCategory,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/businesses',
    name: 'Businesses',
    component: Businesses,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/businesses/add',
    name: 'AddBusiness',
    component: AddBusiness,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/businesses/:id',
    name: 'Business',
    component: Business,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/businesses/:id/edit',
    name: 'EditBusiness',
    component: EditBusiness,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/payments/:id',
    name: 'Payments',
    component: Payments,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/payments/:id/add',
    name: 'AddPayment',
    component: AddPayment,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/payments/:id/edit',
    name: 'EditPayment',
    component: EditPayment,
    props: true,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/payments/:id/delete',
    name: 'DeletePayment',
    component: DeletePayment,
    props: true,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-categories/:id',
    name: 'BusinessCategories',
    component: BusinessCategories,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-categories/:id/add',
    name: 'AddBusinessCategory',
    component: AddBusinessCategory,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-categories/:id/edit',
    name: 'EditBusinessCategory',
    component: EditBusinessCategory,
    props: true,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-categories/:id/delete',
    name: 'DeleteBusinessCategory',
    component: DeleteBusinessCategory,
    props: true,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/notifications',
    name: 'Notifications',
    component: Notifications,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/notifications/:id/delete',
    name: 'DeleteNotification',
    component: DeleteNotification,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/barangays',
    name: 'Barangays',
    component: Barangays,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/barangays/:id/edit',
    name: 'EditBarangay',
    component: EditBarangay,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/barangays/:id/delete',
    name: 'DeleteBarangay',
    component: DeleteBarangay,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/barangays/add',
    name: 'AddBarangay',
    component: AddBarangay,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/periods',
    name: 'Periods',
    component: Periods,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/periods/add',
    name: 'AddPeriod',
    component: AddPeriod,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/periods/:id/edit',
    name: 'EditPeriod',
    component: EditPeriod,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/periods/:id/delete',
    name: 'DeletePeriod',
    component: DeletePeriod,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-periods',
    name: 'BusinessPeriods',
    component: BusinessPeriods,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-periods/:id/edit',
    name: 'EditBusinessPeriod',
    component: EditBusinessPeriod,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/business-periods/:id/add',
    name: 'AddBusinessPeriod',
    component: AddBusinessPeriod,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/upload-collection',
    name: 'UploadCollection',
    component: UploadCollection,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  }else {
    next()
  }
})

export default router
