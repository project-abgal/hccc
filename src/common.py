import os


def get_labels(image_path):
    images = os.listdir(image_path)
    images.sort()
    return images
