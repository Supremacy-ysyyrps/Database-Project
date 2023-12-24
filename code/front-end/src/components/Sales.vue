<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>销售信息管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:搜索部分 -->
    <el-form v-model="getSalesQueryInfo">
      <el-row :gutter="20">
        <el-col :span="10">
          <el-form-item label="销售编号：">
            <el-input placeholder="请输入销售编号" style="width: 400px" v-model="getSalesQueryInfo.query"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item style="margin-left: 100px">
            <el-button type="primary" icon="el-icon-search" @click="getSalesById_query(getSalesQueryInfo.query)">查询</el-button>
            <el-button type="danger"  icon="el-icon-refresh" @click="getSalesNoLike" >重置</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog
      title="查询销售信息"
      :visible.sync="querySalesDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>销售信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>查询销售信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 销售信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="销售编号：">
              <el-input style="width: 800px" v-model="SalesById_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品编号：">
              <el-input style="width: 800px" v-model="SalesById_query[1]" disabled></el-input>
            </el-form-item>            
            <el-form-item label="销售数量：">
              <el-input style="width: 800px" v-model="SalesById_query[2]" disabled></el-input>
            </el-form-item>            
            <el-form-item label="销售商品单价：">
              <el-input style="width: 800px" v-model="SalesById_query[3]" disabled></el-input>
            </el-form-item>
            <el-form-item label="销售日期：">
              <el-input style="width: 800px" v-model="SalesById_query[4]" disabled></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="querySalesDialogVisible = false">关 闭</el-button>
      </span>
    </el-dialog>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:列表部分 -->
    <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addSalesDialogVisible = true">新增销售信息</el-button>
    <el-table
      :data="salesList"
      border
      style="width: 100%">
      <el-table-column
        prop="SR_ID"
        label="销售编号"
        align="center"
        width="150px">
        <template slot-scope="salesList">
          <p v-text="salesList.row[0]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="P_ID"
        label="商品编号"
        align="center">
        <template slot-scope="salesList">
          <p v-text="salesList.row[1]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="SR_Num"
        label="销售数量"
        align="center">
        <template slot-scope="salesList">
          <p v-text="salesList.row[2]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="SR_UnitPrice"
        label="销售商品单价"
        align="center">
        <template slot-scope="salesList">
          <p v-text="salesList.row[3]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="SR_Date"
        label="销售日期"
        align="center">
        <template slot-scope="salesList">
          <p v-text="salesList.row[4]"></p>
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        width="265px"
        align="center">
        <template slot-scope="salesList">
          <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleteSalesById(salesList.row[0])">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加销售对话框 -->
    <el-dialog
      title="新增销售信息"
      :visible.sync="addSalesDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>销售管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>添加销售信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 销售信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form :model="addSalesForm">
            <el-form-item label="销售编号：" required="true">
              <el-input style="width: 800px" v-model="addSalesForm.SR_ID"></el-input>
            </el-form-item>
            <el-form-item label="商品编号：" required="true">
              <el-input style="width: 800px" v-model="addSalesForm.P_ID"></el-input>
            </el-form-item>
            <el-form-item label="销售数量：" required="true">
              <el-input style="width: 800px" v-model="addSalesForm.SR_Num"></el-input>
            </el-form-item>
            <el-form-item label="销售商品单价：" required="true">
              <el-input style="width: 800px" v-model="addSalesForm.SR_UnitPrice"></el-input>
            </el-form-item>
            <el-form-item label="销售日期：" required="true">
              <el-input style="width: 800px" v-model="addSalesForm.SR_Date"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addSalesDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addSales()">提 交</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';
export default {
  name: 'Sales',
  data () {
    return {
      addSalesForm: {
        SR_ID:'',
        P_ID: '',
        SR_Num: '',
        SR_UnitPrice: '',
        SR_Date: '',
      },
      getSalesQueryInfo: {
        query: '',
        pageSize: 5,
        pageNum: 1
      },
      getSalesByIdInfo: {
        SR_ID: ''
      },
      updateSalesInfo: {
        P_ID: '',
        SR_Num: '',
        SR_UnitPrice: '',
        SR_Date: ''
      },
      deleteSalesByIdInfo: {
        SR_ID: ''
      },
      SalesById: {},
      SalesById_query: {},
      total: 0,
      salesList: [],
      // 控制添加对话框显示与隐藏
      addSalesDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      updateSalesDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      querySalesDialogVisible: false
    }
  },
  created () {
    this.getSalesList()
  },
  methods: {


    addSales() {
      const {
        SR_ID,
        P_ID,
        SR_Num,
        SR_UnitPrice,
        SR_Date
      } = this.addSalesForm;

      if (SR_ID !== '' && P_ID !== '' && SR_Num !== '' &&
        SR_UnitPrice !== '' && SR_Date !== '') {

        const params = new URLSearchParams({
          SR_ID,
          P_ID,
          SR_Num,
          SR_UnitPrice,
          SR_Date
        });

        axios.post('http://8.134.218.23:8888/sales/add_sales?' + params)
          .then(response => {
            let result = response.data;
            if (result.error === false) {
              this.$router.push('/sales');
              this.addSalesDialogVisible = false;
              this.getSalesList();
              this.$message.success(result.message);
            } else {
              this.$message.error(result.message);
            }
          })
          .catch(error => {
            console.error('添加销售信息失败:', error);
            this.$message.error('添加销售信息失败');
          });

      } else {
        alert('输入有误，请重新输入！');
      }
    },


    getSalesList() {
      // 添加loading状态
      this.loading = true;

      // 发送请求
      axios.get('http://8.134.218.23:8888/sales/get_all_sales')
        .then(response => {
          // 关闭loading状态
          this.loading = false;

          // 获取响应数据
          let result = response.data;
          if (result && result.error === false) { // 检查是否有错误
            if (result.result && Array.isArray(result.result)) {
              // 更新响应数据的属性，确保响应性
              this.salesList = result.result || [];
            } else {
              this.$message.warning(result.message);
            }
          } else {
            this.$message.warning(result.message);
          }
        })
        .catch(error => {
          // 关闭loading状态
          this.loading = false;

          // 在请求失败时显示错误消息
          this.$message.error('获取销售列表失败!');
          console.error('获取销售列表失败:', error);
        });
    },


    getSalesById(SR_ID) {
      axios({
        url: 'http://8.134.218.23:8888/sales/get_by_sr_id_sales',
        params: {
          SR_ID: SR_ID
        }
      })
      .then(response => {
        let result = response.data
        if (result.result && result.result.length > 0) {
          this.updateSalesDialogVisible = true
          this.SalesById = result.result[0]
        } else {
          this.$message.error(result.message)
        }
      })
      .catch(error => {
        console.error('获取销售信息时出现错误:', error);
      });
    },


    getSalesById_query(SR_ID) {
      // 重置状态
      this.querySalesDialogVisible = false;
      this.SalesById_query = {};

      // 发起 GET 请求
      axios.get('http://8.134.218.23:8888/sales/get_by_sr_id_sales', {
        params: {
          SR_ID: SR_ID
        }
      })
      .then(response => {
        console.log('Response from server:', response.data);
        let result = response.data;
        if (result.result && result.result.length > 0) {
          this.querySalesDialogVisible = true;
          this.SalesById_query = result.result[0];
        } else {
          this.$message.error(result.message);
        }
      })
      .catch(error => {
        console.error('获取销售信息时出现错误:', error);
        this.$message.error('获取销售信息失败!');
      });
    },


    deleteSalesById(SR_ID) {
      if (confirm('确定要删除吗?')) {
        axios({
          method: 'post',
          url: 'http://8.134.218.23:8888/sales/del_sales',
          params: {
            Type: 'SR_ID',
            ID: SR_ID
          },
        })
        .then(response => {
          let result = response.data;
          console.log(result);
          if (result.error === false) {
            // 输出详细信息，成功
            console.log('删除销售信息结果:', result.message || '未知结果');
            this.$message.success(result.message);  // 输出成功的提示消息

            // 可选：更新其他界面或执行其他操作
            this.getSalesByIdInfo.pageNum = 1;
            this.getSalesList();
          } else {
            // 输出详细错误信息，删除失败
            console.error('删除销售信息失败:', result.message || '未知错误');
            this.$message.error('删除销售信息失败: ' + (result.message || '未知错误'));  // 输出删除失败的提示消息
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
      this.getSalesQueryInfo.pageSize = newSize
      this.getSalesList()
    },
    handleCurrentChange (newSize) {
      this.getSalesQueryInfo.pageNum = newSize
      this.getSalesList()
    },
    getSalesByLike (newQuery) {
      this.query = newQuery
      this.getSalesList()
    },
    getSalesNoLike () {
      this.getSalesQueryInfo.query = ''
      this.getSalesList()
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
    list-style: SR_IDne;
    width: 400px;
    height: 40px;
    line-height: 40px;
  }
</style>
