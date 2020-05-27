<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/rsign">Add a Restaurant</router-link>
      <router-link to="/signin">Sign-In</router-link>
      <router-link to="/signup">Sign-Up</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {}
</script>
