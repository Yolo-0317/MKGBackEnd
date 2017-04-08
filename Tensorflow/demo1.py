# -*-coding=utf-*-  
import tensorflow as tf
import numpy as np

training_data = np.loadtxt('./training.txt', delimiter=',', unpack=True, dtype='float32')
test_data = np.loadtxt('./test.txt', delimiter=',', unpack=True, dtype='float32')

training_data = training_data.T  # 转置
test_data = test_data.T

# print(training_data.shape)

iris_X = training_data[:, 0:4]  # [行，列]
iris_Y = training_data[:, 4:7]

iris_test_X = test_data[:, 0:4]
iris_test_Y = test_data[:, 4:7]


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size])) + 0.1  # 推荐biases最好不为零
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:  # activation_function=none表示线性函数，否则是非线性
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def computer_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


xs = tf.placeholder(tf.float32, [None, 4])
ys = tf.placeholder(tf.float32, [None, 3])

prediction = add_layer(xs, 4, 3, activation_function=tf.nn.softmax)  # softmax一般用来做classification

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))  # loss
# 学习速率根据 具体使用的数据进行选取
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(cross_entropy)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
for i in range(700):  # 迭代700次
    sess.run(train_step, feed_dict={xs: iris_X, ys: iris_Y})
    if i % 50 == 0:
        print(computer_accuracy(iris_test_X, iris_test_Y),
              sess.run(cross_entropy, feed_dict={xs: iris_X, ys: iris_Y}))  # 测试准确率与训练误差

# save to file
W = tf.Variable([[1., 2., 3.], [4., 5., 6.]], name='weights')
b = tf.Variable([[1., 2., 3.]], name='biases')

init = tf.initialize_all_variables()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "./save_net.ckpt")  # 存储网络到XX路径
    print('Save to path:', save_path)
