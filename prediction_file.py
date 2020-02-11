import keras
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from keras.models import load_model
from skimage.transform import resize
import cv2

labels = {"0": "Forest", "1": "River", "2": "Highway", "3": "AnnualCrop", "4": "SeaLake", "5": "HerbaceousVegetation", "6": "Industrial", "7": "Residential", "8": "PermanentCrop", "9": "Pasture"}


model = load_model('/Users/shiqinchoo/Desktop/satellite/sat_rgb.h5', compile = False)


def cv_read(file):
    img = cv2.imread(file)
    img = resize(img, (64,64,3))
    img = np.reshape(img, [1,64,64,3])
    prediction = model.predict(img)
    print(labels[str(prediction.argmax())])