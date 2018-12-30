import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it
data = fetch_movielens(min_rating=4.0)

#
print(repr(data['train']))
print(repr(data['test']))

#create model  measures the difference of the model prediction and desired output
#We want to minimise it during training so that our model gets more accurate over time 
model = LightFM(loss='warp')
#Warp create receommendation fr each user  by looking existing user rating pairs and predicting ranking for each 
#Uses stochastic Gradient Descent to improve the prediction
#It is Hybrid system

#train the model
model.fit(data['train'],epochs=30,num_threads=2)



def sample_recommendation(model,data,user_ids):

	#number of users and movies in training data
	n_users,n_items =data['train'].shape


	#generate recommendation for each user we input
	for user_id in user_ids:

		#movies they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#movies our model predicts they will like
		#arange method of numpy gives the number from 0 till number of items
		scores = model.predict(user_id,np.arange(n_items))

		#rank them in order of most liked to least
		top_items = data['item_labels'][np.argsort(-scores)]

		print("User %s" %user_id)
		print("		Known positives:")

		for x in known_positives[:3]:
			print("			  %s" % x)

		print("		Recommended:")

		for x in top_items[:3]:
			print("			%s" % x)

sample_recommendation(model,data,[3,25,450])		