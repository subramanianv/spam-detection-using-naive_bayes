import re
import string
class StringUtility:
   
    @staticmethod
    def WordsToVector(wordlist,email):
        returnVec=[0]*len(wordlist)
        for word in email:
            if word in wordlist:
                returnVec[wordlist.index(word)]=1
        return returnVec

    @staticmethod
    def removeEscapeCharacters(lines):
        delete = ""   # removes all the espace characters
        i=1
        while (i<0x20):
            delete += chr(i)
            i=i+1
        l=[s.translate(None,delete) for s in lines]
        return l

    @staticmethod
    def strip_html_tags(lines):
        cleanr=re.compile('<.*?>')
        cleantext=[re.sub(cleanr,'',raw_html) for raw_html in lines]
        return cleantext
    
    @staticmethod
    def non_alpha(lines):
       t=[]
       for k in range(0,len(lines)):
           my='';
           for s in lines[k]:
               if s.isalpha():
               #print s
                   my=my+s;
               else:
                   my=my+' ';
           t.append(my)
       return t


 
