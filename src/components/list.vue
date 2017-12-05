<template>
  <div>
    <!-- 新建清单按钮 -->
    <el-row>
      <el-col :span="24">
          <el-button type="info" style="width: 100%; font-weight: bold;" @click="addListVisible = true">新 建 清 单</el-button>
      </el-col>
    </el-row>

    <!-- 清单列表+编辑按钮 -->
    <el-row v-for="list in lists">
      <el-col :span="18">
        <a>{{list.title}}</a>
      </el-col>
      <el-col :span="6">
        <i class="el-icon-edit" style="cursor:pointer" @click="goList(list._id,list.title)"></i>
      </el-col>
    </el-row>

    <!-- 新建清单弹出框 -->
    <el-dialog title="清单名称" :visible.sync="addListVisible">
      <el-form :model="form">
        <el-form-item>
          <el-input v-model="listtitle" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addListVisible = false">取消</el-button>
        <el-button type="primary" @click="listAdd">保存</el-button>
      </div>
    </el-dialog>

    <!-- 编辑清单弹出框 -->
    <el-dialog title="清单名称" :visible.sync="editListVisible">
      <el-form :model="form">
        <el-form-item>
          <el-input v-model="listtitle" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="listDel()">删除清单</el-button>
        <el-button type="primary" @click="listUpd">确定修改</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        lists: [],
        addListVisible: false,
        editListVisible: false,
        listtitle: '',
        listId: ''
      }
    },
    // 使用axios请求数据
    mounted() {
      this.$ajax.get('http://127.0.0.1:5000/')
      .then(result => {
        this.lists = result.data
      })
    },
    methods: {
      goList(id,title) {
        this.listId = id,
        this.listtitle = title,
        this.editListVisible = true
      },
      listAdd() {
        this.$ajax.post('http://127.0.0.1:5000/add',{"title": this.listtitle})
        .then(result => {
          this.lists = result.data
        }),
        this.listtitle = '';
        this.addListVisible = false;
      },
      listDel() {
        this.$ajax.post('http://127.0.0.1:5000/delete',{"listId": this.listId})
        .then(result => {
          this.lists = result.data
        })
        this.editListVisible = false
      },
      listUpd() {
        this.$ajax.post('http://127.0.0.1:5000/update',{"listId": this.listId,"title":this.listtitle})
        .then(result => {
          this.lists = result.data
        })
        this.editListVisible = false
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
