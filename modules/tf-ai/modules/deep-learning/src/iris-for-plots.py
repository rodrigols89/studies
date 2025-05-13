import os
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Oculta os avisos do TensorFlow

from plots import plot_loss, plot_accuracy, loss_vs_accuracy_plot, plot_confusion_matrix


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

# Compilação
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Treinamento
history = model.fit(
    X_train,
    y_train_ohe,
    validation_data=(X_test, y_test_ohe),  # obrigatório para ter val_loss e val_accuracy
    epochs=50,
    batch_size=8,
    verbose=0
)

y_pred = model.predict(X_test)
y_pred_classes = tf.argmax(y_pred, axis=1).numpy()

# Usando a função
plot_confusion_matrix(
    y_true=y_test,
    y_pred=y_pred_classes,
    class_names=["Setosa", "Versicolor", "Virginica"],
    filename="confusion-matrix-01.png"
)

