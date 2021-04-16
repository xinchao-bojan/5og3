<template>
  <div id="app" class="main">
    <v-header/>
    <v-main-wrapper/>
    <v-footer/>
  </div>
</template>

<script>
import vMainWrapper from './components/main-wrapper'
import vHeader from './components/header'
import vFooter from './components/footer'

export default {
  setup () {

  },
  components: {
    vHeader,
    vMainWrapper,
    vFooter
  }
}
</script>
<style lang="scss">
html {
  height: 100%;
}

body {
  height: 100%;
}

.main {
  display: flex;
  flex-direction: column;
  height: 100%;
}
#app {
  height: 100%;
  margin: -10px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
