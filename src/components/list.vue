<template>
  <div>

    <el-row>
      <el-col :span="24">
          <el-button type="info" style="width: 100%; font-weight: bold;" @click="dialogFormVisible = true">新 建 清 单</el-button>
      </el-col>
    </el-row>

    <el-row v-for="list in lists">
      <el-col :span="18">
        <a>{{list.title}}</a>
      </el-col>
      <el-col :span="6">
        <i class="el-icon-edit" style="cursor:pointer" @click="dialogFormVisible = true"></i>
      </el-col>
    </el-row>

    <el-dialog title="清单名称" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item>
          <el-input v-model="listname" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">删除清单</el-button>
        <el-button type="primary" @click="listsAdd">确定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        lists: [{ title: '电影清单' }, { title: '购物清单' }, {title: '阅读清单' }],
        dialogFormVisible: false,
        listname: ''
      }
    },
    methods: {
      listsAdd() {
        this.lists.push({
          title: this.listname
        });
        this.listname = '';
        this.dialogFormVisible = false;
      }
    }
  }
</script>

<style>
.el-row {
  padding: 10px;
}

.el-col {
  border-radius: 4px;
}
</style>
