import os
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Oculta os avisos do TensorFlow

# Carrega o dataset Iris
iris = load_iris()
X = iris.data  # 4 features
y = iris.target  # 3 classes

# Pré-processamento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# One-hot encoding das classes
y_train_ohe = tf.keras.utils.to_categorical(y_train, num_classes=3)
y_test_ohe = tf.keras.utils.to_categorical(y_test, num_classes=3)

# Input com 4 features
n_inputs = X.shape[1]  # 4
inputs = tf.keras.Input(shape=(n_inputs,), name="input_layer")

# Camadas Ocultas (Hidden Layers)
hidden1 = tf.keras.layers.Dense(5, activation="relu", name="hidden_layer_1")(inputs)
hidden2 = tf.keras.layers.Dense(3, activation="relu", name="hidden_layer_2")(hidden1)

# Camada de Saída (Output Layer)
output = tf.keras.layers.Dense(3, activation="softmax", name="output_layer")(hidden2)

# Cria o modelo (conecta as camadas)
model = tf.keras.Model(inputs=inputs, outputs=output)
model.summary()  # Visualiza a estrutura da Rede Neural

# Compilação
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Treinamento
model.fit(
    X_train,
    y_train_ohe,
    epochs=50,
    batch_size=8,
    verbose=0
)

# Avaliação
loss, accuracy = model.evaluate(X_test, y_test_ohe, verbose=0)
print(f"\nAcurácia do modelo: {accuracy:.2f}")

# Previsão com um exemplo real
sample = X_test[0].reshape(1, -1)
prediction = model(sample)
print("\nPredição (probabilidades):", prediction.numpy())
print("Classe prevista:", tf.argmax(prediction, axis=1).numpy())
print("Classe Real:", y_test[0])
