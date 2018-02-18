<template>
	<el-menu
		v-model="defaultActive"
		:router="!!$router"
		mode="vertical"
	>
		<el-menu-item index="/">Recipes</el-menu-item>
		<el-menu-item index="/tracking-summary">Track Your Macros</el-menu-item>
		<el-menu-item index="/create-nutrition">Enter Nutrition Info</el-menu-item>

	</el-menu>
</template>



<script>
export default {
	name: "default-navbar",
	data: function(){ 
		return {
			defaultActive: null
		};
	},
	watch: {
		"$route": function(newRoute, oldRoute){
			this.$set(this, "defaultActive", newRoute.path)
		}
	}
};
</script>