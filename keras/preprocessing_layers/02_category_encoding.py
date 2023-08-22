##
##  Keras Category Encoding Layer
##  -> The goal of this layer is to convert
##  categorical feature into numerical features
##  since it's easier to perform computations
##  on numbers than texts or strings.
##
import numpy as np
import tensorflow as tf
tf.random.set_seed(42)

## If there are only 2 to 12 categories, one-hot encoding
## is the recommended option for category encoding
# onehot_layer = tf.keras.layers.CategoryEncoding(num_tokens=6)
# print(onehot_layer)

## So far, the code above works if your category is initially
## numerical. StringLookup layer is used when categories are
## specified in text form:
houses = ["Arryn", "Baratheon", "Celtigar", "Stark", "Stark", "Targaryen"]
str_lookup_layer = tf.keras.layers.StringLookup()
## Use adapt() method to assign unknown categories to 0.
## Known categories are assigned 1, 2, 3, ....
## The most frequent category is assigned 1, the next most frequent
## is assigned 2, and so on...
str_lookup_layer.adapt(houses)

## In machine learning, we sometimes map discrete variables into
## continuous vectors (which means each instance will have
## x-component and y-component if we have 2D vector space) so that
## we can view them in vector space. Once in vector space,
## we can quantify the semantic similarity between categories.
## This is where embedding comes in.
lookup_and_embed = tf.keras.Sequential([
    str_lookup_layer,
    tf.keras.layers.Embedding(input_dim=str_lookup_layer.vocab_size(),
                              output_dim=2)
])
## input_dim = total number of categories estimated by the algorithm + OOV bucket
## by default OOV bucket = 1.
## OOV bucket refers to the bins where unknown categories are dumped
## if output_dim = 2, this means each category is mapped into vector with 2 components

## we can now use the above converter to transform categorical variable into
## numerical variable
lookup_and_embed(np.array([["Arryn", "Baratheon", "Celtigar", "Stark", "Stark", "Targaryen"]]))


## DONE!!!


## Here is some example:
## Suppose we have training set and a validation data set
## which are divided into numerical variables (num)
## and categorical variables (cat)
X_train_num, X_train_cat, y_train = [...] # training set
X_valid_num, X_valid_cat, y_valid = [...] # validation set

## say we have 9 numerical inputs and 6 categorical inputs
num_input = tf.keras.layers.Input(shape=[9], name="num")
cat_input = tf.keras.layers.Input(shape=[6], dtype=tf.string, name="cat")

## we use the previously created lookup_and_embed() to convert
## the categorical input into a trainable embedding vectors
cat_embeddings = lookup_and_embed(cat_input)

## since we now converted categorical input into something numerical
## we concatenate or combine all inputs into one data frame, as you may,
## so that we can feed them to our neural network
encoded_inputs = tf.keras.layers.concatenate([num_input, cat_embeddings])

## for code conciseness, let's save the output layer on a variable
output_layer = tf.keras.layers.Dense(1)(encoded_inputs)

## for simplicity, let's design a model with no hidden layers
model = tf.keras.models.Model(inputs=[num_input, cat_input], outputs=[outputs])

## compile the model so we can set the values of hyperparameters
model.compile(loss="mse", optimizer="sgd")

## we can now train our model.
## we can save the details of our training to a variable, i.e. history
## so that we can print it later
history = model.fit((X_train_num, X_train_cat), y_train, epochs=5,
                        validation_data=((X_valid_num, X_valid_cat), y_valid))
