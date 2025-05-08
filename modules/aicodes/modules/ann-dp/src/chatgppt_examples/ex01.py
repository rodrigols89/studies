import sys
import os

# Adiciona o caminho do diretório datasets ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Oculta os warnings do TensorFlow

from datasets.synthetic import spiral_data

# 1. Carrega os dados
X, y = spiral_data(samples=100, classes=3)

# 2. Visualização da distribuição dos dados
plt.figure(figsize=(6, 5))
plt.title("Distribuição das classes (espiral)")
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg", edgecolors="k")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.show()

# 3. Define o modelo
inputs = tf.keras.Input(shape=(2,), name="input_layer")
x = tf.keras.layers.Dense(4, activation='sigmoid', name="hidden_layer_1")(inputs)
x = tf.keras.layers.Dense(4, activation='sigmoid', name="hidden_layer_2")(x)
x = tf.keras.layers.Dense(4, activation='sigmoid', name="hidden_layer_3")(x)
outputs = tf.keras.layers.Dense(3, activation='softmax', name="output_layer")(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.summary()

# 4. Compila o modelo
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Treina o modelo e guarda o histórico
history = model.fit(X, y, epochs=100, verbose=0)

# 6. Visualização do histórico de treinamento
plt.figure(figsize=(12, 5))

# Loss
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Loss', color='red')
plt.title('Evolução da Loss')
plt.xlabel('Época')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()

# Accuracy
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Accuracy', color='blue')
plt.title('Evolução da Acurácia')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
