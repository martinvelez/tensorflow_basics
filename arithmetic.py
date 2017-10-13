import tensorflow as tf

print("Creating tensors...")
# These operations return a tensor.
t1 = tf.add(1,2)
t2 = tf.sub(1,2)
t3 = tf.mul(1,2)
t4 = tf.div(1,2)

# Create a session
sess = tf.Session()

result = sess.run(t1)
print(result)
result = sess.run(t2)
print(result)
result = sess.run(t3)
print(result)
result = sess.run(t4)
print(result)
