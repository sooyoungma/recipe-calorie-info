<template>
	<div>
			
			<edit-recipe 
				v-if="mode.edit" 
				v-bind:recipe="recipe" 
				v-bind:key="recipe.id"
				v-on:editSubmitted="mode.edit = false"
			>
			</edit-recipe>
		
			<create-vote
				v-if="mode.detail"
				v-bind:event="recipe"
				v-bind:key="recipe.id"
			>
			</create-vote>

		
	</div>
</template>

<script>
export default {
	name: 'recipe-detail',
	props:{
		recipe: Object
	},
	data: function(){
		return {
			mode: {
				edit: true,
				votes: false,
			}
		}
	},
	methods: {
		deleteRecipe: function(event){
			this.$store.dispatch("deleteRecipe", {
				event: this.event
			});
		}
	},	

	
	computed: {
		editMode: function(){
			return this.mode.edit ? "Hide":"Edit";
		}
	}	
};
</script>