#import BeautifulSoup
from stemming.porter2 import stem
from sets import Set
import re
import string
from os import listdir
from os.path import isfile, join
stopwords=[line.strip() for line in open('stopwords.txt')]
mypath='TRAINING'
files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
#print onlyfiles
wordlist=Set()
for j in range(0,len(files)):
 f=open(mypath+'/'+files[j],'r')
 lines=[]
 for line in f:
    lines.append(line)
 f.close()
 delete = ""
 i=1
 while (i<0x20):
    delete += chr(i)
    i=i+1
 l=[s.translate(None,delete) for s in lines]
 cleanr =re.compile('<.*?>')
 cleantext = [re.sub(cleanr,'', raw_html) for raw_html in l];
 #print cleantext
 #print "======="
 t=[]
 for i in range(0,len(cleantext)):
    my='';
    for s in cleantext[i]:
        if s.isalpha():
            my=my+s;
        else:
            my=my+" ";
    t.append(my)
 strs=[p.strip().lower() for p in t if len(p)>0 and len(p)<12]
 #print strs 
 #print "===="
 words=[x for s in strs for x in s.split()]
 cleanwords=[word for word in words if word not in stopwords and len(word)>3]
 #print cleanwords
 #apply stemming
 stemmed_words=[stem(word) for word in cleanwords]
 print "s"+str(j)
 wordlist|=Set(stemmed_words)
 
#print len(wordlist)
print (wordlist)
print len(wordlist)
 
 

