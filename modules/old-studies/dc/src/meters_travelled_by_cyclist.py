from matplotlib import pyplot as plt
import numpy as np

def q(x):
    return 2 * x + 1

if __name__ =='__main__':
    x = np.array(range(0, 10+1))

    plt.figure(figsize=(7, 5))  # Largura(Width), Height(Altura).
    plt.plot(x, q(x), color='green', marker='o')
    plt.title("q(x) = 2x + 1")
    plt.xlabel('Segundos')
    plt.ylabel('Metros')
    plt.xticks(range(0, 10+1, 1))
    plt.yticks(range(0, 21+1, 1))
    plt.grid()
    plt.savefig("../images/meters-travelled-01.png")
    plt.show()
