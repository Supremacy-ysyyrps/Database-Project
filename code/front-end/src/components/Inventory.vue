<template>
    <div>
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>库存信息管理</el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <!-- 卡片视图区域:搜索部分 -->
      <el-form v-model="getinventoryQueryInfo">
        <el-row :gutter="20">
          <el-col :span="10">
            <el-form-item label="商品编号：">
              <el-input placeholder="请输入商品编号" style="width: 400px" v-model="getinventoryQueryInfo.query"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item style="margin-left: 100px">
              <el-button type="primary" icon="el-icon-search" @click="getinventoryById_query(getinventoryQueryInfo.query)">查询</el-button>
              <el-button type="danger" icon="el-icon-refresh" @click="getinventoryNoLike">重置</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <el-dialog
      title="查询商品库存信息"
      :visible.sync="queryinventoryDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>库存信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>查询商品库存信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 商品库存信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="商品编号：">
              <el-input style="width: 800px" v-model="inventoryById_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品当前库存：">
              <el-input style="width: 800px" v-model="inventoryById_query[1]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品最大库存：">
              <el-input style="width: 800px" v-model="inventoryById_query[2]" disabled></el-input>
            </el-form-item>
            <el-form-item label="商品最小库存：">
              <el-input style="width: 800px" v-model="inventoryById_query[3]" disabled></el-input>
            </el-form-item>

          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="queryinventoryDialogVisible = false">关 闭</el-button>
      </span>
    </el-dialog>

      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <!-- 卡片视图区域:列表部分 -->
      <el-table
        :data="inventoryList"
        border
        style="width: 100%">
        <el-table-column
          prop="P_ID"
          label="商品编号"
          align="center"
          width="150px">
          <template slot-scope="inventoryList">
          <p v-text="inventoryList.row[0]"></p>
        </template>
        </el-table-column>
        <el-table-column
          prop="I_CurStock"
          label="商品当前库存"
          align="center">
          <template slot-scope="inventoryList">
          <p v-text="inventoryList.row[1]"></p>
        </template>
        </el-table-column>
        <el-table-column
          prop="I_MaxStock"
          label="商品最大库存"
          align="center">
          <template slot-scope="inventoryList">
          <p v-text="inventoryList.row[2]"></p>
        </template>
        </el-table-column>
        <el-table-column
          prop="I_MinStock"
          label="商品最小库存"
          align="center">
          <template slot-scope="inventoryList">
          <p v-text="inventoryList.row[3]"></p>
        </template>
        </el-table-column>
      </el-table>

      <!-- 添加库存信息对话框 -->
      <el-dialog
        title="新增商品库存信息"
        :visible.sync="addinventoryDialogVisible"
        width="65%">
        <!-- 内容的主体区域 -->
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/home' }">
            <i class="el-icon-s-home"></i>首页
          </el-breadcrumb-item>
          <el-breadcrumb-item>库存信息管理</el-breadcrumb-item>
          <el-breadcrumb-item><b>新增库存信息</b></el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 设置分割线 -->
        <el-divider></el-divider>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <i class="el-icon-document"></i>
            <span> 库存信息</span>
          </div>
          <!-- 表单信息 -->
          <div style="margin-left: 3%">
            <el-form :model="addinventoryForm">
              <el-form-item label="商品编号：" required="true">
                <el-input style="width: 800px" v-model="addinventoryForm.P_ID"></el-input>
              </el-form-item>
              <el-form-item label="商品当前库存：" required="true">
                <el-input style="width: 800px" v-model="addinventoryForm.I_CurStock"></el-input>
              </el-form-item>
              <el-form-item label="商品最大库存：" required="true">
                <el-input style="width: 800px" v-model="addinventoryForm.I_MaxStock"></el-input>
              </el-form-item>
              <el-form-item label="商品最小库存：" required="true">
                <el-input style="width: 800px" v-model="addinventoryForm.I_MinStock"></el-input>
              </el-form-item>
              
            </el-form>
          </div>
        </el-card>
        <!-- 内容的底部区域 -->
        <span slot="footer" class="dialog-footer">
          <el-button @click="addinventoryDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="addinventory()">提 交</el-button>
        </span>
      </el-dialog>
    </div>
  </template>
  
  <script>
    import axios from 'axios';

  export default {
    name: 'inventory',
    data () {
      return {
        addinventoryForm: {
          P_ID: '',
          I_CurStock:'',
          I_MaxStock: '',
          I_MinStock: ''
        },
        getinventoryQueryInfo: {
          query: '',
          pageSize: 5,
          pageNum: 1
        },
        getinventoryByIdInfo: {
          P_ID: ''
        },
        updateinventoryInfo: {
          P_ID: '',
          I_MaxStock: '',
          I_MinStock: ''
        },
        deleteinventoryByIdInfo: {
          P_ID: ''
        },
        inventoryById: {},
        inventoryById_query: {},
        total: 0,
        inventoryList: [],
        // 控制添加对话框显示与隐藏
        addinventoryDialogVisible: false,
        // 控制查询对话框显示与隐藏
        queryinventoryDialogVisible: false
      }
    },
    created () {
      this.getinventoryList()
    },
    methods: {


    getinventoryList() {
      // 发送请求
      axios.get('http://8.134.218.23:8888/inventory/get_all_inventory')
        .then(response => {
          // 获取响应数据
          let result = response.data;
          if (result.error === false) {
            if (result.result.length === 0) {
              return this.$message.warning('获取库存信息列表失败!');
            } else {
              // 获取库存信息列表成功
              this.inventoryList = result.result;
              this.total = result.total || 0;
              this.pageNum = result.pageNum; // 确保这里是正确的页码值
              this.pageSize = result.pageSize;

              // 如果 totalCount 为 0，你可以选择显示错误消息
              if (result.totalCount === 0) {
                return this.$message.error(result.message);
              }
            }
          } else {
            this.$message.error(result.message);
          }
        })
        .catch(error => {
          this.$message.error('获取库存信息列表失败!');
        });
    },


    getinventoryById_query(P_ID) {
      // 重置状态
      this.queryinventoryDialogVisible = false;
      this.inventoryById_query = {};

      // 发起 GET 请求
      axios.get('http://8.134.218.23:8888/inventory/get_by_p_id_inventory', {
        params: { P_ID: P_ID }
      })
        .then(response => {
          console.log('Response from server:', response.data);
          let result = response.data;
          if (result.result && result.result.length > 0) {
            this.queryinventoryDialogVisible = true;
            this.inventoryById_query = result.result[0];
          } else {
            this.$message.error(result.message);
          }
        })
        .catch(error => {
          console.error('获取库存信息时出现错误:', error);
          this.$message.error('获取库存信息失败!');
        });
    },


      handleSizeChange (newSize) {
        this.getinventoryQueryInfo.pageSize = newSize
        this.getinventoryList()
      },
      handleCurrentChange (newSize) {
        this.getinventoryQueryInfo.pageNum = newSize
        this.getinventoryList()
      },
      getinventoryByLike (newQuery) {
        this.query = newQuery
        this.getinventoryList()
      },
      getinventoryNoLike () {
        this.getinventoryQueryInfo.query = ''
        this.getinventoryList()
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
  