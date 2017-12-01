<template>
	<div>
		<p>Name of Dish: {{recipe.name}}</p> 
		<p>Serving Size: {{recipe.serving}}</p>
		<p>Calorie Count: {{recipe.calorie}}</p>
		<router-link v-bind:to="'/recipe/' + recipe.id">Detail</router-link>
	</div>
</template>


<script>
export default {
	name: "recipe-summary",
	props:{
		recipe: Object
	}
};
</script>