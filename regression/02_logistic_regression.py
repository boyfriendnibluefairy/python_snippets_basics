## How to implement logistic regression in python
## using the famous iris data set


## save the iris data as a data frame
from sklearn.datasets import load_iris
iris_data = load_iris(as_frame=True)

## print contents of iris data
# print(list(iris_data))
# print(iris_data.data.head(3))

## by printing the ff info, we know that each record
## has assigned target variable which correspends to
## 0 -> "setosa"
## 1 -> "versicolor"
## 2 -> "virginica"
## by printing iris_data.target.head(200)
## you'll know that the data are not shuffled;
## they are arranged from 0's, 1's, 2's
# print(iris_data.target.head(200))
# print("=========")
# print(iris_data.target_names)

## from the entire data set we will just separate a subset
## that will serve as the training data set
from sklearn.linear_model import LogisticRegression

## the ff object split arrays or matrices into
## random train and test subsets
## if train_size is not set, size defaults to 25 %
from sklearn.model_selection import train_test_split

## let's focus on the column data about petal width
# print(iris_data.data.head(3))
X = iris_data.data[["petal width (cm)"]].values
# print(iris_data.target_names)
# print("=========")
# print(iris_data.target)

## replace integer with their species name counter part
## and then create a boolean matrix that tells us that
## certain records refer to virginica data
y = iris_data.target_names[iris_data.target] == "virginica"

## Let's now create a training data set and a test data set
## with y containing True's and False's
## random_state = 42 so that you can replicate my results
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)

## We can now train a logistic regression object based on our
## training data set
log_reg_obj = LogisticRegression(random_state=42)
log_reg_obj.fit(X_train, y_train)


## Let's now test our log_reg_obj

## Create a vector of X_new
## see linspace at the foot note
## create array of 1000 data points inside 0.0 to 3.0 range
import numpy as np
## convert array into column vector
## col=1 means you reshape the array in such a way it must have
## 1 column.
## row=-1 means that you let numpy determine the number of rows
## based on the number of columns
X_new = np.linspace(0,3,1000).reshape(-1,1)

## The awesome thing about log_reg_obj is that it has
## predict_proba() function that assigns probability to each X_new values
y_proba = log_reg_obj.predict_proba(X_new)
#print(y_proba)

## generate a decision boundary, see footnotes
## first, create an array of values from X_new that has
## probabilities greater than 50 %
## after that, get the first instance of such array and
## that will be your decision boundary, depcited by [0,0] in the code.
## this is just a single point which results to a vertical line
## because we only have one feature under study.
## If you have two features predciting the probabilities
## you'll have a line with a slope
decision_boundary = X_new[y_proba[:, 1] >= 0.5][0,0]
#print(decision_boundary)

## page 196
import matplotlib.pyplot as plt
plt.plot(X_new, y_proba[:, 0], "m--", linewidth=2, label="Not Iris virginica proba")
plt.plot(X_new, y_proba[:, 1], "b-", linewidth=2, label="Iris virginica proba")
plt.plot([decision_boundary, decision_boundary], [0, 1], "k:", linewidth=2, label="Decision boundary")
plt.grid()
# plt.xlabel('Petal width (cm)', fontsize=16)
# plt.ylabel('Probability', fontsize=16)
plt.xlabel('Petal width (cm)')
plt.ylabel('Probability')
plt.title(label="Iris data set estimated probabilities and decision boundary")

y_test2 = log_reg_obj.predict(X_test)
X_pass = X_test[y_test2[:] >= 0.5]
y_pass = y_test2[y_test2[:] >= 0.5]
X_fail = X_test[y_test2[:] < 0.5]
y_fail = y_test2[y_test2[:] < 0.5]
plt.scatter(X_pass,y_pass, marker="^", c="b")
plt.scatter(X_fail,y_fail, marker="v", c="m")

plt.show()



## ======================================================
## FOOTNOTES:

## The NumPy linspace function creates sequences of evenly spaced
# values within a defined interval. Essentially, you specify a
# starting point and an ending point of an interval, and then specify
# the total number of breakpoints you want within that interval

## In Logistic Regression, Decision Boundary is a linear line,
# which separates class A and class B.

# matplotlib import error in Apple Silicon M2
## pip3 install matplotlib   --compile --force-reinstall


