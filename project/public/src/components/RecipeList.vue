<template>
	<div> <p> Recipe : </p>
		<p>Name of dish: {{recipe.name}}</p> <p>Serving Size: {{recipe.serving}} </p> <p> Calories: {{recipe.calorie}}
		</p></div>
</template>


<script>
export default {
	name: "recipe-list-summary",
	props:{
		event: Object
	}
};
</script>