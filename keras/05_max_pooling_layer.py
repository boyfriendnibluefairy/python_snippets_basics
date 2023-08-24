##
##  Pooling layers are applied after conv layers in CNN.
##  The basic purpose of pooling is to make computation faster
##  by reducing the size of feature maps. Though averaging pooling
##  collectively represents the pixels from a receptive field,
##  max pooling is generally preferred because it chooses the
##  strogest/brightest features from the receptive field.
##
import tensorflow as tf

## How to create max pooling layer:
max_pool_layer = tf.keras.layers.MaxPool2D(pool_size=3)
## pool size refers to kernel size of filter size