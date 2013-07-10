#import BeautifulSoup
import numpy as np
from naive_bayes import Naive_bayes
from scipy.sparse import lil_matrix
from StringUtility import StringUtility

#from sample import sample
from stemming.porter2 import stem
from sets import Set
import string
from os import listdir
from os.path import isfile, join
import pickle
"""
def WordsToVector(wordlist,email):
   returnVec=[0]*len(wordlist)
   for word in email:
       if word in wordlist:
          returnVec[wordlist.index(word)]=1
   
   return returnVec

"""

stopwords=[line.strip() for line in open('stopwords.txt')]
mypath='TRAINING'
files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
#print onlyfiles
wordlist=Set()
emails=[]
for j in range(0,len(files)):
#for j in range(0,1):
 lines = open(mypath+'/'+files[0]).read().splitlines()
 l=StringUtility.removeEscapeCharacters(lines)
 cleantext = StringUtility.strip_html_tags(l) #strip html tags
 #print cleantext
 #print "====step 1======="   
 # removes all the non-alphabet characters
 t=StringUtility.non_alpha(cleantext)
 strs=[p.strip() for p in t if len(p)>0] #strips the space
 
 #print strs 
 #print "======="
 words=[x.lower() for s in strs for x in s.split()] #converts to lowercase and converts lists of words into one single word
 #print words
 cleanwords=[word for word in words if word not in stopwords and len(word)>3 and len(word) < 12] #removes all the words that are less than 3 and greater than 12
 #print cleanwords
 #apply stemming
 stemmed_words=[stem(word) for word in cleanwords] # stem the word
 emails.append(stemmed_words)
 print "Training Document "+str(j)
 wordlist|=Set(stemmed_words) 

 
print len(files),len(wordlist) 
X=lil_matrix((len(files),len(wordlist)))
wl=len(wordlist);
for i in range(0,len(files)):
    print i,"s"
    X[i,0:wl]=StringUtility.WordsToVector(list(wordlist),emails[i]);

X=X.tocsr()
print type(X)
o=open('SPAMTrain.label')
y=[int(line[0]) for line in o];
qp=[];
for i in range(0,len(files)):
    qp.append(y[i])

y=np.array(qp)
classifier = Naive_bayes(X,y)
classifier.train()
classifier.saveParams()
pickle.dump(list(wordlist),open("wordlist.p","wb"))
#print classifier.classify(qp1)
