import pandas as pd
from joblib import load
def get_values(age,sex,cp,chol,thalach,ca):
    
    sex=sex
    age=int(age)
    sexM=['Male','MALE','male']
    if sex in sexM:
        sex=1
    else:
        sex=0
    cp=int(cp)
    
    ca=int(ca)
    chol=int(chol)
    thalach=int(thalach)

    scaler = load('scaler.joblib')
    ip=scaler.transform(pd.DataFrame([[age,sex,cp,chol,thalach,ca]],columns=['age','sex','cp','chol','thalach','ca']))

    return ip

def predict(age,sex,cp,chol,thalach,ca):
    
    from joblib import load
   
    model = load('heart_rf.joblib')

    ip=get_values(age,sex,cp,chol,thalach,ca)
     
    prediction=model.predict(ip)

    return prediction
        

    
    
