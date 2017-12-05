<template>
	<form v-on:submit.prevent="editEven($event, name, serving, calorie)">
		<label> Name of Dish:
			<input type="text" name="name" v-model="name">
		</label>
		<label>	Serving Size:
			<input type="text" name="serving" v-model="serving">
		</label>
		<label> Calorie Count:
			<input type="text" name="calorie" v-model="calorie">
		</label>
			
		<el-button type="submit">Edit Recipe</el-button>
			
	</form>
</template>


<script>
export default {
	name: 'edit-recipe',
	props:{
		recipe: Object
	},
	data: function(){
		return {
			name: this.recipe.name,
			serving: this.recipe.serving,
			calories: this.recipe.calories
		};
	},
	methods: {
		editRecipe: function(event, name, serving, calorie){
			this.$store.dispatch("editRecipe", {
				recipe: this.recipe,
				data: {
					name: name,
					serving: serving,
					calories: calories
				}

			});
			this.$emit("editSubmitted");
			
		}
	}
};
</script>