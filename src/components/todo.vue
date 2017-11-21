<template>
  <div>

    <el-row class="newtodo">
      <el-col :span="24">
        <i class="el-icon-date" style="margin-right:5px;"></i>{{todo.title}}
      </el-col>
      <el-col :span="24" style="margin-top:5px;">
        <input class="Addinput" type="text" v-model="text" placeholder="添加一个任务..." @keyup.enter="onAdd" />
      </el-col>
    </el-row>

    <el-row>
      <el-col :span="24">
        <div v-for="item in items">
          <item :item="item"></item>
        </div>
      </el-col>
    </el-row>

  </div>
</template>

<script>
  import item from './item'
  export default {
    data() {
      return {
        todo: {
          title: '大电影清单'
        },
        items: [
        { checked: true, text: '肖申克的救赎', isDelete: false },
        { checked: false, text: '香水', isDelete: false },
        { checked: false, text: '包法利夫人', isDelete: false }
        ],
        text: ''
      }
    },
    methods: {
      onAdd() {
        this.items.push({
          checked: false, text: this.text, isDelete: false
        }); // 当用户点击回车时候 ，给items的值新增一个对象，this.text 即输入框绑定的值
        this.text = ''; //初始化输入框的值。
      }
    },
    components: {
      item
    }
  }
</script>

<style>
::-webkit-input-placeholder { /* WebKit browsers */
  color: #FFF;
}
.newtodo {
  background-color: #58aad3;
  margin: 0px;
  height: 90px;
  padding: 10px;
  color: #FFF;
  font-weight: bolder;
  text-align : left;
}
.Addinput {
  padding-left:10px;
  border-radius:5px;
  height:40px;
  width:98%;
  border:none;
  outline:medium;
  background-color:#488eb2;
  color: #FFF;
  font-size:14px;
}

</style>
