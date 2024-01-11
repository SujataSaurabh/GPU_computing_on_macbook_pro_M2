import tensorflow as tf
import time

# Check if GPU is available
if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found. Please ensure you have a compatible GPU and TensorFlow-GPU installed.")

# Generate random matrices
matrix_size = 1000
matrix_a = tf.random.normal(shape=(matrix_size, matrix_size))
matrix_b = tf.random.normal(shape=(matrix_size, matrix_size))

# Perform matrix multiplication on GPU
with tf.device('/GPU:0'):
    tf.debugging.set_log_device_placement(True)
    start_time = time.time()
    result = tf.matmul(matrix_a, matrix_b)
    end_time = time.time()

# Print the result and execution time
print("Result matrix:")
print(result.numpy())
print("Execution time on GPU: {:.4f} seconds".format(end_time - start_time))

