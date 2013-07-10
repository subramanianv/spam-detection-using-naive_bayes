import numpy as np
from scipy.sparse import *
from scipy import *
import pickle
class Naive_bayes:
    def __init__(self,X,y=None):
         print type(X)
         if isinstance(X,basestring) and y is None:
             Params=pickle.load(open(X,"rb"))
             self.pTrue=Params['pTrue']
             self.p1v=Params['p1v']
             self.p0v=Params['p0v']  
             print "Initialized"      
         else: 
              self.X=X
              self.y=y
              (self.m,self.n)=X.shape
    
    """ 
    def __init__(self,filename):
        params=pickle.load(open(filename,'rb'))
        self.p1v=params['p1v']
        self.p0v=params['p0v']
    """
 
    def train(self):
        
        self.pTrue=float(np.sum(self.y))/self.m
        p1v=np.ones(self.n)
        p0v=np.ones(self.n)
        p1d=2
        p0d=2
        for i in range(0,self.m):
            print 'Training',i
            if self.y[i]==1:
               p1v = p1v + self.X.getrow(i)
               p1d = p1d + np.sum(self.X.getrow(i).todense())
            else:
               p0v = p0v + self.X.getrow(i);
               p0d = p0d + np.sum(self.X.getrow(i).todense())
        p1v = np.log(p1v/p1d)
        p0v = np.log(p0v/p0d)
        self.p1v = p1v
        self.p0v = p0v
    def classify(self,xv):
        self.pfalse = 1 - self.pTrue
        #print "false",self.pfalse;
        #print xv.shape,self.p1v.shape,self.p0v.shape
        #print type(xv),type(self.p1v)
        p1 = np.dot(xv,np.asarray(self.p1v).reshape(-1))# + log(self.pTrue)
        p0 = np.dot(xv,np.asarray(self.p0v).reshape(-1))# + log(self.pfalse)
        print p1,p0
        if p1>p0:
           return 1
        else:
            return 0
        
    def saveParams(self):
        print "Saving params"
        params={}
        params['p1v']=self.p1v;
        params['p0v']=self.p0v;
        params['pTrue']=self.pTrue;
        pickle.dump(params,open('params.p','wb'))
                
 

 
        
