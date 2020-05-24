import cv2
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

model = tf.keras.models.load_model("detect_number.model")

root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, 'images')
nums = []
for img in os.listdir(path):
    print(img)
    img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
    new_img = cv2.resize(img_arr, (28,28))
    float_img = np.float32(new_img)
    for i,row in enumerate(float_img):
        for j,val in enumerate(row):
            float_img[i][j] = 255-val

    nums.append(float_img)

print(np.shape(nums))
predictions = model.predict([nums])
for p in predictions:
    print(np.argmax(predictions[0]))

