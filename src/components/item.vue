
<template>
  <div>
    <el-row class="itemcss">
      <el-col :span="1">
        <el-checkbox v-model="item.checked"></el-checkbox>
      </el-col>
      <el-col :span="22">
        <input v-model="item.text" style="border:0px;background-color:transparent;font-size:14px;" type="text" name="fname" />
      </el-col>
      <el-col :span="1">
              <i class="el-icon-delete"></i>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    props: ['item']
  }
</script>

<style>
.itemcss {
  border-radius:5px;
  box-shadow: 1px 1px 10px #ddd;
  text-align: left;
  padding: 10px;
  margin-top: 10px;
}
</style>
