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
				"header": {"template": '<h2 class="align-center">Recipe Info</h2>'},
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
				"header": {"template": '<h2 class="align-center">Recipe Info</h2>'},
				"aside": {"template": "<default-navbar></default-navbar>"},
				"main": {"template": "<create-recipe></create-recipe>"}
			}
		},
		{
			name: "tracking-summary",
			path: '/tracking-summary',
			components: {
				"header": { "template": '<h2 class="align-center">Recipe Info</h2>'},
				"aside": { "template": "<default-navbar></default-navbar>"},
				"main": { "template": "<tracking-summary></tracking-summary>" }
			}
		},
		{
			name: "recipe-detail",
			path: '/recipe/:id',
			components: 
			{
				"header": { "template": '<h2>Recipe Info</h2>'},
				"aside": { "template": "<default-navbar></default-navbar>"},
				"main": { 
					"template": '<recipe-detail :recipe="recipe"></recipe-detail>', 
					"props": {
						"recipe": {
							"required": true, 
							"type": Object
						}
					}
				}
			},
			props: { 
				main : function(route){
					recipe = DataStore.getters.getRecipe(parseInt(route.params.id));
					if (recipe){
						return {"recipe": recipe};
					} else {
						console.log("error");
						return {"recipe": {"id": 2}};
					}
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