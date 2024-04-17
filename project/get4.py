import pandas as pd
from joblib import load
def get_values(age,glucose,bp,skinTh,insulin,bmi):
    
    
    age=int(age)
    
    glucose=int(glucose)
    
    bp=int(bp)
    skinTh=int(skinTh)
    insulin=int(float(insulin))
    bmi=float(bmi)

    scaler = load('scaler4.joblib')
    ip=scaler.transform(pd.DataFrame([[glucose,bp,skinTh,insulin,bmi,age]],columns=['Glucose','BloodPressure','SkinThickness','Insulin','BMI','Age']))

    return ip

def predict(age,glucose,bp,skinTh,insulin,bmi):
    
    
   
    model = load('diabetes.joblib')

    ip=get_values(age,glucose,bp,skinTh,insulin,bmi)
     
    prediction=model.predict(ip)

    return prediction
        

    
    
