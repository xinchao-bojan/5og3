<template>
  <div class="v-main-wrapper">
    <router-view/>
    
    <!-- Здесь будут отображаться компоненты, путь к которым ты пропишешь в router/index.js-->
  </div>
</template>

<script>
export default {
  setup () {

  }
}
</script>

<style lang="scss">
.v-main-wrapper {
  flex: 1 0 auto;
  background-color: #fff;
}
</style>
