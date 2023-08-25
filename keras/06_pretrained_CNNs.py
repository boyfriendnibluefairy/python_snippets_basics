##
##  How to use built-in pretrained Convolutional
##  Neural Networks from keras
##  Download time of weights : 2 mins
##
import tensorflow as tf

## Let's use sample images from sklearn to test
## our model
from sklearn.datasets import load_sample_images
sample_images = load_sample_images()["images"]

## view the images
# from keras.preprocessing.image import save_img
# i = 0
# for img in my_images:
#     i += 1
#     save_img(f"image_0{i}.png", img)

## EfficientNetB3 architecture is insepcting a size of 300 x 300 pixels.
## Let's resize the images before feeding it to our model
resized_images = tf.keras.layers.Resizing(height=300, width=300,
                                          crop_to_aspect_ratio=True)(sample_images)

## load your desired model from keras applications package
## and use the weights resulting from a previous training by
## other researchers
pretrained_model = tf.keras.applications.EfficientNetB3(weights="imagenet")

## We are not sure if EfficientNetB3 and other architecture/model prefer
## a pixel values scaled from 0 to 1 or from 0 to 255.
## Each model has preprocess_input() to change whatever scale your inputs
## have to a scale that the model prefer. To ensure that our input has
## the preferred scale, let's preprocess it:
preprocessed_inputs = tf.keras.applications.efficientnet.preprocess_input(resized_images)

## You can now use the pretrained model to make predictions:
y_probabilities = pretrained_model.predict(preprocessed_inputs)
print(y_probabilities.shape) ## output : (2, 1000)
## The output is a matrix with 2 rows and 1000 columns.
## The 2 rows refer to our two input images.
## ImageNet has 1000 classes to differentiate the images.
## Each column displays the probability that our image
## belongs to a specific class.
## Let's print the top six predictions by using
## decode_predictions()
top_predictions \
    = tf.keras.applications.efficientnet.decode_predictions(y_probabilities,top=6)
for i in range(len(preprocessed_inputs)):
    print(f"Image # {i}:")
    for class_id, class_name, y_probability in top_predictions[i]:
        print(f"{class_id} - {class_name:12s} {y_probability:.2%}")

### OUTPUT:
# Image # 0:
# n02825657 - bell_cote    47.49%
# n03877845 - palace       22.37%
# n09332890 - lakeside     6.41%
# n02980441 - castle       1.59%
# n03781244 - monastery    0.91%
# n03617480 - kimono       0.86%
# Image # 1:
# n03530642 - honeycomb    14.12%
# n11939491 - daisy        8.63%
# n13133613 - ear          4.89%
# n09229709 - bubble       4.27%
# n13052670 - hen-of-the-woods 2.86%
# n02948072 - candle       1.33%

## awesome!!!