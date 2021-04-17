<template>
  <v-app>
    <div id="app" class="main">
      <vHeader/>
      <vMainWrapper/>
      <vFooter/>
    </div>
  </v-app>
</template>

<script>
import vMainWrapper from './components/main-wrapper'
import vHeader from './components/header'
import vFooter from './components/footer'
export default {
  name: 'App',
  components: {
    vHeader,
    vMainWrapper,
    vFooter,
  },
}
</script>

<style>
.main {
  padding-top: 64px;
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>