import tensorflow as tf 
import numpy as np

# The arrays 
xs = np.array([1, 2, 3, 4, 5])
ys = np.array([3, 5, 7, 9, 11])


# A model with only one neural network
model = tf.keras.Sequential([
	tf.keras.layers.Dense(1, input_shape=[1])
])

# Compiling the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Training the model
model.fit(xs, ys, epochs=10)

# Predicting with another number
print(model.predict([10.0]))