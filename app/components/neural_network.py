import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

class_names = ['CAT', 'DOG']

def load_model():

    path = "./app/models/cats_vs_dogs_transfer_learning.h5"
    load = tf.keras.models.load_model(path, custom_objects={"KerasLayer": hub.KerasLayer})
    return load

model = load_model()

def make_prediction(image):

    global model
    
    if model is None:
        model = load_model()
    
    predicted = model.predict(image).tolist()[0]
    predicted_label = np.argmax(predicted)

    prob_cat = round(predicted[0], 2)
    prob_dog = 1 - prob_cat
    pred_class = class_names[predicted_label]
    
    data = {"prob_cat": prob_cat,
            "prob_dog": prob_dog,
            "predicted_class": pred_class}
    
    return data