from fastapi import FastAPI
from components.neural_network import make_prediction
from components.image_preprocessing import preprocess_image
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    image: str

@app.post("/predict")
def predict(image: Image):
    
    image = image.image
    image = preprocess_image(image)
    return make_prediction(image)
   

    

    
    