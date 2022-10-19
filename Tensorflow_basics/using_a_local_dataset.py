import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator 


training_dir = "horse-or-humans/training"
validation_dir = "horse-or-human/validation"
# All images will be rescaled by 1/255 
training_datagen = ImageDataGenerator(rescale=1/255)
train_generator = training_datagen.flow_from_directory(
	training_dir,
	target_size =(300, 300),
	class_mode = 'binary'
)

# Validation 
validation_datagen = ImageDataGenerator(rescale=1/255)
validation_generator = validation_datagen.flow_from_directory(
	validation_dir,
	target_size =(300, 300),
	class_mode="binary"
)


# The model 
model = tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
	tf.keras.layers.MaxPooling2D(2, 2), 
	tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2, 2), 
	tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2, 2),
	tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2, 2),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(512, activation="relu"),
	tf.keras.layers.Dense(1, activation="sigmoid")
])


# Compiling the model 
model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
	loss = 'binary_crossentropy',
	metrics = ['accuracy']
)

# Training the model
history = model.fit(
	train_generator,
	epochs = 15,
	validation_data = validation_generator
)