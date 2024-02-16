import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

w = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)
x = np.arange(1, 5)

y = w * x + b

print(y)

plt.plot(x, y)
plt.savefig("../images/tf-var-01.png", format="png")
plt.show()
