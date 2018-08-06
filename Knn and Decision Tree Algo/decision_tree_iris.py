import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split  

def decision_tree_iris():
    print("DECIISON_TREE algo")
    names=['sepal-length','sepal-width','petal-length','petal-width','Class']
    data_frame=pd.read_csv('IRIS.csv',names=names)
    data_frame.head()
    x=data_frame.iloc[:,:-1].values
    y=data_frame.iloc[:,4].values
    
    #the datset is divided into training and tsting data set and
    #here the random_state defines not to change the data_frame randomly if run multiple times
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=100)  
    
    from sklearn.preprocessing import StandardScaler  
    scaler = StandardScaler()  
    scaler.fit(X_train) #compute mean and standard deviation to be used
    
    #perform standardization by centring and scaling
    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test)  

    
    #here the decision tree classfier function is used for implemeniting the algo
    from sklearn.tree import DecisionTreeClassifier
    #gini_index= DecisionTreeClassifier(
    #            criterion = "gini", random_state = 80, #here the criterion entropy means information gain else it would be gini
    #            max_depth = 3, min_samples_leaf = 5)
    
    
    info_gain = DecisionTreeClassifier(
                criterion = "gini", random_state=100,#here the criterion entropy means information gain else it would be gini
                max_depth = 3, min_samples_leaf = 5)
    #Fit the model using X as training data and y as target values
    info_gain.fit(X_train,y_train)
    y_pred=info_gain.predict(X_test)
    
    #evaluating the algorithm
    from sklearn.metrics import classification_report, confusion_matrix  
    print(confusion_matrix(y_test, y_pred))  
    print(classification_report(y_test, y_pred))    
    
    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, y_pred)*100)
decision_tree_iris()
