<template>
	<form v-on:submit.prevent="editRecipe($event, name, serving, calorie)">
		<label> Name of Dish:
			<input type="text" name="name" v-model="name">
		</label>
		<label>	Serving Size:
			<input type="text" name="serving" v-model="serving">
		</label>
		<label>	calorie count:
			<input type="text" name="calorie" v-model="calorie">
		</label>		
			<button type="submit">Edit Recipe</button>
			
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
			calorie: this.recipe.calorie
		};
	},
	methods: {
		editRecipe: function(event, name, serving, calorie){
			this.$store.dispatch("editRecipe", {
				event: this.event,
				data: {
					name: name,
					serving: serving,
					calorie: calorie
				}
			});
			
		}
	}
};
</script>