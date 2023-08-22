##
##  Keras Normalization Layer
##  -> normalizes continuous features
##  -> shift and scale inputs into a distribution
##     centered around 0 with standard deviation 1
##

import tensorflow as tf

## create normalizaton layer object
norm_layer = tf.keras.layers.Normalization()

## feed your training data to the norm_layer so that
## the internal parameters of the norm_layer will adjust
## based on the given data, e.g. create numpy array or tf graph
## for later calculations, etc.
norm_layer.adapt(X_train)

## you can also just extract scaled versions of X_train
## and X_valid for later use
X_scaled_train = norm_layer(X_train)
X_scaled_valid = norm_layer(X_valid)

## create your model using keras Sequential API
my_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1)
])

## compile the model to set hyperparameters
my_model.compile(loss="mse",
                 optimizer=tf.keras.optimizers.SGD(learning_rate=2e-3))

## you can now train your model
model.fit(X_scaled_train, y_train, epochs=5,
          validation_data=(X_scaled_valid, y_valid))

## When we deploy the model, the deployed model will not apply
## the normalization layer to the inputs because it's not
## included in the deployed model. To forcibly include the
## normalization inside the model, we wrap the adapted
## Normalization layer and the trained model:
wrapped_model = tf.keras.Sequential([norm_layer, my_model])

## To test the wrapped model, select six unscaled instances
## from the test data set
X_sampled_test = X_test[:6]
y_pred = wrapped_model(X_sampled_test)