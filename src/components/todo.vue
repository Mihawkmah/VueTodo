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
        items: [],
        text: ''
      }
    },
    watch: {
      '$route.params.id'() {
        // 监听$route.params.id的变化，如果这个id即代表用户点击了其他的待办项需要重新请求数据。
        this.init();
      }
    },
    created() {
      // created生命周期，在实例已经创建完成，页面还没渲染时调用init方法。
      this.init();
    },
    methods: {
      init() {
        // 获取到 $route下params下的id,即我们在list.vue组件处传入的数据。
        this.$ajax.post('http://127.0.0.1:5000/todos',{"listId": this.$route.params.id})
        .then(result => {
          this.items = result.data
        })
      },
      onAdd() {
        this.$ajax.post('http://127.0.0.1:5000/todos/add',{"listId": this.$route.params.id, "todoTitle": this.text})
        this.text = '';
        location.reload()
      },
      delTodo(item) {
        this.$ajax.post('http://127.0.0.1:5000/todos/delete',{"listId": this.$route.params.id, "item": item})
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
