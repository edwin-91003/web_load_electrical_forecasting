import uvicorn
from fastapi import FastAPI
from load import Load
import numpy as np
import pickle
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


app=FastAPI()
pickle_in=open("model.pkl","rb")
# Model=pickle.load(pickle_in)
model=load_model("my_model.h5")

@app.get('/')
def index():
    return {'message':'Hello '}

@app.post('/predict')
def predict_load(data:Load):
    data=data.dict()
    T1=data['T1']
    # print(T1)
    T2=data['T2']
    # print(T2)
    T3=data['T3']
    # print(T3)
    T4=data['T4']
    # print(T4)
    T24=data['T24']
    # print(T24)
    T48=data['T48']
    # print(T48)
    T72=data['T72']
    # print(T72)
    T96=data['T96']
    # print(T96)
    DAY=data['DAY']
    # print(DAY)
    SEASON=data['SEASON']
    # print(SEASON)
    TEMP=data['TEMP']
    # print(TEMP)
    HUMIDITY=data['HUMIDITY']
    # print(HUMIDITY)
    #print(model.predict([[T1,T2,T3,T4,T24,T48,T72,T96,DAY,SEASON,TEMP,HUMIDITY]]))
    # print("Hello")
    ms=MinMaxScaler()
    test = pd.read_csv("dataset.csv").drop(columns=["Unnamed: 0","T"])
    ms=ms.fit(np.array(test))
    data=ms.transform([[T1,T2,T3,T4,T24,T48,T72,T96,DAY,SEASON,TEMP,HUMIDITY]])
    prediction=model.predict(data)
    # min_load=test.min()
    # # print(min_load)
    # max_load=test.max()
    # print(max_load)
    # print(ms.inverse_transform(prediction))
    print(prediction)
    return {"prediction":float(prediction[0])*10000-1000}


if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
    

     

    

 