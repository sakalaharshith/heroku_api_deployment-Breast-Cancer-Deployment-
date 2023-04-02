from fastapi import FastAPI
from pydantic import BaseModel
import pickle as pkl
import json
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins=['*']
app.add_middleware(
CORSMiddleware, 
allow_origins=origins,
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*']
)

class model_input(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean:   float
    concave_points_mean: float
    symmetry_mean : float
    fractal_dimension_mean: float
    radius_se:  float
    texture_se: float
    perimeter_se: float
    area_se  :    float
    smoothness_se: float
    compactness_se: float
    concavity_se  : float
    concave_points_se: float
    symmetry_se    :   float
    fractal_dimension_se: float
    radius_worst       :  float
    texture_worst      :  float
    perimeter_worst    :  float
    area_worst         :  float
    smoothness_worst   :  float
    compactness_worst  :  float
    concavity_worst     : float
    concave_points_worst : float
    symmetry_worst       : float
    fractal_dimension_worst: float

model=pkl.load(open('log_regression_model_new.pkl','rb'))

@app.post('/breast_cancer_prediction')
def cancer_prediction(data_input:model_input):
    input_data=data_input.json()
    input_dictionary=json.loads(input_data)
    list_input=[]
    for key,value in input_dictionary.items():
        list_input.append(value)
    prediction=model.predict([list_input])[0]
    print(prediction)
    
    if prediction==0:
        return "The breast cancer is benevolent"
    if prediction==1:
        return "The breast cancer is malignant!!"
if __name__=='__main__':
    uvicorn.run(app) 








