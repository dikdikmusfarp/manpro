<template>
  <!-- Sidebar -->
  <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

    <!-- Sidebar - Brand -->
    <nuxt-link class="sidebar-brand d-flex align-items-center justify-content-center" to="/">
      <div class="sidebar-brand-icon rotate-n-15">
        <i class="fas fa-laugh-wink"></i>
      </div>
      <div class="sidebar-brand-text mx-3">M A N P R O</div>
    </nuxt-link>

    <!-- Divider -->
    <hr class="sidebar-divider my-0">

    <!-- Nav Item - Dashboard -->
    <li class="nav-item">
      <nuxt-link to="/" class="nav-link">
        <i class="fas fa-fw fa-tachometer-alt"></i>
        <span>Dashboard</span>
      </nuxt-link>
    </li>

    <!-- Divider -->
    <hr class="sidebar-divider">

    <!-- Heading -->
    <div class="sidebar-heading">
      Project Management
    </div>

    <!-- Nav Item - Charts -->
    <li class="nav-item">
      <nuxt-link to="/project" class="nav-link">
        <i class="fas fa-fw fa-chart-area"></i>
        <span>Project</span>
      </nuxt-link>
    </li>

    <!-- Nav Item - Tables -->
    <li class="nav-item">
      <nuxt-link to="/task" class="nav-link">
        <i class="fas fa-fw fa-chart-area"></i>
        <span>Task</span>
      </nuxt-link>
    </li>

    <!-- Divider -->
    <hr class="sidebar-divider d-none d-md-block">


  </ul>
  <!-- End of Sidebar -->
</template>

<script>
export default {
  data() {
    return {
      role: null,
    }
  },
  async created() {
  },
}
</script>
