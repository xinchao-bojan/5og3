<template>
  <div id="app" class="main">
    <vHeader/>
    <vMainWrapper/>
    <vFooter/>
  </div>
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
html {
  height: 100%;
}
a {
  color: #2c3e50;
  text-decoration: none;
}
body {
  height: 100%;
}
#app {
  font-family: Gost, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  margin: 0;
}
.main {
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>