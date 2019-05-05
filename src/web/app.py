import io
import base64
import argparse
import sys
sys.path.append('..')

from flask import Flask, render_template, request, g
from flask_bootstrap import Bootstrap

from PIL import Image
import numpy as np

import chainer
import chainer.links as L
import chainer.functions as F

#from ml.cc_cnn import CCCNN
from cc_cnn import CCCNN
from common import get_labels


def load_model(model_file):
    model = L.Classifier(CCCNN(50))
    chainer.serializers.load_npz(model_file, model, path='updater/model:main/')
    return model


def create_app():
    app = Flask(__name__)
    Bootstrap(app)


    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')


    @app.route('/', methods=['POST'])
    def upload():
        file = request.files['hcc_image']
        image_data = file.read()
        image_text = "data:image/png;base64,{}".format(base64.b64encode(image_data).decode("utf-8"))
        image = Image.open(io.BytesIO(image_data))
        model = load_model(app.config['model'])
        predict = model.predictor(np.asarray(image.convert('RGB')).reshape(1, 3, 64, 64).astype(np.float32)/255)
        return render_template('index.html', image_text=image_text, predict=get_labels('../../images/')[np.argmax(predict.array)])

    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    args = parser.parse_args()
    app = create_app()
    app.config['model'] = args.model
    app.run()

