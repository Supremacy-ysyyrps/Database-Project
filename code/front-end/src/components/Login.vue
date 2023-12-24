<template>
  <div class="login-container">
    <img src="../assets/login.jpg" style="width: 100%; height: 100%" />
    <div class="login_box">
      <!-- 头像区域
      <div class="avatar_box">
        <img src="../assets/超市4.jpg" />
      </div> -->
      <!-- 表单区域 -->
      <el-form
        ref="loginFormRef"
        :model="loginForm"
        :rules="loginFormRules"
        label-width="0px"
        class="login_form"
      >
        <!-- 角色选择区域 -->
        <div class="fixed-message">昊鸣连锁超市</div>
        <el-form-item prop="role">
          <el-select v-model="loginForm.role" placeholder="请选择角色">
            <el-option label="管理员" value="manager"></el-option>
            <el-option label="进货员" value="buyer"></el-option>
            <el-option label="售货员" value="seller"></el-option>
          </el-select>
        </el-form-item>
        <!-- 用户名区域 -->
        <el-form-item prop="username">
          <el-input
            type="text"
            v-model="loginForm.username"
            prefix-icon="el-icon-user"
            placeholder="请输入登录账号"
          ></el-input>
        </el-form-item>
        <!-- 密码区域 -->
        <el-form-item prop="password">
          <el-input
            type="password"
            v-model="loginForm.password"
            prefix-icon="el-icon-lock"
            placeholder="请输入登录密码"
          ></el-input>
        </el-form-item>
        <!-- 按钮区域 -->
        <el-form-item class="btns">
          <el-button type="primary" @click="login()">登录</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'Login',
    data() {
      return {
        loginForm: {
          title: '',
          role: '',
          username: '',
          password: ''
        },
        loginFormRules: {
          title:[{required: false, message: '昊鸣连锁超市', trigger: 'blur' }],
          role: [{ required: true, message: '请选择角色', trigger: 'change' }],
          username: [
            { required: true, message: '请输入登录账号', trigger: 'blur' },
            { min: 5, max: 12, message: '长度在 5 到 12 个字符', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请输入登录密码', trigger: 'blur' },
            { min: 5, max: 12, message: '长度在 6 到 12 个字符', trigger: 'blur' }
          ]
        }
      };
    },
  methods: {
    resetLoginForm() {
      this.$refs.loginFormRef.resetFields();
    },
    login() {
      this.$refs.loginFormRef.validate((valid) => {
        if (!valid) return;

        // 发送登录请求，处理逻辑
        const requestData = {
          role: this.loginForm.role,
          username: this.loginForm.username,
          password: this.loginForm.password,
        };

        axios.post('http://8.134.218.23:8888/role', requestData)
          .then(response => {
            // 处理登录成功逻辑
            const result = response.data;
            if (result.error) {
              this.$message.error(result.message);
            } else {
              // 示例：成功后跳转路由
              this.$router.push('/Home');
              this.$message.success('登录成功！');
            }
          })
          .catch(error => {
            // 处理登录失败逻辑
            console.error('登录请求出错:', error);
            this.$message.error('登录失败');
          });
      });
    }
  }
};
</script>

<style lang="less" scoped>
.login-container {
  background-color: #373d41;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  box-shadow: 0 0 10px #ddd;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.fixed-message {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
  text-align: center;
}

.btns {
  display: flex;
  justify-content: flex-end;
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>