import tensorflow as tf 

# Defining a callback function
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}): 
        if (logs.get('accuracy') >= 0.96):
            print('\nStopping because the accuracy has exceeded 96%')
            self.model.stop_training = True

# Instantiating the callback function
callbacks = myCallback()

# Importing the dataset
mnist = tf.keras.datasets.fashion_mnist

# Loading the dataset
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# Normalizing the data
training_images = training_images / 255.0
test_images = test_images / 255.0

# Defining the model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    # The value 10 is due to the number of labels that exist
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compiling the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training the model
model.fit(training_images, training_labels, epochs=10, callbacks=[callbacks])

# Evaluating the model
model.evaluate(test_images, test_labels)

# Predicting using the test images
classifications = model.predict(test_images)

# A single test image
print(classifications[34])
print(test_labels[34])