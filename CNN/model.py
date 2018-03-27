from keras import backend as K
from keras.engine.topology import Input, Container
from keras.models import Model
from keras.layers import *
from keras.optimizers import *

K.set_image_dim_ordering("tf")
print("image_dim_ordering:tf")


def get_net(size, classes, session=None):

    inputs = Input(shape=(size, size, 3))

    midout = Conv2D(4, 3, padding="same", activation="relu",
                    kernel_initializer="he_normal")(inputs)
    # out = GlobalAveragePooling2D()(out)
    midout = Flatten()(midout)
    midout = Dense(100, activation="relu",
                   kernel_initializer="he_normal")(midout)
    out = Dense(classes)(midout)

    if session is not None:
        K.set_session(session)
    model = Model(inputs=inputs, outputs=out)
    model.compile(Adam(lr=1e-4), loss="binary_crossentropy",
                  metrics=["accuracy"])
    return(model)
