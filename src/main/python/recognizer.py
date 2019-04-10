import tensorflow as tf

def nth_batch(data, batch_size, ix):
    off = ix * batch_size
    return data[off:off+batch_size]

class Recognizer:
    learning_rate = 0.5
    epochs = 10
    batch_size = 100

    def __init__(self, data_set):
        input = tf.placeholder(tf.float32, [None, 100])
        output = tf.placeholder(tf.float32, [None, 8])

        W1 = tf.Variable(tf.random_normal([100, 75], stddev=0.03), name='W1')
        b1 = tf.Variable(tf.random_normal([75], stddev=0.03), name='b1')
        W2 = tf.Variable(tf.random_normal([75, 8], stddev=0.03), name='W2')
        b2 = tf.Variable(tf.random_normal([8], stddev=0.03), name='b2')

        hidden_out = tf.add(tf.matmul(x, W1), b1)
        hidden_out = tf.nn.relu(hidden_out)

        output_ = tf.nn.softmax(tf.add(tf.matmul(hidden_out, W2), b2))

        output_clipped = tf.clip_by_value(output_, 1e-10, 0.9999999)
        cross_entropy = tf.reduce_mean(tf.reduce_sum(output * tf.log(output_clipped) + (1 - output) * tf.log(1 - output_clipped), axis=1))

        optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cross_entropy)

        init_op = tf.global_variables_initializer()

        correct_prediction = tf.equal(tf.argmax(output, 1), tf.argmax(output_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        sess = tf.Session()
        sess.run(init_op)
        total_batch = int(len(data_set) / batch_size)
        for epoch in range(epochs):
            avg_cost = 0
            for i in range(total_batch):
                batch_inp, batch_out = nth_batch(data_set, batch_size, i)
                _, c = sess.run([optimizer, cross_entropy], feed_dict={input: batch_inp, output: batch_out})
                avg_cost += c / total_batch

        self.output = output_
        self.session = sess

    def run(inp):
        return self.session.run(self.output, feed_dict={input: inp, output: tf.random_normal([8], stddev=0.03)})
