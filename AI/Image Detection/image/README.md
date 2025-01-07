This project is a basic image classification system using Convolutional Neural Networks (CNNs). It classifies images into two categories: trucks and cars.
Directory Structure
Image Classification/
data/
truck/
a_truck.jpeg
a_truck_standing_on_the_hightway.jpeg
car/
a_car.jpeg
a_car_standing_on_the_hill.jpeg
data_loader.py
model.py
train.py
evaluate.py
predict.py
utils.py
requirements.txt
README.md
Files
data_loader.py: Loads and preprocesses image data.
model.py: Defines the CNN model architecture.
train.py: Trains the model using the training data.
evaluate.py: Evaluates the model's performance on the test data.
predict.py: Makes predictions on new, unseen images.
utils.py: Utility functions for image normalization.
requirements.txt: Lists dependencies required to run the project.
Requirements
TensorFlow 2.x
Keras 2.x
OpenCV 4.x
NumPy 1.20.x
Scikit-learn 1.0.x
Usage
Install dependencies: pip install -r requirements.txt
Train the model: python train.py
Evaluate the model: python evaluate.py
Make predictions: python predict.py --image_path='data/truck/a_truck.jpeg'
Model Architecture
The CNN model consists of:
Conv2D layers with max pooling
Flatten layer
Dense layers with ReLU activation
Dropout layer for regularization
Softmax output layer
Dataset
The dataset consists of 4 images:
2 truck images
2 car images
License
This project is licensed under the MIT License.
Author
[Your Name]
Acknowledgments
TensorFlow and Keras documentation
OpenCV documentation
NumPy and Scikit-learn documentation

