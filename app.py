from fastapi import FastAPI
import uvicorn
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
   
if __name__ == "__main__":
    uvicorn.run(app, debug=True)
    

    
    