import tensorflow as tf
import numpy as np

def kinetic_energy(velocity: tf.Variable) -> float:
    return 0.5 * tf.square(velocity)

def hamiltonian(position: tf.Variable, velocity: tf.Variable, energy_function) -> float:
    return energy_function(position) + kinetic_energy(velocity)

def leapfrog_step(x0: tf.Variable, v0: tf.Variable, log_posterior, step_size: float, num_steps: int) -> tf.Variable:

    v = v0 - 0.5 * step_size * tf.gradients(log_posterior(x0), x0)[0]
    x = x0 + step_size * v

    for _ in range(num_steps):
        gradient = tf.gradients(log_posterior(x), x)[0]
        v = v - step_size * gradient
        x = x + step_size * v
    v = v - 0.5 * step_size * tf.gradients(log_posterior(x), x)[0]

    return x, v

def hmc(initial_x: tf.Variable, step_size: float, num_steps: int, log_posterior: str) -> tf.Variable:
    v0 = tf.random_normal(initial_x.get_shape())
    x, v = leapfrog_step(initial_x,
                      v0, 
                      step_size=step_size, 
                      num_steps=num_steps, 
                      log_posterior=log_posterior)

    orig = hamiltonian(initial_x, v0, log_posterior)
    current = hamiltonian(x, v, log_posterior)
    p_accept = min(1.0, tf.exp(orig - current))

    if p_accept > np.random.uniform():
        return x
    else:
        return initial_x