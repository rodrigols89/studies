import os
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings


# Input size.
n_inputs = 5

# Tensor of input.
inputs = tf.keras.Input(shape=(n_inputs,), name="input_layer")

# Hidden layers.
hidden1 = tf.keras.layers.Dense(4, name="hidden_layer_1")(inputs)
hidden2 = tf.keras.layers.Dense(4, name="hidden_layer_2")(hidden1)
hidden3 = tf.keras.layers.Dense(4, name="hidden_layer_3")(hidden2)

# Output layer.
output = tf.keras.layers.Dense(1, name="output_layer")(hidden3)

# Make the model (connect the layers).
model = tf.keras.Model(inputs=inputs, outputs=output)
model.summary()  # Visualize the model architecture.

# Make random input data (one sample with 5 features).
input_data = tf.random.normal((1, n_inputs))

result = model(input_data)  # Apply forward pass.

print("\nTensor:", result)
print("Tensor value:", result.numpy())
