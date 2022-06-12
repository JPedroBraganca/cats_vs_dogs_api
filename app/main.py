from fastapi import FastAPI
from components.neural_network import make_prediction
from components.image_preprocessing import preprocess_image
from pydantic import BaseModel
#import uvicorn

app = FastAPI()

class Image(BaseModel):
    image: str

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post("/predict")
def predict(image: Image):
    
    image = image.image
    image = preprocess_image(image)
    return make_prediction(image)

#if __name__ == '__main__':
#    uvicorn.run(app,
#            host='127.0.0.1',
#            port=8000
#           )   