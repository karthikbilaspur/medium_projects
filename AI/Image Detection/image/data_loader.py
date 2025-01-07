import os
import cv2
import numpy as np

def load_data(truck_folder, car_folder):
    truck_images = []
    car_images = []

    for filename in os.listdir(truck_folder):
        img = cv2.imread(os.path.join(truck_folder, filename))
        img = cv2.resize(img, (224, 224))
        truck_images.append(img)

    for filename in os.listdir(car_folder):
        img = cv2.imread(os.path.join(car_folder, filename))
        img = cv2.resize(img, (224, 224))
        car_images.append(img)

    return np.array(truck_images) / 255.0, np.array(car_images) / 255.0

def create_labels(truck_images, car_images):
    truck_labels = np.zeros((len(truck_images),))
    car_labels = np.ones((len(car_images),))

    return np.concatenate((truck_labels, car_labels)), np.concatenate((truck_images, car_images))