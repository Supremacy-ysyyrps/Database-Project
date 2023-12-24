<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>进货信息管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:搜索部分 -->
    <el-form v-model="getpurchaseQueryInfo">
      <el-row :gutter="20">
        <el-col :span="10">
          <el-form-item label="进货编号：">
            <el-input placeholder="请输入进货编号" style="width: 400px" v-model="getpurchaseQueryInfo.query"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item style="margin-left: 100px">
            <el-button type="primary" icon="el-icon-search" @click="getpurchaseById_query(getpurchaseQueryInfo.query)">查询</el-button>
            <el-button type="danger" icon="el-icon-refresh" @click="getpurchaseNoLike">重置</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog
      title="查询进货信息"
      :visible.sync="querypurchaseDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>进货信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>查询进货信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 进货信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="进货编号：">
              <el-input style="width: 800px" v-model="purchaseById_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品编号：">
              <el-input style="width: 800px" v-model="purchaseById_query[1]" disabled></el-input>
            </el-form-item>
            <el-form-item label="进货数量：">
              <el-input style="width: 800px" v-model="purchaseById_query[2]" disabled></el-input>
            </el-form-item>
            <el-form-item label="进货商品单价：">
               <el-input style="width: 800px" v-model="purchaseById_query[3]" disabled></el-input>
            </el-form-item>
            <el-form-item label="进货日期：">
               <el-input style="width: 800px" v-model="purchaseById_query[4]" disabled></el-input>
            </el-form-item>
          </el-form>

        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="querypurchaseDialogVisible = false">关 闭</el-button>
      </span>
    </el-dialog>

    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:列表部分 -->
    <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addpurchaseDialogVisible = true">新增进货信息</el-button>
    <el-table
      :data="purchaseList"
      border
      style="width: 100%">
      <el-table-column
        prop="PR_ID"
        label="进货编号"
        align="center"
        width="150px">
        <template slot-scope="purchaseList">
          <p v-text="purchaseList.row[0]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="P_ID"
        label="商品编号"
        align="center">
        <template slot-scope="purchaseList">
          <p v-text="purchaseList.row[1]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="PR_Num"
        label="进货数量"
        align="center">
        <template slot-scope="purchaseList">
          <p v-text="purchaseList.row[2]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="PR_UnitPrice"
        label="进货商品单价"
        align="center">
        <template slot-scope="purchaseList">
          <p v-text="purchaseList.row[3]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="PR_Date"
        label="进货日期"
        align="center"
        width="150px">
        <template slot-scope="purchaseList">
          <p v-text="purchaseList.row[4]"></p>
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        width="265px"
        align="center">
        <template slot-scope="purchaseList">
          <el-button type="danger" icon="el-icon-delete" size="mini" @click="deletepurchaseById(purchaseList.row[0])">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加进货对话框 -->
    <el-dialog
      title="新增进货信息"
      :visible.sync="addpurchaseDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>进货信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>新增进货信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 进货信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form :model="addpurchaseForm">
            <el-form-item label="进货编号：" required="true">
              <el-input style="width: 800px" v-model="addpurchaseForm.PR_ID"></el-input>
            </el-form-item>
            <el-form-item label="商品编号：" required="true">
              <el-input style="width: 800px" v-model="addpurchaseForm.P_ID"></el-input>
            </el-form-item>
            <el-form-item label="进货数量：" required="true">
              <el-input style="width: 800px" v-model="addpurchaseForm.PR_Num"></el-input>
            </el-form-item>
            <el-form-item label="进货商品单价：" required="true">
              <el-input style="width: 800px" v-model="addpurchaseForm.PR_UnitPrice"></el-input>
            </el-form-item>
            <el-form-item label="进货日期：" required="true">
              <el-input style="width: 800px" v-model="addpurchaseForm.PR_Date"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addpurchaseDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addpurchase()">提 交</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';
  
export default {
  name: 'purchase',
  data () {
    return {
      addpurchaseForm: {
        PR_ID:'',
        P_ID: '',
        PR_Num: '',
        PR_UnitPrice: '',
        PR_Date:'',
        password:''
      },
      getpurchaseQueryInfo: {
        query: '',
        pageSize: 5,
        pageNum: 1
      },
      getpurchaseByIdInfo: {
        PR_ID: ''
      },
      updatepurchaseInfo: {
        PR_ID: '',
        PR_Num: '',
        PR_UnitPrice: '',
        PR_Date: ''
      },
      deletepurchaseByIdInfo: {
        PR_ID: ''
      },
      purchaseById: {},
      purchaseById_query:{},
      total: 0,
      purchaseList: [],
      // 控制添加对话框显示与隐藏
      addpurchaseDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      updatepurchaseDialogVisible: false,
      // 控制查询对话框显示与隐藏
      querypurchaseDialogVisible:false
    }
  },
  created () {
    this.getpurchaseList()
  },
  methods: {


    addpurchase() {
      const {
        PR_ID,
        P_ID,
        PR_Num,
        PR_UnitPrice,
        PR_Date
      } = this.addpurchaseForm;

      if (PR_ID !== '' && P_ID !== '' && PR_Num !== '' &&
        PR_UnitPrice !== '' && PR_Date !== '') {

        const params = new URLSearchParams({
          PR_ID,
          P_ID,
          PR_Num,
          PR_UnitPrice,
          PR_Date
        });

        axios.get('http://8.134.218.23:8888/purchase/add_purchase', { params })
          .then(response => {
            let result = response.data;
            if (result.error === false) {
              this.$router.push('/purchase');
              this.addpurchaseDialogVisible = false;
              this.getpurchaseList();
              this.$message.success(result.message);
            } else {
              this.$message.error(result.message);
            }
          })
          .catch(error => {
            console.error('添加进货信息失败:', error);
            this.$message.error('添加进货信息失败');
          });

      } else {
        alert('输入有误，请重新输入！');
      }
    },


    getpurchaseList() {
      // 发送请求
      const params = {
        page: this.pageNum,
        pageSize: this.pageSize,
      };

      axios.get('http://8.134.218.23:8888/purchase/get_all_purchase', { params })
        .then(response => {
          // 获取响应数据
          let result = response.data
          if (result && result.error === false) { // 检查是否有错误
            this.purchaseList = result.result;
            this.total = result.total || 0;

          } else {
            this.$message.warning(result.message)
          }
        })
        .catch(error => {
          console.error('获取进货列表时出现错误:', error);
          this.$message.error('获取进货列表失败!')
        })
    },


    getpurchaseById(PR_ID) {
      axios.get('http://8.134.218.23:8888/purchase/get_by_pr_id_purchase', {
        params: {
          PR_ID: PR_ID
        }
      })
      .then(response => {
        let result = response.data
        if (result && result.error === false) {
          this.updatepurchaseDialogVisible = true
          this.purchaseById = result.result
        } else {
          this.$message.error(result.message)
        }
      })
      .catch(error => {
        console.error('获取进货信息时出现错误:', error);
        this.$message.error('获取进货信息失败!')
      });
    },


    getpurchaseById_query(PR_ID) {
      // 重置状态
      this.querypurchaseDialogVisible = false;
      this.purchaseById_query = {};

      // 发起 GET 请求
      axios.get('http://8.134.218.23:8888/purchase/get_by_pr_id_purchase', {
        params: {
          PR_ID: PR_ID
        }
      })
      .then(response => {
        console.log('Response from server:', response.data);
        let result = response.data;
        if (result.result && result.result.length > 0) {
          this.querypurchaseDialogVisible = true;
          this.purchaseById_query = result.result[0];
        } else {
          this.$message.error(result.message);
        }
      })
      .catch(error => {
        console.error('获取进货信息时出现错误:', error);
        this.$message.error('获取进货信息失败!');
      });
    },


    deletepurchaseById(PR_ID) {
      if (confirm('确定要删除吗?')) {
        axios({
          method: 'post',
          url: 'http://8.134.218.23:8888/purchase/del_purchase',
          params: {
            Type: 'PR_ID',
            ID: PR_ID,
          },
        })
        .then(response => {
          let result = response.data;
          console.log(result);

          if (result.error === false) {
            // 输出详细信息，成功
            console.log('删除进货信息结果:', result.message || '未知结果');
            this.$message.success(result.message);  // 输出成功的提示消息

            // 可选：更新其他界面或执行其他操作
            this.getpurchaseByIdInfo.pageNum = 1;
            this.getpurchaseList();
          } else {
            // 输出详细错误信息，删除失败
            console.error('删除进货信息失败:', result.message || '未知错误');
            this.$message.error('删除进货信息失败: ' + (result.message || '未知错误'));  // 输出删除失败的提示消息
          }
        })
        .catch(error => {
          // 输出请求失败的错误信息
          console.error('请求失败:', error);
          this.$message.error('请求失败，请稍后重试');
        });
      }
    },


    handleSizeChange (newSize) {
      this.getpurchaseQueryInfo.pageSize = newSize
      this.getpurchaseList()
    },
    handleCurrentChange (newSize) {
      this.getpurchaseQueryInfo.pageNum = newSize
      this.getpurchaseList()
    },
    getpurchaseByLike (newQuery) {
      this.query = newQuery
      this.getpurchaseList()
    },
    getpurchaseNoLike () {
      this.getpurchaseQueryInfo.query = ''
      this.getpurchaseList()
    }
  }
}
</script>

<style lang="less" scoped>
  /deep/.el-form-item__content {
    float: left;
  }
  .el-pagination{
    margin-top: 15px;
  }
  ul li{
    list-style: none;
    width: 400px;
    height: 40px;
    line-height: 40px;
  }
</style>
