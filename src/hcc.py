import random
import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training
from chainer.training import extensions
import argparse
import os
import glob
from PIL import Image
import numpy as np
from cc_cnn import CCCNN
from common import get_labels

# FIXME:
IMAGE_PATH = '../images/'


def load_training_data():
    labels = get_labels(IMAGE_PATH)
    data = []
    for l in labels:
        for image_file in glob.glob("{0}{1}/*.png".format(IMAGE_PATH, l)):
            image = Image.open(image_file)
            # some file has alpha channel
            data.append((np.asarray(image.convert('RGB')).reshape(3, 64, 64).astype(np.float32)/255, labels.index(l)))
    return data


def training_hcc(resume = None):
    train_data = load_training_data()
    random.shuffle(train_data)
    threshold = int(len(train_data) * 0.8)
    print("number of training data {0}".format(threshold))
    train_iter = chainer.iterators.SerialIterator(train_data[:threshold], 100)
    test_iter = chainer.iterators.SerialIterator(train_data[threshold:], 100, repeat=False, shuffle=False)
    model = L.Classifier(CCCNN(len(get_labels(IMAGE_PATH))), lossfun=F.softmax_cross_entropy)
    optimizer = chainer.optimizers.Adam().setup(model)

    updater = training.StandardUpdater(train_iter, optimizer, device=-1)
    trainer = training.Trainer(updater, (300, 'epoch'), out='result')

    trainer.extend(extensions.Evaluator(test_iter, model, device=-1))
    trainer.extend(extensions.dump_graph('main/loss'))
    trainer.extend(extensions.snapshot(), trigger=(10, 'epoch'))
    trainer.extend(extensions.LogReport())
    if extensions.PlotReport.available():
        trainer.extend(extensions.PlotReport(['main/loss', 'validation/main/loss'], 'epoch', file_name='loss.png'))
        trainer.extend(extensions.PlotReport(['main/accuracy', 'validation/main/accuracy'], 'epoch', file_name='accuracy.png'))
    trainer.extend(extensions.PrintReport(['epoch',
                                           'main/loss',
                                           'validation/main/loss',
                                           'main/accuracy',
                                           'validation/main/accuracy',
                                           'elapsed_time']))
    if resume is not None:
        print("resume {}".format(resume))
        # Resume from a snapshot
        chainer.serializers.load_npz(resume, trainer)

    print("training start")
    trainer.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='mode for running')
    parser.add_argument('--resume', help='snapshot for resuming')
    args = parser.parse_args()
    if args.mode == 'training':
        print('Start Training')
        training_hcc(args.resume)
    elif args.mode == 'predict':
        print('Start Prediction')
