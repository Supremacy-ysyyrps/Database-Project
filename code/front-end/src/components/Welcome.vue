<template>
    <div>
      <img src="../assets/home.jpg" height="100%" width="100%" />
    </div>
</template>

<script>
export default {
  name: 'Welcome',
  data () {
    return {
      value: new Date()
    }
  }
}
</script>

<style lang="less" scoped>
  .welcome{
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
    font-size: 18px;
  }
  /*修改日历组件的高度*/
  /deep/.el-calendar-table .el-calendar-day {
    height: 75px;
  }
  .is-selected {
    color: #1989FA;
  }
</style>