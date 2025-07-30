import numpy as np

#question1

mult1 = 2
mult2 = np.array([[6,-9,1],
                 [4,24,8]])
ans1 = np.dot(mult1,mult2)
print(ans1)

#question 2

mult1 = np.array([[1,0],[0,1]])
mult2 = mult2 #mult 2 is the same as before, just for the sake of documentation
ans2 = np.dot(mult1, mult2)
print(ans2)

#question 3

mult1 = np.array([[4,3],[3,2]])
mult2 = np.array([[-2,3],[3,-4]])
ans3 = np.dot(mult1, mult2)
print(ans3)