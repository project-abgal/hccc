from chainer import Chain
import chainer.functions as F
import chainer.links as L


class CCCNN(Chain):
    def __init__(self, out_size):
        super(CCCNN, self).__init__()
        with self.init_scope():
            self.conv1 = L.Convolution2D(None, out_channels=16, ksize=3)
            self.conv2 = L.Convolution2D(None, out_channels=32, ksize=3)
            self.conv3 = L.Convolution2D(None, out_channels=64, ksize=3)
            self.conv4 = L.Convolution2D(None, out_channels=128, ksize=3)
            self.fc1 = L.Linear(None, 512)
            self.fc2 = L.Linear(None, out_size)

    def forward(self, x):
        h = F.relu(self.conv1(x))
        h = F.dropout(F.max_pooling_2d(h, 2, 2))
        h = F.relu(self.conv2(h))
        h = F.dropout(F.max_pooling_2d(h, 2, 2))
        h = F.relu(self.conv3(h))
        h = F.dropout(F.max_pooling_2d(h, 2, 2))
        h = F.relu(self.conv4(h))
        h = F.dropout(F.max_pooling_2d(h, 2, 2))
        h = F.dropout(F.relu(self.fc1(h)))
        return self.fc2(h)

