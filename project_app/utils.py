import pandas as pd
import numpy as np
import json
import pickle
import config
import warnings
warnings.filterwarnings('ignore')


class MedicalInsurance():
    def __init__ (self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex =  sex
        self.bmi= bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_'+ region

    def load_model(self):

        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)


        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data=json.load(f)

    def get_prediction(self):

        self.load_model()

        region_index = list(self.json_data['columns']).index(self.region)
        arr = np.zeros(len(self.json_data['columns']))
        arr[0]= self.age
        arr[1]= self.json_data['sex'][self.sex]
        arr[2]= self.bmi
        arr[3]= self.children
        arr[4]= self.json_data['smoker'][self.smoker]
        arr[region_index]=1

        charges=np.around(self.model.predict([arr])[0],2)

        return charges


if __name__=="__main__":
    age = 19
    sex = "female"
    bmi = 27.9
    children = 0.0
    smoker = "yes"
    region = "southwest"


    med_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=med_ins.get_prediction()

    print("Medical Insurance charges will be:",charges,'/-Rs. Only')





     

        