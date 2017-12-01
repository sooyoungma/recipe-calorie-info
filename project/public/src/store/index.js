"use strict";
import Vue from 'vue';
import Vuex from 'vuex';
import api from '../api/recipes.js'

Vue.use(Vuex);

const store = new Vuex.Store({
	strict: true,
	state: {
		recipes: [],
	},
	mutations: {
		createRecipe: function(state, payload){
			state.recipes.push(payload);
		},
		loadRecipes: function(state, payload){
			Vue.set(state, 'recipes', payload.data);
		},
		loadVotes: function(state, payload){
			Vue.set(payload.obj, 'votes', payload.data);
		},
		editRecipe: function(state, payload){
			Object.assign(payload.obj, payload.data);
		},
		createVote: function(state, payload){
			payload.obj.votes.push(payload.data);
		},
		editVote: function(state, payload){
			Object.assign(payload.obj, payload.data);
		},
		deleteRecipe: function(state, payload){
			for (let idx = 0; idx < state.recipes.length; idx++){
				if (state.recipes[idx].id === payload.target.id){
					state.recipes.splice(idx, 1);
					return;
				}
			}
		}
	},
	actions: {
		createRecipe: function(context, payload){
			return new Promise(function(resolve, reject){
				api.createRecipe(payload.data).then(function({request,data}){
					context.commit("createRecipe", data);
					resolve();
				}).catch(function(){
					reject();
				});
			});
			
		},
		editRecipe: function(context, payload){
			return new Promise(function(resolve, reject){
				api.editRecipe(payload.recipe.id, payload.data).then(function({request, data}){
					context.commit("editRecipe", {
						obj: payload.recipe,
						data: data
					});
					resolve();
				}).catch(function(){
					reject();
				});
			});
		},
		deleteRecipe: function(context, payload){
			
			return new Promise(function(resolve, reject){
				api.deleteRecipe(payload.recipe.id).then(function(){
					context.commit("deleteRecipe", {
						target: payload.recipe
					});
				}).catch(function(){
					reject();
				});
			});
		},
		createVote: function(context, payload){
			return new Promise(function(resolve, reject){
				api.createVote(payload.recipe.id, payload.data).then(function({request, data}){
					context.commit("createVote", {
						obj: payload.recipe,
						data: data
					});
					resolve(data);
				}).catch(function(){
					reject();
				});
			});	
		},
		editVote: function(context, payload){
			return new Promise(function(resolve, reject){	
				api.editVote(payload.vote.id, payload.data).then(function({request, data}){
					context.commit("editVote", {
						obj: payload.vote,
						data: data
					});
					resolve(data);
				}).catch(function(){
					reject();
				});
			});	
		},
		loadRecipes: function(context){
			return new Promise(function(resolve, reject){			
				api.getRecipes().then(function({data,request}){
					context.commit("loadRecipes", {
						"data": data
					});
					resolve(data);
				}).catch(function(){
					reject();
				});
			});
		},
		loadVotes: function(context, payload){
			return new Promise(function(resolve, reject){
				var votes = api.getRecipeVotes(payload.recipe.id);
				votes.then(function({data, request}){
					context.commit("loadVotes", {
						"obj": payload.recipe,
						"data": data
					});
					resolve(data);
				}).catch(function(){
					reject();
				});
			});	
		}
	},
	getters: {
		getRecipes: function(state, getters){
			return state.recipes;
		},
		getRecipe: function(state, getters){
			return function(recipeId){
				var recipes = state.recipes;
				return recipes.find(function(element){
					if (element.id === recipeId){
						return element;
					}
				})
			}
		},
		getVote: function(state, getters){
			return function(recipeId, voteId){
				var recipe = getters.getRecipe(recipeId);
				if (recipe){
					return recipe.votes.find(function(element){
						if (element.id === voteId){
							return element;
						}
					});
				}
			}
		},
		getVotes: function(state, getters){
			return function(recipeId){
				var recipe = getters.getRecipe(recipeId);
				if (recipe){
					return recipe.votes
				}
			}
		},
	}
});

export default store;