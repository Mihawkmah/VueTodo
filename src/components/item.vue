
<template>
  <div>
    <el-row class="itemcss">
      <el-col :span="1">
        <el-checkbox id="item.completed" v-model="item.completed" ></el-checkbox>
      </el-col>
      <el-col :span="22">
        <input v-model="item.title" style="border:0px;background-color:transparent;font-size:14px;" type="text" name="fname" />
      </el-col>
      <el-col :span="1">
              <i class="el-icon-delete" style="cursor:pointer" @click="item.isdelete = true; todoUpd()"></i>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    props: {
      item:{},
      index:{},
      id:{},
      init:{}
    },
    methods: {
      todoUpd() {
        this.$ajax.post('http://127.0.0.1:5000/todos/update',{"id":this.id, "isdelete":this.item.isdelete, "index": this.index})
      }
    }
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
