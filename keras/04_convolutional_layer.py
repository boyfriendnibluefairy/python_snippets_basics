## How to implement convolutional layer in Keras
import tensorflow as tf

## Let's use sample images from sklearn to test
## our convolutional layer
from sklearn.datasets import load_sample_images
my_images = load_sample_images()["images"]

## view the images
# from keras.preprocessing.image import save_img
# i = 0
# for img in my_images:
#     i += 1
#     save_img(f"image_0{i}.png", img)

## centercrop and rescale the images
cropped_images = tf.keras.layers.CenterCrop(height=60, width=120)(my_images)
rescaled_images = tf.keras.layers.Rescaling(scale=1/255)(cropped_images)
# ## view the images
# from keras.preprocessing.image import save_img
# i = 0
# for img in rescaled_images:
#     i += 1
#     save_img(f"rescaled_0{i}.png", img)

## Let's view the dimensions of the resulting image tensor
print(rescaled_images.shape) ## (2, 60, 120, 3)
## this outputs [a, b, c, d] where a,b,c,d are scalars
## a refers to number of batches, in our case, this refers to num of images
## b, c refer to image size, e.g. 60 px by 120 px
## d refers to the data's channel, e.g. RGB

## Let's now feed the image to keras 2D ( recall the sizes b & c above)
## convolution layer
conv2d_layer = tf.keras.layers.Conv2D(filters=36, kernel_size=6)
## A single filter is randomly initialized with random weights.
## Backprop adjusts these weights to minimize the loss.
## Hence there's no maximum limit about the number of filters.
## kernel_size=6 means we have 6 by 6 matrix (2d for 2d conv)
## each cell in the matrix was initialized with random weight.
feature_maps = conv2d_layer(rescaled_images)
## let's explore the shape of the conv output
print(feature_maps.shape) ## (2, 55, 115, 36)
## We have 36 channels. This is because we applied 36 filters
## which resulted to 36 feature maps stacked on convolution layer 1.
## Instead of RGB maps from the input, we now have 36 intensity patterns
## resulting from 36 filters.
## The size 55 and 115 is smaller than the previous because
## Conv2D does not apply zero padding by default.