##
##  Keras Image Processing Layers
##
import tensorflow as tf
from sklearn.datasets import load_sample_images
import matplotlib.pyplot as plt
from keras.preprocessing.image import save_img

## let's view first what load_sample_images look like
my_images = load_sample_images()["images"]
# for img in my_images:
#     plt.imshow(tf.keras.preprocessing.image.array_to_img(img))
#     plt.show()
## we can also view images by saving it to a file
i = 0
for img in my_images:
    i += 1
    save_img(f"image_0{i}.png", img)

## create a crop image layer to centercrop the image with
## the ff sizes:
crop_img_layer = tf.keras.layers.CenterCrop(height=100, width=100)

## apply the cropping layer on the images
cropped_images = crop_img_layer(my_images)

## let's view the cropped images
i = 0
for img in cropped_images:
    i += 1
    save_img(f"cropped_0{i}.png", img)

## tf.keras.layers.Rescaling is used to map pixel
## values to a new range, i.e. [0, 255] to [0, 1]
## f.keras.layers.Resizing is used for resizing the
## image, like from making it bigger or making it
## smaller
expanded_img_layer = tf.keras.layers.Resizing(height=300, width=300)
expanded_images = expanded_img_layer(cropped_images)
i = 0
for img in expanded_images:
    i += 1
    save_img(f"expanded_0{i}.png", img)