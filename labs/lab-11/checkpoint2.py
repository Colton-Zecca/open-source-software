# Licensed with the MIT License, see the below page for where this code was found.
# Tutorial Source: https://www.tensorflow.org/tutorials/keras/classification
# --------------------------------------------------------------------------------

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

print(tf.__version__)

# ---------------Checkpoint 3 Image Setup--------------- #





# Greyscale
# 28x28 pixels - make sure you use cropping to get your image square before resizing it
# inverted (white is 0)
# scaled between 0 an 1 instead of 0 and 255

# Turn images into:
#   my_test_images: numpy uint8 array of grayscale image data with shape (num_samples, 28, 28).





# ---------------Inspect the first image--------------- #
# plt.figure()
# plt.imshow(my_test_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# my_test_images = my_test_images / 255.0
# ---------------End Checkpoint 3 Image Setup--------------- #


fashion_mnist = tf.keras.datasets.fashion_mnist

# The train_images and train_labels arrays are the training set; i.e. the data the model uses to learn
# The test_images and test_labels arrays are the test set; i.e. what the model is tested against
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# The name associated with the label number
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# ---------------Inspect the first image--------------- #
# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# Scale the values to a range of 0 to 1 instead of 0 to 255
train_images = train_images / 255.0
test_images = test_images / 255.0

# ---------------Verifying the data is in the correct format--------------- #
# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), # Reformats data (flattens the array)
    tf.keras.layers.Dense(128, activation='relu'), 
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)

# i = 0
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(i, predictions[i], test_labels, test_images)
# plt.subplot(1,2,2)
# plot_value_array(i, predictions[i],  test_labels)
# plt.show()

# i = 12
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(i, predictions[i], test_labels, test_images)
# plt.subplot(1,2,2)
# plot_value_array(i, predictions[i],  test_labels)
# plt.show()

# ---------------Checkpoint 2--------------- #
# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  image_index = 9000 + i
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(image_index, predictions[image_index], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(image_index, predictions[image_index], test_labels)
plt.tight_layout()
plt.show()

# ---------------Checkpoint 3--------------- #


# Turn images into:
#   my_test_images: numpy uint8 array of grayscale image data with shape (num_samples, 28, 28).

# ---------------Inspect the first image--------------- #
# plt.figure()
# plt.imshow(my_test_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# my_test_images = my_test_images / 255.0



# # Grab an image from the test dataset.
# img = my_test_images[1]
# print(img.shape)

# # Add the image to a batch where it's the only member.
# img = (np.expand_dims(img,0))
# print(img.shape)

# predictions_single = probability_model.predict(img)
# print(predictions_single)

# plot_value_array(1, predictions_single[0], test_labels)
# _ = plt.xticks(range(10), class_names, rotation=45)
# plt.show()