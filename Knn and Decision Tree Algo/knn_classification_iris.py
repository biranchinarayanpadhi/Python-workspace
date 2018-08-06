import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split  

def knn_iris():
    print("KNN algo")
    names=['sepal-length','sepal-width','petal-length','petal-width','Class']
    data_frame=pd.read_csv('IRIS.csv',names=names)
    data_frame.head()
    
    x=data_frame.iloc[:,:-1].values
    y=data_frame.iloc[:,4].values
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=100)  
    
    #Standardize features by removing the mean and scaling to unit variance
    from sklearn.preprocessing import StandardScaler  
    scaler = StandardScaler()  
    scaler.fit(X_train) #compute mean and standard deviation to be used
    
    #perform standardization by centring and scaling
    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test)  
    
    #applying K-neighbors classification
    from sklearn.neighbors import KNeighborsClassifier  
    classifier = KNeighborsClassifier(n_neighbors=5)  
    #Fit the model using X as training data and y as target values
    classifier.fit(X_train, y_train)  
    #prediction on the test data
    y_pred = classifier.predict(X_test)
    
    #evaluating the algorithm
    from sklearn.metrics import classification_report, confusion_matrix  
    print(confusion_matrix(y_test, y_pred))  
    print(classification_report(y_test, y_pred))    
    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, y_pred)*100)


#error = []
#
## Calculating error for K values between 1 and 40
#for i in range(1, 40):  
#    knn = KNeighborsClassifier(n_neighbors=i)
#    knn.fit(X_train, y_train)
#    pred_i = knn.predict(X_test)
#    error.append(np.mean(pred_i != y_test))
#    
#plt.figure(figsize=(6, 6))  
#plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',  
#         markerfacecolor='blue', markersize=10)
#plt.title('Error Rate K Value')  
#plt.xlabel('K Value')  
#plt.ylabel('Mean Error')  
