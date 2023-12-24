<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>商品信息管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:搜索部分 -->
    <el-form v-model="getProductQueryInfo">
      <el-row :gutter="20">
        <el-col :span="10">
          <el-form-item label="商品编号：">
            <el-input placeholder="请输入商品编号" style="width: 400px" v-model="getProductQueryInfo.query"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item style="margin-left: 100px">
            <el-button type="primary" icon="el-icon-search" @click="getProductBypid_query(getProductQueryInfo.query)">查询</el-button>
            <el-button type="danger" icon="el-icon-refresh" @click="getProductNoLike">重置</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog
      title="查询商品信息"
      :visible.sync="queryProductDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>商品信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>查询商品信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 商品信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="商品编号：">
              <el-input style="width: 800px" v-model="ProductBypid_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品名称：">
              <el-input style="width: 800px" v-model="ProductBypid_query[1]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品类型：">
              <el-input style="width: 800px" v-model="ProductBypid_query[2]" disabled></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="queryProductDialogVisible = false">关 闭</el-button>
      </span>
    </el-dialog>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:列表部分 -->
    <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addProductDialogVisible = true">新增商品信息</el-button>
  <el-table
  :data="ProductsList"
  border
  style="width: 100%"
  >
  <el-table-column
    prop="P_ID"
    label="商品编号"
    align="center"
    width="150px"
  >
    <template slot-scope="scope">
      <p v-text="scope.row.P_ID"></p>
    </template>
  </el-table-column>
  <el-table-column
    prop="P_Name"
    label="商品名称"
    align="center"
  >
    <template slot-scope="scope">
      <p v-text="scope.row.P_Name"></p>
    </template>
  </el-table-column>
  <el-table-column
    prop="P_Type"
    label="商品类型"
    align="center"
  >
    <template slot-scope="scope">
      <p v-text="scope.row.P_Type"></p>
    </template>
  </el-table-column>

  <el-table-column
    label="操作"
    width="265px"
    align="center"
  >
    <template slot-scope="scope">
      <el-button type="primary" icon="el-icon-view" size="mini" @click="getProductBypid(scope.row.P_ID)">编辑</el-button>
      <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleteProductBypid(scope.row.P_ID)">删除</el-button>
    </template>
  </el-table-column>
  </el-table>

    <!-- 添加商品对话框 -->
    <el-dialog
      title="新增商品信息"
      :visible.sync="addProductDialogVisible"
      width="31%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>商品信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>新增商品</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 商品信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form :model="addProductForm">
            <el-form-item label="商品编号：" required="true">
              <el-input style="width: 400px" v-model="addProductForm.P_ID"></el-input>
            </el-form-item>
            <el-form-item label="商品名称：" required="true">
              <el-input style="width: 400px" v-model="addProductForm.P_Name"></el-input>
            </el-form-item>
            <el-form-item label="商品类型：" required="true">
              <el-input style="width: 400px" v-model="addProductForm.P_Type"></el-input>
            </el-form-item>
          
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addProductDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addProduct()">提 交</el-button>
      </span>
    </el-dialog>
    <!-- 编辑商品对话框 -->
    <el-dialog
      title="编辑商品信息"
      :visible.sync="updateProductDialogVisible"
      width="31%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>商品信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑商品信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 商品信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="商品编号：">
              <el-input style="width: 400px" v-model="ProductBypid.P_ID" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品名称：">
              <el-input style="width: 400px" v-model="ProductBypid.P_Name"></el-input>
            </el-form-item>
            <el-form-item label="商品类型：">
              <el-input style="width: 400px" v-model="ProductBypid.P_Type"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="updateProductDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateProduct()">提 交</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Product',
  data () {
    return {
      addProductForm: {
        P_ID: '',
        P_Name: '',
        P_Type: '',
      },
      getProductQueryInfo: {
        query: '',
        pageSize: 5,
        pageNum: 1
      },
      getProductBypidInfo: {
        P_ID: ''
      },
      updateProductInfo: {
        P_ID: '',
        P_Name: '',
        P_Type: '',
      },
      deleteProductBypidInfo: {
        P_ID: ''
      },
      ProductBypid: {},
      ProductBypid_query: {},
      total: 0,
      ProductsList: [],
      // 控制添加对话框显示与隐藏
      addProductDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      updateProductDialogVisible: false,
      // 控制查询对话框显示与隐藏
      queryProductDialogVisible: false
    }
  },
  created () {
    this.getProductList();
  },
  methods: {

    addProduct() {
      if (this.addProductForm.P_ID !== '' && this.addProductForm.P_Name !== '' && this.addProductForm.P_Type !== '') {
        const data = {
          P_ID: this.addProductForm.P_ID,
          P_Name: this.addProductForm.P_Name,
          P_Type: this.addProductForm.P_Type,
        };

        axios.post('http://8.134.218.23:8888/product/add_product', null, { params: data })
          .then(response => {
            if (response.status === 200) {
              let result = response.data;
              if (result && result.error) {
                this.$message.error(result.message);
              } else {
                this.$router.push('/product');
                this.addProductDialogVisible = false; // Fix the variable name here
                this.getProductList();
                this.$message.success('商品信息添加成功!');
              }
            } else {
              // Handle non-200 status code
              this.$message.error('请求失败，状态码：' + response.status);
            }
          })
          .catch(error => {
            console.error('添加商品时出错:', error);
            this.$message.error('添加商品失败');
          });
      } else {
        alert('输入有误，请重新输入！');
      }
    },


    getProductList() {
      // 发送请求
      axios.get('http://8.134.218.23:8888/product/get_all_product')
        .then(response => {
          let result = response.data;
          if (result.error) {
            return this.$message.warning(result.message);
          } else {
            this.ProductsList = result.result.map(item => {
              return {
                P_ID: item[0],
                P_Name: item[1],
                P_Type: item[2],
              };
            });
          }
        })
        .catch(error => {
          console.error('获取商品列表失败:', error);
          this.$message.error(String(error));
        });
    },

    
    getProductBypid(P_ID) {
      axios.get('http://8.134.218.23:8888/product/get_by_p_id_product', { params: { P_ID: P_ID } })
        .then(response => {
          let result = response.data;
          if (result.error === false && result.result.length > 0) {
            // 确保 result.result 是一个非空数组
            this.updateProductDialogVisible = true;
            this.ProductBypid = result.result[0];  // 使用数组的第一个元素
          } else {
            this.$message.error(result.message);
          }
        })
        .catch(error => {
          console.error('获取商品信息时出现错误:', error);
        });
    },

    getProductBypid_query(P_ID) {
      axios.get('http://8.134.218.23:8888/product/get_by_p_id_product', { params: { P_ID: P_ID } })
        .then(response => {
          console.log('Response from server:', response.data);
          let result = response.data;
          if (result.result && result.result.length > 0) {
            this.queryProductDialogVisible = true;
            this.ProductBypid_query = result.result[0];
          } else {
            this.$message.error(result.message);
          }
        })
        .catch(error => {
          console.error('获取商品信息时出现错误:', error);
        });
    },

    deleteProductBypid(P_ID) {
      if (confirm('确定要删除吗?')) {
        axios.post('http://8.134.218.23:8888/product/del_product', null, { params: { P_ID: P_ID } })
          .then(response => {
            console.log('Response from server:', response.data);
            let result = response.data;
            if (result.error === false && result.message.includes('商品信息删除成功')) {
              this.getProductBypidInfo.pageNum = 1;
              this.getProductList();
              this.$message.success(result.message);
            } else {
              this.$message.error(result.message);
            }
          })
          .catch(error => {
            console.error('删除商品信息失败:', error);
            this.$message.error(result.message);
          });
      }
    },


    updateProduct() {
      const data = {
        p_id: this.ProductBypid[0],
        P_Name: this.ProductBypid.P_Name,
        P_Type: this.ProductBypid.P_Type,
      };

      axios.post('http://8.134.218.23:8888/product/set_product', null, { params: data })
        .then(response => {
          console.log('Response from server:', response.data);
          let result = response.data;

          // 判断是否为成功消息
          if (result.message && result.message.includes('商品信息更新成功！')) {
            this.$router.push('/product');
            this.updateProductDialogVisible = false;
            this.getProductList();
            this.$message.success(result.message);
          } else {
            // 显示后端返回的错误消息
            console.error('商品信息更新失败:', result.message);
            this.$message.error('商品信息更新失败: ' + result.message);
          }
        })
        .catch(error => {
          console.error('编辑商品信息时出现错误:', error);
          this.$message.error('编辑商品信息时出现错误');
        });
    },

    handleSizeChange (newSize) {
      this.getProductQueryInfo.pageSize = newSize
      this.getProductList()
    },
    handleCurrentChange (newSize) {
      this.getProductQueryInfo.pageNum = newSize
      this.getProductList()
    },
    getProductByLike (newQuery) {
      this.query = newQuery
      this.getProductList()
    },
    getProductNoLike () {
      this.getProductQueryInfo.query = ''
      this.getProductList()
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
