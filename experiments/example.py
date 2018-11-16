from hmc import hmc
import tensorflow as tf
import numpy as np

def gaussian_log_posterior_correlated(x):
  covariance = tf.constant(
    np.array([
        [1.0, 0.8],
        [0.8, 1.0]]), 
    dtype=tf.float32
  )
      
  covariance_inverse = tf.matrix_inverse(covariance)

  xA = tf.matmul(x, covariance_inverse)
  xAx = tf.matmul(xA, tf.transpose(x))
  return xAx / 2.0

def main():
  num_samples = 20
  # Number of dimensions for samples
  ndim = 2

  session = tf.Session()
  with session.as_default():
    print("Drawing from a correlated Gaussian...")
    initial_x = tf.Variable(
      tf.random_normal(
        (1, ndim), 
        dtype=tf.float32)
      )
    session.run(tf.initialize_all_variables())
    for i in range(num_samples):
      sample = session.run(
        hmc(initial_x, 
          log_posterior=gaussian_log_posterior_correlated, 
          step_size=0.1, 
          num_steps=10)
      )
      print(sample)