import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

from sklearn.metrics import confusion_matrix


def plot_loss(history, filename="loss_plot.png"):
    """
    Gera e salva um gráfico de perda (loss) por época com base no objeto `history` do Keras.

    Parâmetros:
    - history: objeto retornado por model.fit()
    - filename: nome do arquivo de imagem que será salvo
    """
    loss = history.history.get("loss")
    val_loss = history.history.get("val_loss")

    epochs = range(1, len(loss) + 1)

    plt.figure(figsize=(8, 5))
    plt.plot(epochs, loss, "b-", label="Loss de Treinamento")
    
    if val_loss:
        plt.plot(epochs, val_loss, "r--", label="Loss de Validação")

    plt.title("Perda (Loss) por Época")
    plt.xlabel("Época")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)

    plt.savefig("../images/" + filename)
    plt.close()


def plot_accuracy(history, filename="accuracy_plot.png"):
    """
    Gera e salva um gráfico de acurácia por época com base no objeto `history` do Keras.

    Parâmetros:
    - history: objeto retornado por model.fit()
    - filename: nome do arquivo de imagem que será salvo
    """
    acc = history.history.get("accuracy")
    val_acc = history.history.get("val_accuracy")

    epochs = range(1, len(acc) + 1)

    plt.figure(figsize=(8, 5))
    plt.plot(epochs, acc, "b-", label="Acurácia de Treinamento")
    
    if val_acc:
        plt.plot(epochs, val_acc, "g--", label="Acurácia de Validação")

    plt.title("Acurácia por Época")
    plt.xlabel("Época")
    plt.ylabel("Acurácia")
    plt.legend()
    plt.grid(True)

    plt.savefig("../images/" + filename)
    plt.close()


def loss_vs_accuracy_plot(history, filename="training_metrics.png"):
    """
    Gera e salva um gráfico com a perda (loss) e acurácia (accuracy) por época, usando o histórico de treinamento.
    
    Parâmetros:
    - history: objeto retornado por model.fit()
    - filename: nome do arquivo de imagem a ser salvo
    """
    loss = history.history.get("loss")
    val_loss = history.history.get("val_loss")
    acc = history.history.get("accuracy")
    val_acc = history.history.get("val_accuracy")

    epochs = range(1, len(loss) + 1)

    plt.figure(figsize=(12, 5))

    # 🔻 Subplot 1: Perda
    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss, "b-", label="Perda de Treinamento")
    if val_loss:
        plt.plot(epochs, val_loss, "r--", label="Perda de Validação")
    plt.title("Perda por Época")
    plt.xlabel("Época")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)

    # 🔺 Subplot 2: Acurácia
    plt.subplot(1, 2, 2)
    plt.plot(epochs, acc, "g-", label="Acurácia de Treinamento")
    if val_acc:
        plt.plot(epochs, val_acc, "m--", label="Acurácia de Validação")
    plt.title("Acurácia por Época")
    plt.xlabel("Época")
    plt.ylabel("Acurácia")
    plt.legend()
    plt.grid(True)

    plt.savefig("../images/" + filename)
    plt.close()


def plot_confusion_matrix(y_true, y_pred, class_names=None, filename="confusion_matrix.png"):
    """
    Gera e salva um gráfico de matriz de confusão.
    
    Parâmetros:
    - y_true: rótulos verdadeiros
    - y_pred: rótulos previstos pelo modelo
    - class_names: nomes das classes (opcional)
    - filename: nome do arquivo de saída
    """
    # Calcula a matriz de confusão
    cm = confusion_matrix(y_true, y_pred)

    # Cria os rótulos se não forem fornecidos
    if class_names is None:
        class_names = [str(i) for i in range(cm.shape[0])]

    # Cria o gráfico
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=class_names,
                yticklabels=class_names)

    plt.xlabel("Classe Predita")
    plt.ylabel("Classe Real")
    plt.title("Matriz de Confusão")
    plt.tight_layout()

    plt.savefig("../images/" + filename)
    plt.close()
