import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')

X = df.drop(['trestbps', 'fbs', 'restecg', 'exang', 'oldpeak', 'slope', 'thal', 'target'], axis=1)
y = df.target

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=14)

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'min_samples_leaf': [1, 3, 5]
}

# Create the grid search object
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5, n_jobs=-1)

# Fit the grid search object to the data
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_

rf_model = RandomForestClassifier(**best_params)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)


train_acc = rf_model.score(X_train, y_train)
print('===================================================')
print('Training accuracy:', train_acc)
print('===================================================')
print('Testing Accuracy : ',accuracy_score(y_test,y_pred)*100,"%")
print('===================================================')
print(scaler.mean_)
print(scaler.scale_)
print('===================================================')
aCt=scaler.transform(pd.DataFrame([[50,0,0,254,159,0]],columns=['age','sex','cp','chol','thalach','ca']))
print(aCt)
print('===================================================')
print(rf_model.predict(aCt))

from joblib import dump
dump(rf_model, 'heart_rf.joblib')
dump(scaler,'scaler.joblib')

