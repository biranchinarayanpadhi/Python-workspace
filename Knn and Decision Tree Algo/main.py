from knn_classification_cgpa import knn_cgpa
from decision_tree_cgpa import decision_tree_cgpa
from knn_classification_iris import knn_iris
from decision_tree_iris import decision_tree_iris

def cgpa():
    knn_cgpa()
    decision_tree_cgpa()

def iris():
    knn_iris()
    decision_tree_iris()
    
if __name__=="__main__":
    print("Results of cgpa dataset:\n")
    cgpa()
    print("\n")
    print("Results of iris dataset:\n")
    iris()
    