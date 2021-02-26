# Personality-Test-App


GO check out the website at: https://personality-test-app.herokuapp.com/

The result is shown to you by processing your data through an Unsupervised Machine Learning model trained locally with GTX 1650. The data for training the model was taken from Kaggle at BIG-FIVE-PERSONALITY-TEST.

The model was serialized by a python library called "pickle" and then put into the django backend. Each input by the user is passed throught the serialized Model and it returns personality characteristic values which are shown in a React App. 
