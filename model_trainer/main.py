import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import os
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

print("TensorFlow version: {}".format(tf.__version__))

train_dataset_url = "http://download.tensorflow.org/data/iris_training.csv"

train_dataset_fp = '/home/maciej/Projects/PyCharmProjects/Drone-control-with-hand-gestures-using-image-processing' \
                   '/data_collector/data/iris_training.csv'

# train_dataset_fp = '/home/maciej/Projects/PyCharmProjects/Drone-control-with-hand-gestures-using-image-processing' \
#                    '/data_collector/data/02_data_max_abs.csv'

print("Local copy of the dataset file: {}".format(train_dataset_fp))

# column_names = ['WRIST_X', 'WRIST_Y',
#                 'THUMB_CMC_X', 'THUMB_CMC_Y',
#                 'THUMB_MCP_X', 'THUMB_MCP_Y',
#                 'THUMB_IP_X', 'THUMB_IP_Y',
#                 'THUMB_TIP_X', 'THUMB_TIP_Y',
#                 'INDEX_FINGER_MCP_X', 'INDEX_FINGER_MCP_Y',
#                 'INDEX_FINGER_PIP_X', 'INDEX_FINGER_PIP_Y',
#                 'INDEX_FINGER_DIP_X', 'INDEX_FINGER_DIP_Y',
#                 'INDEX_FINGER_TIP_X', 'INDEX_FINGER_TIP_Y',
#                 'MIDDLE_FINGER_MCP_X', 'MIDDLE_FINGER_MCP_Y',
#                 'MIDDLE_FINGER_PIP_X', 'MIDDLE_FINGER_PIP_Y',
#                 'MIDDLE_FINGER_DIP_X', 'MIDDLE_FINGER_DIP_Y',
#                 'MIDDLE_FINGER_TIP_X', 'MIDDLE_FINGER_TIP_Y',
#                 'RING_FINGER_MCP_X', 'RING_FINGER_MCP_Y',
#                 'RING_FINGER_PIP_X', 'RING_FINGER_PIP_Y',
#                 'RING_FINGER_DIP_X', 'RING_FINGER_DIP_Y',
#                 'RING_FINGER_TIP_X', 'RING_FINGER_TIP_Y',
#                 'PINKY_MCP_X', 'PINKY_MCP_Y',
#                 'PINKY_PIP_X', 'PINKY_PIP_Y',
#                 'PINKY_DIP_X', 'PINKY_DIP_Y',
#                 'PINKY_TIP_X', 'PINKY_TIP_Y', 'gestures']

# column order in CSV file
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

feature_names = column_names[:-1]
label_name = column_names[-1]

print("Features: {}".format(feature_names))
print("Label: {}".format(label_name))

class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']

# class_names = ['go_up', 'go_right', 'go_down']

batch_size = 32

train_dataset = tf.data.experimental.make_csv_dataset(
    train_dataset_fp,
    batch_size,
    column_names=column_names,
    label_name=label_name,
    num_epochs=1)

features, labels = next(iter(train_dataset))

print(features)
print(labels)

plt.scatter(features['petal_length'],
            features['sepal_length'],
            c=labels,
            cmap='viridis')

# plt.scatter(features['INDEX_FINGER_TIP_X'],
#             features['INDEX_FINGER_TIP_Y'],
#             c=labels,
#             cmap='viridis')

plt.xlabel("Petal length")
plt.ylabel("Sepal length")
plt.show()


def loss(model, x, y):
    y_ = model(x)
    return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)


def grad(model, inputs, targets):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, targets)
    return loss_value, tape.gradient(loss_value, model.trainable_variables)


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

global_step = tf.train.get_or_create_global_step()

loss_value, grads = grad(model, features, labels)

print("Step: {}, Initial Loss: {}".format(global_step.numpy(),
                                          loss_value.numpy()))

optimizer.apply_gradients(zip(grads, model.variables), global_step)

print("Step: {},         Loss: {}".format(global_step.numpy(),
                                          loss(model, features, labels).numpy()))

## Note: Rerunning this cell uses the same model variables

# keep results for plotting
train_loss_results = []
train_accuracy_results = []

num_epochs = 201

for epoch in range(num_epochs):
    epoch_loss_avg = tfe.metrics.Mean()
    epoch_accuracy = tfe.metrics.Accuracy()

    # Training loop - using batches of 32
    for x, y in train_dataset:
        # Optimize the model
        loss_value, grads = grad(model, x, y)
        optimizer.apply_gradients(zip(grads, model.variables),
                                  global_step)

        # Track progress
        epoch_loss_avg(loss_value)  # add current batch loss
        # compare predicted label to actual label
        epoch_accuracy(tf.argmax(model(x), axis=1, output_type=tf.int32), y)

    # end epoch
    train_loss_results.append(epoch_loss_avg.result())
    train_accuracy_results.append(epoch_accuracy.result())

    if epoch % 50 == 0:
        print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                    epoch_loss_avg.result(),
                                                                    epoch_accuracy.result()))

fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
fig.suptitle('Training Metrics')

axes[0].set_ylabel("Loss", fontsize=14)
axes[0].plot(train_loss_results)

axes[1].set_ylabel("Accuracy", fontsize=14)
axes[1].set_xlabel("Epoch", fontsize=14)
axes[1].plot(train_accuracy_results)

test_url = "http://download.tensorflow.org/data/iris_test.csv"

test_fp = tf.keras.utils.get_file(fname=os.path.basename(test_url),
                                  origin=test_url)

test_dataset = tf.contrib.data.make_csv_dataset(
    test_fp,
    batch_size,
    column_names=column_names,
    label_name='species',
    num_epochs=1,
    shuffle=False)

test_dataset = test_dataset.map(pack_features_vector)

test_accuracy = tfe.metrics.Accuracy()

for (x, y) in test_dataset:
    logits = model(x)
    prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
    test_accuracy(prediction, y)

print("Test set accuracy: {:.3%}".format(test_accuracy.result()))
