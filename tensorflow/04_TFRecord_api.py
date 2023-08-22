##
##  TFRecord is a flexible format which can store
##  text, images, audio, compressed video, and any data
##  that can be cast to a byte representation.
##
import tensorflow as tf

## How to create a TFRecord file from scratch:
# with tf.io.TFRecordWriter("sample_data.tfrecord") as f:
#     f.write(b"first sample record")
#     f.write(b"second sample record")
#     f.write(b"third sample record")

## How to read TFRecord file:
# file_names = ["sample_data.tfrecord"]
# sample_dataset = tf.data.TFRecordDataset(file_names)
# for item in sample_dataset:
#     print(item)

## How to save and compress TFRecord files for efficient
## network transfer using TFRecordWriter object
options = tf.io.TFRecordOptions(compression_type="GZIP")
with tf.io.TFRecordWriter("compressed_data.tfrecord", options) as f:
    f.write(b"first record")
    f.write(b"second record")
    f.write(b"last line before compressing")

## How to read compressed file:
## Note that compression type must be specified.
sample_dataset = tf.data.TFRecordDataset(["compressed_data.tfrecord"],
                                         compression_type="GZIP")
