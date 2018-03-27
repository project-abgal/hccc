import os
# change the value according to the GPU you want to use
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import numpy as np
from glob import glob
from tqdm import tqdm
from prefetch_generator import BackgroundGenerator
from keras.callbacks import TensorBoard
from model import *

# ready for training
import tensorflow as tf
f_log = './log'
tb_cb = TensorBoard(log_dir=f_log, histogram_freq=10000, write_graph=False)
#config = tf.ConfigProto(gpu_options=tf.GPUOptions(
#    per_process_gpu_memory_fraction=0.45))
#session = tf.Session(config=config)
session = tf.Session()
model_size = 28
num_of_classes = 2
mod = get_net(model_size, num_of_classes, session=session)
session.run(tf.global_variables_initializer())


# x_train =
# y_train =
# put images here as array
# x_train: list of images (28,28,3)
# x_test =
# y_test =

# training
epochs = 501

for e in tqdm(range(epochs)):
    mod.fit(x_train, y_train, epochs=1, shuffle=True, verbose=1,
            batch_size=1024, callbacks=[tb_cb], validation_data=(x_test, y_test))
    if e % 50 == 0:
        mod.save("put the folder you want to save the model here.")
print('done.')
