import Vue from 'vue';
import VueRouter from 'vue-router';

import DataStore from '../store/index.js';

Vue.use(VueRouter);

const router = new VueRouter({
	routes: [
		{
			name: "recipes",
			path: "/",
			components: {
				"header": {"template": '<h2 class="align-center">Recipe Information</h2>'},
				"aside": {"template": "<default-navbar></default-navbar>"},
				"main": {"template": "<recipe-collection></recipe-collection>"}
			},
			beforeEnter: function(to, from, next){
				if (DataStore.getters.getRecipes.length){
					next();
				} else {	
					DataStore.dispatch('loadRecipes').then(function(){
						next();
					});
				}
			}
		},
		{
			name: "create-recipe",
			path: "/create-recipe",
			components: {
				"header": {"template": '<h2 class="align-center">Recipe Information</h2>'},
				"aside": {"template": "<default-navbar></default-navbar>"},
				"main": {"template": "<create-recipe></create-recipe>"}
			}
		},
		{
			name: "profile",
			path: "/profile",
			components: {
				"header": { "template": '<h2 class="align-center">Recipe Information</h2>'},
				"aside": { "template": "<default-navbar></default-navbar>"},
				"main": { "template": "<p>Placeholder</p>" }
			}
		},
		{
			name: "recipe-detail",
			path: '/recipes/:id',
			name: 'recipe',
			components: 
			{
				"header": { "template": '<h2 class="align-center">Recipe Information</h2>'},
				"aside": { "template": "<default-navbar></default-navbar>"},
				"main": { "template": "<recipe-detail></recipe-detail>" }
			},
			props: true,
			beforeEnter: function(to, from, next){
				recipe = DataStore.getters.getRecipe(parseInt(to.params.id));
				if (recipe){
					to.params.recipe = recipe;
					if (!Object.hasOwnProperty.call(recipe, "votes")){
						DataStore.dispatch("loadVotes", {
							recipe: recipe
						}).then(function(){
							next();
						});
					} else {
						next();
					}
				} else {
					console.log("error");
					// next({name: '404'});
				}
			}
		},
		{
			path: '/error',
			name: '404',
			components: {
				"main": { "template": '<p>Not Found</p>' }
			}
		}
	]
});


export default router;