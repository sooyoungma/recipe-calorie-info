import Vue from 'vue';

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

import DefaultNavBar from './DefaultNavBar.vue';
import RecipeCollection from './RecipeCollection.vue';
import RecipeSummary from './RecipeSummary.vue';
import RecipeDetail from './RecipeDetail.vue';
import CreateRecipe from './CreateRecipe.vue';
import EditRecipe from './EditRecipe.vue';
import TrackMacros from './TrackMacros.vue';



Vue.component(DefaultNavBar.name, DefaultNavBar);
Vue.component(RecipeCollection.name, RecipeCollection);
Vue.component(RecipeSummary.name, RecipeSummary);
Vue.component(RecipeDetail.name, RecipeDetail);
Vue.component(CreateRecipe.name, CreateRecipe);
Vue.component(EditRecipe.name, EditRecipe);
Vue.component(TrackMacros.name, TrackMacros);
