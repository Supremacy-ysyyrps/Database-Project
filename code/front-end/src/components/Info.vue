<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>查看个人身份</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <i class="el-icon-date"></i>
        <span> 个人身份</span>
      </div>
      <div style="margin-top: 25px; width: 300px; float: left; margin-left: 10%">
        <img src="../assets/user.jpg" />
      </div>
      <div class="info">
        <el-table :data="nowRole" border style="width: 400px">
          <el-table-column prop="role" label="身 份" align="center" width="399px"></el-table-column>
        </el-table>
      </div>
    </el-card>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  name: 'Info',
  data() {
    return {
      queryInfo: {
        aname: sessionStorage.getItem('AdminName'),
        apass: sessionStorage.getItem('AdminPassword'),
      },
      nowRole: [], // 新增 nowRole 数据项
      show: false,
    };
  },
  created() {
    this.getAdminInfos();
  },
  methods: {
    getAdminInfos() {
      this.$http.get('http://8.134.218.23:8888/now_role').then((response) => {
        let result = response.data;
        this.nowRole = [{ role: result.message }]; // 将获取的角色信息赋值给 nowRole
      });
    },
  },
};
</script>

<style lang="less" scoped>
  .info {
    width: 500px;
    height: 300px;
    float: left;
    margin-left: 8%;
    margin-top: 10%;
  }
  img {
    background-color: #fff;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    width: 300px;
    height: 300px;
  }
</style>
