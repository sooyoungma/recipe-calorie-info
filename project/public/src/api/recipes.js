import axios from "axios";

axios.defaults.baseURL = '/api/v0/';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const ACTIVITY_TYPES = {
	"LIKE": "L",
	"DISLIKE": "D",
};

export default {
	getRecipes: function(){
		return axios({
			method: 'get',
			url: '/recipes'
		});
	},
	getRecipe: function(recipeId){
		return axios({
			method: 'get',
			url: '/recipes/' + recipeId
		});
	},
	getRecipeVotes: function(recipeId){
		return axios({
			method: 'get',
			url: '/recipes/' + recipeId + '/votes'
		});
	},
	createRecipe: function(data){
		return axios({
			method: 'post',
			url: '/recipes',
			data: data
		});
	},
	editRecipe: function(recipeId, data){
		return axios({
			method: 'put',
			url: '/recipes/' + recipeId,
			data: data
		});
	},
	deleteRecipe: function(recipeId){
		return axios({
			method: 'delete',
			url: '/recipes/' + recipeId
		});
	},
	createVote: function(recipeId, data){
		data.status = STATUSES[data.status];
		return axios({
			method: 'post',
			url: '/recipes/' + recipeId + "/votes",
			data: data
		});
	},
	editVote: function(voteId, data){
		data.status = STATUSES[data.status];
		return axios({
			method: 'put',
			url: '/votes/' + voteId,
			data: data
		});
	}
}