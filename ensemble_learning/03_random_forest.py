#
#   RANDOM FOREST
#   Sample Code
#   Author : Gilbert M. Oca
#
#   Description:
#   This code demonstrates how random forest
#   can be applied to the famous iris data set.
#   (see FOOTNOTES).

# Let's load the iris data set and save it on a
# variable called iris_df. Here "df" means
# dataframe.
from sklearn.datasets import load_iris
iris_df = load_iris(as_frame=True)

# Let's create a subset of training data and
# a subset of test data from iris_df.
# If test_size is not specified, the default is 0.25.
# This means that 25 % of the data becomes test data
# and the remaining 75 % will be the training data.
from sklearn.model_selection import train_test_split
X = iris_df.data.values
# categorical target names are assigned 0, 1, and 2
# for efficient processing
# 0 -> setosa
# 1 -> versicolor
# 2 -> virginica
# Here, random_state is set to 42. In case the algorithm
# uses random or pseudorandom numbers, we will have the same
# sequence of random numbers. This makes my result replicable
# by other researchers.
y = iris_df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Let's create a Random Forest object that will be trained
# using our training data.
# n_estimators=600 means that we will train the classifier
#      with 600 trees
# max_leaf_nodes=16 means we will stop the training when 16 leaf
#      nodes are reached. Otherwise, if we don't specify it,
#      the object will continue to generate leaf nodes and split nodes.
#      And this will result to overfitting.
# n_jobs=-1 means the algorithm will use all the available cores or CPU's
#      during the training
from sklearn.ensemble import RandomForestClassifier
rnd_clf_obj = RandomForestClassifier(n_estimators=600,
                                     max_leaf_nodes=16,
                                     n_jobs=-1,
                                     random_state=42)
rnd_clf_obj.fit(X_train, y_train)

# Now that we have trained our RandomForest Classifier object
# we can now test its ability to predict.
# Let's print the first instance in our test data set:
print("=========")
print("first instance in our test data set:")
print(f"X_test features = {X_test[0]}")
print(f"y_test species  = {y_test[73]}")
# Let's print the species predicted by random classifier object:
print("=========")
y_predict = rnd_clf_obj.predict(X_test[0].reshape(1,-1))
print(f"predicted species  = {y_predict}")
# awesome! the model predicted the same value of species


# Let's now determine which feature (e.g. petal length,
# petal width, sepal length, sepal width) is the most statistically
# significant. In other words, which feature is the most
# important in the sample classification. Such relative importance
# is measured by the score presented in the code below.
# See footnotes for the zip() function.
print("=========")
for score, feature_name in zip(rnd_clf_obj.feature_importances_,
                               iris_df.data.columns):
    print(feature_name, "\t", round(score,3))
# Based on the results, petal length and petal width are
# the most important features




## =============================================
## FOOTNOTES

# Iris data set contains 150 samples of the
# flower Iris. The samples are divided into
# three species: Setosa, Virginica, and Versicolor.
# The data set has four features:
# 1) petal length
# 2) petal width
# 3) sepal length
# 4) sepal width

# With random forest, we can predict whether
# a sample is Setosa, Virginica, or Versicolor.
# We can also use Random Forest to determine
# which feature is the most statistically
# significant classifier.

# zip() function is used to combine dictionaries
# where corresponding elements from the inputs
# are paired as tuples.