import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex); //安装 Vuex 插件

// 创建初始应用全局状态变量
const state = {
  count:1 //指我们的待办事项列表数据
};

// 定义所需的 mutations
const mutations={
        add(state){
            state.count+=1;
        },
        reduce(state){
            state.count-=1;
        }
    }

// 创建 store 实例并且导出
export default new Vuex.Store({
        state
    });
