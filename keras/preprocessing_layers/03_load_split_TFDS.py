##
##  TensorFlow DataSets (TFDS) are collection
##  of datasets that are ready-to-use with tensorflow
##
import tensorflow as tf
import tensorflow_datasets as tfds
tf.random.set_seed(42)

## Download your data using the load() method
## tfds can automatically split the training data set and
## test data set using the split argument. For example,
## [ ] use the first 60 % of training data for training
## [ ] use remaning 40 % for validation
## [ ] use 100 % of test data for calculating generalization error
## as_supervised=True means that you're telling tensorflow that data
## consist of label and feature.
X_train, X_valid, X_test = tfds.load(
    name="mnist",
    split=["train[:90%]", "train[90%:]", "test"],
    as_supervised=True
)

## shuffle your training dataset.
## buffer_size has something to do with the cards analogy of shuffling.
## batch(m) means you'll shuffle the set for every m batches
## prefetch(n) means you'll fetch the next n batch while shuffling the latest batch
X_train = X_train.shuffle(buffer_size=9_000, seed=42).batch(30).prefetch(3)
## temporarily cache other data on memory or local storage to improve
## performance
X_valid = X_valid.batch(30).cache()
X_test = X_test.batch(30).cache()

## for simplicity, let's build a model with no hidden layers
my_model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),         # input layer
    tf.keras.layers.Dense(10, activation="softmax")  # output layer
])

## compile the model to set hyperparameter values
my_model.compile(loss="sparse_categorical_crossentropy",
                 optimizer="nadam",
                 metrics=["accuracy"])

## train the model while saving the training details on the
## variable history
history = my_model.fit(X_train, validation_data=X_valid, epochs=6)

## calculate the generalization accuracy
test_loss, test_accuracy = my_model.evaluate(X_train)
print(test_loss)
print("=========")
print(test_accuracy)

