<template>
	<div>
	
		<select v-model="restaurant" multiple>
		  <option>McDonalds</option>
		  <option>Burger King</option>
		  <option>Popeyes</option>
		  <option>Wendys</option>

		</select>
		<br>
		<span>Selected: {{ selected }}</span>
	</div>
</template>


<script>
export default {
	name: "tracking-summary",
	props:{
		recipe: Object
	}
};

	// computed: {
	// 	}
	// },
</script>