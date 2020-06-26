#!/usr/bin/env python
# coding: utf-8

# ## Iris Flower Prediction Application using StreamLit

# In[1]:


#importing important libraries
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


# In[2]:


#creating Title of page
st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")


# In[3]:


#creating sidebar
st.sidebar.header('User Input Parameters')


# In[4]:


#input parameters
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


# In[5]:


#converting user input to dataframe
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)
#loading dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target


# In[6]:


#creating model
clf = RandomForestClassifier()
clf.fit(X, Y)
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)
st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)
st.subheader('Prediction Probability')
st.write(prediction_proba)


# In[ ]:




