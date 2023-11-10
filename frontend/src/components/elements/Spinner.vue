<template>
    <span class="loader"></span>
</template>
<script>
</script>
<style>
.loader {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: inline-block;
  position: relative;
  background: linear-gradient(0deg, transparent 0%, rgb(117, 117, 207) 100%);
  box-sizing: border-box;
  animation: rotation .3s linear infinite;
}
.loader::after {
  content: '';  
  box-sizing: border-box;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 96px;
  height: 96px;
  border-radius: 50%;
  background: rgb(20, 20, 20);
}
@keyframes rotation {
  0% { transform: rotate(0deg) }
  100% { transform: rotate(360deg)}
} 
</style>