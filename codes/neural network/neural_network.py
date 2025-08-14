import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Simple neural network
model = Sequential([
    Dense(16, activation='relu', input_shape=(10,)),  # Input layer with 10 features
    Dense(8, activation='relu'),                      # Hidden layer
    Dense(1, activation='sigmoid')                    # Output layer (binary classification)
])

model.summary()
