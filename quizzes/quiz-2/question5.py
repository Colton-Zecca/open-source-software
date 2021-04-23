import tensorflow as tf
from tensorflow.keras import Model
import matplotlib.pyplot as plt

# ( Code originally used tensorflow to find the 2 coefficients m and b of y = mx + b )
# Modify the code to solve for quadratics, make sure you update make_noisy_data AND code to calculate the solution
# y = a * x^2  +  b * x  +  c

# Define utilities
def make_noisy_data(a=0.5, b=-0.6, c=0.3, n=1000):
  x = tf.random.uniform(shape=(n,))
  noise = tf.random.normal(shape=(len(x),), stddev=0.01)
  
  y = a * (x * x) + b * x + c + noise
  return x, y

def predict(x):
  y = a * (x * x) + b * x + c
  return y

def squared_error(y_pred, y_true):
  return tf.reduce_mean(tf.square(y_pred - y_true))

# Set up the data:
x_train, y_train = make_noisy_data()
plot1 = plt.figure(1)
plt.plot(x_train, y_train, 'b.')
# plt.show()

a = tf.Variable(0.)
b = tf.Variable(0.)
c = tf.Variable(0.)

loss = squared_error(predict(x_train), y_train)
loss_vec = []
print("Starting loss {:.6f}".format(loss.numpy()))

# Training Parameters:
learning_rate = 0.4
steps = 2000

# Execute the gradient descent:
for i in range(steps):
  with tf.GradientTape() as tape:
      predictions = predict(x_train)
      loss = squared_error(predictions, y_train)

  loss_vec.append(loss)
  gradients = tape.gradient(loss, [a, b, c])

  a.assign_sub(gradients[0] * learning_rate)
  b.assign_sub(gradients[1] * learning_rate)
  c.assign_sub(gradients[2] * learning_rate)

  if i % 20 == 0:
      print("Step {:d}, Loss {:.6f}".format(i, loss.numpy()))


# Report data results
print("Solution: y = {:.6f} * x^2 + {:.6f} * x + {:.6f}".format(a.numpy(), b.numpy(), c.numpy()))
plot2 = plt.figure(2)
plt.plot(range(steps), loss_vec)
# plt.show()

plot3 = plt.figure(3)
plt.plot(x_train, y_train, 'b.')
plt.plot(x_train, predict(x_train), 'r.')
# plt.show()

plt.show()