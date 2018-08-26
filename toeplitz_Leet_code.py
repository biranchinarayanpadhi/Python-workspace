import numpy as np
arr=np.array([1,2,3,4,5,1,2,3,9,5,1,2])
matrix=arr.reshape(3,4)
matrix.shape[0]
class Solution:
    def isToeplitzMatrix(self,matrix):
        boolean=True
        for row in range(len(matrix)):
            if row==0:
                for column in range(len(matrix[0])):
                    val=matrix[row][column]
                    m=row
                    n=column
                    while(m<len(matrix)-1 and n<len(matrix[0])-1):
                        m+=1
                        n+=1
        #                print(m,n)
                        if val==matrix[m][n]:
                            continue
                        else:
                            boolean=False
        #                    print("Not a toeplitz matrix")
            else:
             j=0
             val=matrix[row][j]
             m=row
             n=j
             while(m<len(matrix)-1 and n<len(matrix[0])-1):
                m+=1
                n+=1
                if val==matrix[m][n]:
                    continue
                else:
                    boolean=False
        #            print("not a toeplitz matrix")
        
        return boolean