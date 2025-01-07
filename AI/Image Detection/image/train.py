from sklearn.model_selection import train_test_split
from data_loader import load_data, create_labels
from model import create_model

def train_model():
    truck_folder = 'data/truck'
    car_folder = 'data/car'

    truck_images, car_images = load_data(truck_folder, car_folder)
    labels, images = create_labels(truck_images, car_images)

    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

    model = create_model()
    model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(test_images, test_labels))

    model.save('image_classification_model.h5')