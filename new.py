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
    x_inb = 0
    y_inb = 0
    for i,row in enumerate(img_arr):
        for j,val in enumerate(row):
            print(val)
            if val > 254:
                x_inb = j
                y_inb = i
                x_out = 36-j
                y_out = 36-i
                break

    print(x_inb, x_out, y_inb, y_out)
    cut_down = [row[y_out:y_inb] for row in img_arr[x_inb:x_out]]
    new_img = cv2.resize(img_arr, (28,28))
    float_img = np.float32(new_img)
    for i,row in enumerate(float_img):
        for j,val in enumerate(row):
            float_img[i][j] = 255-val
    float_img = np.int32(float_img)
    plt.imshow(cut_down, cmap=plt.cm.binary)
    plt.show()
    nums.append(float_img)

# print(np.shape(nums))
print(nums[0])
predictions = model.predict(nums[0])
for p in predictions:
    print(np.argmax(predictions[0]))

