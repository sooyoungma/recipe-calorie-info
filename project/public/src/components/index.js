import Vue from 'vue';

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

function register(component){
	Vue.component(component.name, component);
};

import DefaultNavBar from './DefaultNavBar.vue';
register(DefaultNavBar);

import RecipeCollection from './RecipeCollection.vue';
register(RecipeCollection);

import RecipeSummary from './RecipeSummary.vue';
register(RecipeSummary);

import RecipeDetail from './RecipeDetail.vue';
register(RecipeDetail);

import CreateNutrition from './CreateNutrition.vue';
register(CreateNutrition);

import EditRecipe from './EditRecipe.vue';
register(EditRecipe);

// import AttendeeList from './AttendeeList.vue';
// register(AttendeeList);

// import AttendeeDetail from './AttendeeDetail.vue';
// register(AttendeeDetail);

// import CreateAttendee from './CreateAttendee.vue';
// register(CreateAttendee);

// import EditAttendee from './EditAttendee.vue';
// register(EditAttendee);