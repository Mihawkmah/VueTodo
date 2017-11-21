<template>

  <el-container>

    <el-aside width="200px"><list></list></el-aside>

    <el-container>
    <el-main><todo></todo></el-main>
    </el-container>

  </el-container>

</template>

<script>
  import list from './list'
  import todo from './todo'
  export default {
  data() {
    return {
      input: '输入任务名称'
    }
  },
  components: {
    list,
    todo
  }
  }
</script>

<style>
.el-container {
  height: 100vh;
  width:800px;
}

.el-aside {
  background-color: #283037;
  color: #fff;
}

.el-main {
  background-color: #fffbfb;
  color: #656d71;
  padding: 0px;
}

</style>
