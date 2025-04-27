from matplotlib import pyplot as plt
import pandas as pd

def f(x):
  return x**2

if __name__ =='__main__':

    df = pd.DataFrame({'x': range(-10, 10+1)}) # x Values.
    df['y'] = [f(x) for x in df.x] # y Values.

    print(df)

    # Window Settings
    dpi = 100
    width_px = 800
    height_px = 500
    figsize = (width_px / dpi, height_px / dpi)

    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(df.x, df.y, color='blue', marker='o')
    plt.title(r'$f(x) = x^{2}$')
    plt.xlabel('x')
    plt.ylabel(r'$x^{2}$')
    plt.xticks(range(-10, 10+1, 1))
    plt.yticks(range(0, 100+1, 5))
    plt.grid()
    plt.savefig("../images/derivative-plot-01.png")
    plt.show()
