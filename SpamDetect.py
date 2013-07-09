#import StringUtility from StringUtility
import numpy as np
from stemming.porter2 import stem
from StringUtility import StringUtility
#import Naive_bayes from naive_bayes
import sys
import getopt

if __name__ == "__main__":
    stopwords=[line.strip() for line in open('stopwords.txt')]
    if len(sys.argv)==1 or len(sys.argv)>2:
       print "Usage:python SpamDetect.py <filename>"
    else:
        lines=[line.strip() for line in open(sys.argv[1])]
        l=StringUtility.removeEscapeCharacters(lines)
        cleantext = StringUtility.strip_html_tags(l)
        t=StringUtility.non_alpha(cleantext)
        strs=[p.strip() for p in t if len(p)>0]
        words=[x.lower() for s in strs for x in s.split()]
        cleanwords=[word for word in words if word not in stopwords and len(word)>3 and len(word) < 12]
        stemmed_words=[stem(word) for word in cleanwords]
        print stemmed_words
        
