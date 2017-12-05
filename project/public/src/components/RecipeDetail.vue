<template>
	<div>
		<transition-group name="component-fade" mode="in-out">
			<div v-bind:key="recipe.id">
				<p>Name: {{recipe.name}}</p> 
				<p>Serving: {{recipe.serving}}</p>
				<p>Calories: {{recipe.calories}}</p>
			</div>
			
			<edit-recipe 
				v-if="mode.edit" 
				v-bind:recipe="recipe" 
				v-bind:key="recipe.id"
				v-on:editSubmitted="mode.edit = false"
			>
			</edit-recipe>
		</transition-group>
		
		<el-button-group>
			<el-button 
				active
				size="xs"
				v-bind:key="recipe.id"
				v-on:click="mode.edit = !mode.edit" 
			>
				{{ editMode }}
			</el-button>
			
			<el-button 
				type="danger"
				size="xs" 
				v-bind:key="recipe.id"
				v-on:click="deleteRecipe"
			>
				Delete
			</el-button>
		</el-button-group>

		<transition-group name="component-fade" mode="in-out">
			<create-vote 
				v-if="mode.detail"
				v-bind:recipe="recipe"
				v-bind:key="recipe.id"
			>
			</create-vote>

			<ul 
				v-bind:recipe="recipe"
				v-bind:key="recipe.id"
			>
				<li 
					is="vote-detail"
					v-for="vote in recipe.votes"
					v-bind:vote="vote"
					v-bind:key="vote.id"
				></li>
			
			</ul>
		
		</transition-group> 
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
				edit: false,
				votes: false,
			}
		}
	},
	methods: {
		deleteRecipe: function(event){
			this.$store.dispatch("deleteRecipe", {
				recipe: this.recipe
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