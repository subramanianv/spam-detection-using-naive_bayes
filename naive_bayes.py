import numpy as np
class Naive_bayes:
    def __init__(self,X,y):
          self.X=X
          self.y=Y
          (m,n)=X.shape
          
    def train():
        pTrue=np.sum(y)/m
        p1v=np.ones(n)
        p0v=np.ones(n)
        p1d=2
        p0d=2
        for i in range(0,m):
            if y[i]==1:
               p1v = p1v + X(i,:]
               p1d = p1d + 1
            else
               p0v = p0v + X[i,:];
               p0d = p0d + 1
        p1v = np.log(p1v/p1d)
        p0v = np.log(p0v/p0d)
        self.p1v = p1v
        self.p0v = p0v
    def classify(xv):
        pfalse = 1 - pTrue
        p1 = np.sum(xv*self.p1v) + log(pTrue)
        p2 = np.sum(xv*self.p0v) + log(pfalse)
        if p1>p0:
           return 1
        else:
            return 0

 
        
