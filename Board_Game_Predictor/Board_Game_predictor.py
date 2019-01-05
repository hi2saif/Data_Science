
# coding: utf-8

# In[1]:


import sys
import numpy
import pandas
import matplotlib
import seaborn
import scipy
import sklearn

print('Python: {}'.format(sys.version))
print('Numpy: {}'.format(numpy.__version__))
print('Pandas: {}'.format(pandas.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('Seaborn: {}'.format(seaborn.__version__))
print('Scipy: {}'.format(scipy.__version__))
print('Scipy: {}'.format(sklearn.__version__))


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


# In[3]:


games =pd.read_csv("C:\\Users\\bad_engineer\\Desktop\\git\\Data_Science\\games.csv")
#load the data


# In[5]:


print(games.columns)
print(games.shape)


# In[7]:


#make the histogram of all the ratings in the average_rating column
plt.hist(games["average_rating"])
plt.show()
#what is histogram


# In[10]:


#Print the first row of all the games with zero scores
print(games[games["average_rating"]==0].iloc[0])
print()
#Print the first row of all the games with scores greater than 0
print(games[games["average_rating"]>0].iloc[0])

#By Exploring the data we can confirm that we dont need the data which have average rating as 0 
#thast why it becomes important for us to explore the data before applying the concepts of machine learning


# In[14]:


#Remove rows withour user reviews
games = games[games["users_rated"]>0]

#Remove rows with missing values
games = games.dropna(axis=0)
#dropna is the function of pandas
#Make a histogram of all the average ratings
plt.hist(games["average_rating"])
plt.show()


# In[15]:


print(games.columns)


# In[24]:


#make a corelation matrix -->Use seaborn
corrmat = games.corr()
fig = plt.figure(figsize =(12,9))

sns.heatmap(corrmat,vmax= .8,square=True)
plt.show()


# In[26]:


#Data Set Preprocessing
# GEt all the columns from the dataFrame
columns = games.columns.tolist()

#filter the column to remove data we do not want
columns = [c for c in columns if c not in ["bayes_average_rating","average_rating","type","name","id"]]

#store the variable we'll be predicting on
target = "average_rating"


# In[28]:


#Generate trainign and test datasets
from sklearn.model_selection import train_test_split

#Generate the trainign set
train = games.sample(frac=0.8,random_state=1)

#Select anything not in the training set and put it in test
test = games.loc[~games.index.isin(train.index)]

print (train.shape)
print(test.shape)


# In[30]:


#import linear regression model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Initialize the model class
LR = LinearRegression()

#fit the model the training data
LR.fit(train[columns],train[target])


# In[31]:


#Generate Prediction for the test set
prediction =LR.predict(test[columns])

#Compute error between our test prediction and actual values
mean_squared_error(prediction,test[target])


# In[33]:


#import the random forest model
from sklearn.ensemble import RandomForestRegressor

#Initialize the model
RFR = RandomForestRegressor(n_estimators=100,min_samples_leaf=10,random_state=1)

#fit the data
RFR.fit(train[columns],train[target])


# In[34]:


#Predictions
predictions =RFR.predict(test[columns])

#Compute error between our test prediction and actual values
mean_squared_error(predictions,test[target])


# In[35]:


test[columns].iloc[0]


# In[37]:


ratings_LR =LR.predict(test[columns].iloc[0].values.reshape(1,-1))
ratings_RFR =RFR.predict(test[columns].iloc[0].values.reshape(1,-1))

print(ratings_LR)
print(ratings_RFR)


# In[38]:


test[target].iloc[0]

