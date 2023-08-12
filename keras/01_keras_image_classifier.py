#
#  Neural Networks using Keras Library
#  (with 97 % validation accuracy)
#  A sample implementation of neural networks by
#  applying keras sequential API to MNIST
#  handwritten digits dataset
#
#  Author : Gilbert M. Oca
#

import tensorflow as tf
# print(tf.__version__)
import numpy as np

## Let's use the MNIST handwritten digits image data set.
## By default, it's already divided into 60 000 training data set
## and 10 000 test data set
## Use the last 5000 images of the training data for validation.
## Remember that if we use training data to check the model,
## we can calculate the validation error.
## If we use test data, then we can calculate the generalization error.
digit_images = tf.keras.datasets.mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = digit_images
# print(X_train_full.shape) # (60000, 28, 28)
# print(y_train_full.shape) # (60000,)
# print(X_test.shape)       # (10000, 28, 28)
# print(y_test.shape)       # (10000,)
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]

## Before we begin, let's see the class of the first three instances
## of our test data:
class_names = ["digit 0", "digit 1", "digit 2", "digit 3", "digit 4", "digit 5",
               "digit 6", "digit 7", "digit 8", "digit 9", "digit 10"]
# print(np.array(class_names)[y_test[:3]])
## our first the instances refer to class 7, 2, and 1.
## later, after we have trained our model, we will use
## the model to predict the classes of the first three
## instances of our test data. If the model yields
## exactly [7,2,1], then our model has a high generalization
## accuracy. Of course, that also means we are successful
## in training the model.

## Let's design the neural network architecture
tf.random.set_seed(42)
nn_model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=[28,28]),       # input layer
    tf.keras.layers.Dense(300, activation="relu"), # 1st hidden layer
    tf.keras.layers.Dense(200, activation="relu"), # 2nd hidden layer
    tf.keras.layers.Dense(100, activation="relu"), # 3rd hidden layer
    # units below is 10 because we have 10 classes: 0, 1, 2, ...
    tf.keras.layers.Dense(10, activation="softmax")  # output layer
])

## Let's try to print some details
# print(nn_model.summary())
# tf.keras.utils.plot_model(
#     model = nn_model,
#     to_file="my_model.png"
# )
# print(nn_model.layers)

## During compilation, specify the model's
## loss function, optimizer, and metrics
nn_model.compile(
    loss = "sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

## We can now train the model by simply calling its
## fit() function
history = nn_model.fit(
    X_train,
    y_train,
    epochs=30,
    validation_data=(X_valid,y_valid) # this is optional
)

## Now that we have trained our model. Let's see its
## performance on the test data. Recall that the test data
## was not used in training the model. This means that
## the following code measures how the model generalize to
## test instances.
# print("===========================")
# print("EVALUATION RESULTS:")
# nn_model.evaluate(X_test,y_test)
## note that our validation accuracy is 97 %
## even of we have not yet fine tuned
## the hyperparameters during the training

## We can now use the model to predict the class of...
## let's say the first three instances of our test data
X_pred = X_test[:3]
y_proba = nn_model.predict(X_pred)
y_pred = y_proba.argmax(axis=-1)
print(np.array(class_names)[y_pred])
## output: ['digit 7' 'digit 2' 'digit 1'] ## awesome!!!





## ======================================================
## FOOTNOTE:

## If MINST data isn't loading, try this one:
## Go to your Python folder and find a script called
## Install Certificates.command. Double click to run it
## and it will install a lib called certifi.
## This tool will handle SSL certification for you.
## If you are on Mac it is here: /Applications/Python\ 3.6/Install\
## Certificates.command