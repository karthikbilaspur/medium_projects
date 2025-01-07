from tensorflow.keras.models import load_model
from data_loader import load_data, create_labels

def evaluate_model():
    truck_folder = 'data/truck'
    car_folder = 'data/car'

    truck_images, car_images = load_data(truck_folder, car_folder)
    labels, images = create_labels(truck_images, car_images)

    model = load_model('image_classification_model.h5')
    loss, accuracy = model.evaluate(images, labels)
    print(f'Test accuracy: {accuracy:.2f}%')