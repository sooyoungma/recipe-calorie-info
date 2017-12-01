<template>

	<form v-on:submit.prevent="createRecipe($event, name, serving, calorie)">
		<label> Name of Dish:
			<input type="text" name="name" v-model="name">
		</label>
		<label>	Serving Size:
			<input type="text" name="serving" v-model="serving">
		</label>
		<label> Calorie Count:
			<input type="text" name="calorie" v-model="calorie">
		</label>
		
			<el-button button type="text">Enter Recipe Info</el-button>
			
	</form>


</template>


<script>
export default {
	name: 'create-recipe',
	data: function(){
		return {
			name:'',
			serving:'',
			calorie:'',
		};
	},

	methods:{
		createRecipe: function(event, name, serving, calorie ){
			this.$store.dispatch("createRecipe", {
				data: {
					name: name,
					serving: serving,
					calorie: calorie,

				}
			});
			this.$set(this, "name", "");
			this.$set(this, "serving", "");
			this.$set(this, "calorie", "");

			
		}
	}
}
</script>