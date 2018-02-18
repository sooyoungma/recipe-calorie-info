<template>

	<form v-on:submit.prevent="createNutrition($event, name, calories, calories_from_fat, total_fat, saturated_fat, trans_fat, cholesterol, sodium, carbohydrates, fiber, sugar, protein, category)">

		<label> Name of Dish:
			<input type="text" name="name" v-model="name">
		</label>
		<label>	calories:
			<input type="text" name="calories" v-model="calories">
		</label>
		<label>	calories from fat:
			<input type="text" name="calories_from_fat" v-model="calories_from_fat">
		</label>
		<label>	total fat:
			<input type="text" name="total_fat" v-model="total_fat">
		</label>
		<label> saturated fat:
			<input type="text" name="saturated_fat" v-model="saturated_fat">
		</label>
		<label> trans fat:
			<input type="text" name="trans_fat" v-model="trans_fat">
		</label>
		<label> cholesterol:
			<input type="text" name="cholesterol" v-model="cholesterol">
		</label>
		<label> sodium:
			<input type="text" name="sodium" v-model="sodium">
		</label>
		<label> carbohydrates
			<input type="text" name="carbohydrates" v-model="carbohydrates">
		</label>
		<label> fiber:
			<input type="text" name="fiber" v-model="fiber">
		</label>
		<label> sugar:
			<input type="text" name="sugar" v-model="sugar">
		</label>
		<label> protein:
			<input type="text" name="protein" v-model="protein">
		</label>
		<label> category:
			<input type="text" name="category" v-model="category">
		</label>				
			<el-button button type="text">Enter Info of Dish</el-button>
			
	</form>


</template>


<script>
export default {
	name: 'create-nutrition',
	data: function(){
		return {
			name:'',
			calories:'',
			total_fat:'',
			saturated_fat:'',
			trans_fat:'',
			cholesterol:'',
			sodium:'',
			carbohydrates:'',
			fiber:'',
			sugar:'',
			protein:'',
			category:'',			
		};
	},

	methods:{
		createNutrition: function(event, name, calories, calories_from_fat, total_fat, saturated_fat,trans_fat, cholesterol, sodium, carbohydrates,fiber, sugar, protein, category ){
			this.$store.dispatch("createNutrition", {
				data: {
			name: name,
			calories: calories,
			total_fat: total_fat,
			saturated_fat: saturated_fat,
			trans_fat: trans_fat,
			cholesterol: cholesterol,
			sodium: sodium,
			carbohydrates: carbohydrates,
			fiber: fiber,
			sugar: sugar,
			protein: protein,
			category: category,

				}
			});
			this.$set(this, "name", "");
			this.$set(this, "calories", "");
			this.$set(this, "total_fat", "");
			this.$set(this, "saturated_fat", "");
			this.$set(this, "trans_fat", "");
			this.$set(this, "cholesterol", "");
			this.$set(this, "sodium", "");
			this.$set(this, "carbohydrates", "");
			this.$set(this, "fiber", "");	
			this.$set(this, "sugar", "");
			this.$set(this, "protein", "");
			this.$set(this, "category", "");		
		}
	}
}
</script>