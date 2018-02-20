<template>
	<div>
	
		<select v-model="calories">
		  <option>Less than 1,000 calories</option>
		  <option>Less than 900 calories</option>
		  <option>Less than 800 calories</option>
		  <option>Less than 700 calories</option>
		  <option>Less than 600 calories</option>
		  <option>Less than 500 calories</option>
		  <option>Less than 400 calories</option>
		  <option>Less than 300 calories</option>

		</select>
		<br>
		<span>calories: {{ calories }}</span>
	</div>


</template>


<script>
export default {
	name: 'tracking-summary',
	data: function(){
		return {
			name:'',
			calories:0,
			calories_from_fat: 0,
			total_fat: 0,
			saturated_fat: 0,
			trans_fat: '',
			cholesterol: 0,
			sodium: 0,
			carbohydrates: 0,
			fiber: 0,
			sugar: 0,
			protein: 0,
			category: '',
			restaurant: ''
		};
	},
	methods:{
		onSubmit: function(event, name, calories, calories_from_fat, total_fat, saturated_fat,trans_fat, cholesterol, sodium, carbohydrates, fiber, sugar, protein, category, restaurant){
			this.$store.dispatch("", {
				data: {
					origin: origin,
					destination: destination,
					departure_date: departure_date,
					return_date: return_date,
					quantity: quantity,
					type_of_trip: type_of_trip
				}
			});
			this.$set(this, "origin", "");
			this.$set(this, "destination", "");
			this.$set(this, "departure_date", "");
			this.$set(this, "return_date", "");
			this.$set(this, "quantity", "");
			this.$set(this, "type_of_trip", "");
			this.$store.dispatch("createSavedRoute", {
				data: {
					origin: origin,
					destination: destination,
					quantity: quantity,
					type_of_trip: type_of_trip
				}
			});
			this.$set(this, "origin", "");
			this.$set(this, "destination", "");
			this.$set(this, "quantity", "");
			this.$set(this, "type_of_trip", "");

			
		},
		// databaseSave: function(event, origin, destination, quantity, type_of_trip){
		// 	this.$store.dispatch("createSavedRoute", {
		// 		data3: {
		// 			origin: origin,
		// 			destination: destination,
		// 			quantity: quantity,
		// 			type_of_trip: type_of_trip
		// 		}
		// 	});
		// 	this.$set(this, "origin", "");
		// 	this.$set(this, "destination", "");
		// 	this.$set(this, "quantity", "");
		// 	this.$set(this, "type_of_trip", "");
		// }
	}
}
</script>