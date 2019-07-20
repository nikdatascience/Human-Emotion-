import nltk
import re
from nltk.tag import pos_tag
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber
tb = Blobber(analyzer=NaiveBayesAnalyzer())
k1=tb("abcd")
k1.sentiment.classification
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
from collections import Counter
import time
import pyprind

while True:
    text =input("Enter String")
    y1=""
    sum1 = 0
    aFC = ""
    aFD = ""
    aTD = ""
    aQS = 0
    aQS1 = 0
    aFRB = ""
    aFDT = ''
    aVNS = 0
    aFS = 0
    aAS = 0
    aDS = 0
    aES = 0
    x = ''
    x31=""
    rFirst = ''
    rSecond = ''
    rThrid = ''
    rForth = ''
    rFifth = ''
    rSecondLast = ''
    rLast = ''
    aFN = ""
    aFSD = ""
    text = text.replace("?", "")
    text = text.replace("'", "")
    text = text.replace(":", "")
    text = text.replace(",", "")
    text = text.replace("-", "")
    text = text.replace("_", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace(".", "")
    text = text.replace("\"", "")
    text = text.replace(";", "")
    text = text.strip()
    pbar = pyprind.ProgBar(45)
    start = time.time()
    text=text.lower()
    ts = pos_tag(text.split())
    print(ts)
    u=[word for word, pos in ts if pos== 'MD'] or [word for word, pos in ts if pos== 'VBP'] or[word for word, pos in ts if pos== 'VBD'] #for question cature
    u="".join(u)
    print(u)
    k=[word for word, pos in ts if pos== 'TO']
    k="".join(k)
    print(k)
    dt=[word for word, pos in ts if pos== 'DT'] # for determinant
    if len(dt)!=0:
     aFDT=dt[0]
    j=[word for word, pos in ts if pos== 'JJ'] # for adjective or compliment
    j="".join(j)
    print(j)
    e=[word for word, pos in ts if pos== 'PRP'] or[word for word, pos in ts if pos== 'PRP$'] # for pronoun
    e1=e
    e=" ".join(e)
    print(e)
    q=[word for word, pos in ts if pos== 'IN'] # for infinity
    q = "".join(q)
    print(q)
    f=([word for word, pos in ts if pos== 'NN'] or [word for word, pos in ts if pos== 'NNS'] or [word for word, pos in ts if pos== 'NNP']) # for noun
    if len(f)==2:
      aFN=f[0]
      aFSD=f[1]
    f = " ".join(f)
    print(f)
    g=[word for word, pos in ts if pos== 'VB'] or [word for word, pos in ts if pos== 'VBP'] or [word for word, pos in ts if pos== 'VBD'] or [word for word, pos in ts if pos== 'VBZ'] # for verb
    g1=['has','have','died','die','had']# for negative verb detection in compound sentence
    g3=g
    g2=set(g).intersection(set(g1))
    g2=' '.join(g2)
    g = "".join(g)
    print(g)
    h=[word for word, pos in ts if pos== 'WRB'] or [word for word, pos in ts if pos== 'WP'] or [word for word, pos in ts if pos== 'WDT'] or [word for word, pos in ts if pos== 'WP$'] # Wh type question
    h="".join(h)
    print(h)
    y = [word for word, pos in ts if pos == 'CC'] # for conjunction
    if len(y)==1:
        y1=y[0]
        y1 = "".join(y1)
    print(y1)
    aLR=['not','never','neither','hardly','barely','scarcely','nor','no','rarely','seldom','never','didnt','dont','wont'] # negative adverb
    aLRB=" ".join(aLR)
    z2=[word for word, pos in ts if pos == 'RB'] # for adverb
    if len(z2)>=1:
     aFRB=z2[0]
    z=set(aLR).intersection(set(z2))
    aVRB=set(aLR).intersection(set(g3))
    z=" ".join(z)
    aVRB=" ".join(aVRB)
    print(z)
    blob = tb(text)
    x1 = blob.sentiment.classification # classification labeling of whole sentence into pos or neg
    snt = analyser.polarity_scores(text)['pos']
    if snt >=0:
        x112 = 'pos'
    elif snt < 0:
        x112 = 'neg'
    a = text.split()
    for i in a:
        k = tb(i)
        x1 = k.sentiment.classification
        if x1 == "pos":
            sum1 = sum1 + 1
        else:
            sum1 = sum1 - 1
    print(sum1)
    analysis = TextBlob((text))
    if analysis.sentiment.subjectivity > 0:
        x31="obj"
    r= text.split() # making list text and storing into variable r
    print(r)
    with open('./verb.txt',encoding="utf8") as file: # negative verb words file processing
        aVNS=(sum(word in r for line in file for word in line.split())) # if word in list persent in r then count sum and store in variable
    print(aVNS)
    with open('./fear.txt',encoding="utf8") as file: # fear word file processing
        aFS=(sum(word in r for line in file for word in line.split())) # if word in list persent in r then count sum and store in variable
    print(aFS)
    with open('./exu.txt',encoding="utf8") as file: # anger word file processing
        aAS = (sum(word in r for line in file for word in line.split()))# if word in list persent in r then count sum and store in variable
    print(aAS)
    print(len(r))
    if(len(r))>=1: # condition for not getting empty list error
     rFirst = r[0] # storing first variable of list into new variable
     pattern1=re.compile(r'%s'%rFirst) # making pattern using re
     with open('./exict.txt',encoding="utf8") as file: # excitment words file processing
         s1=[line for line in file if pattern1.match(line)] # if line in file match with pattern then make list
         aES=len(s1) #storing the length of list in a variable
     with open('./qt.txt',encoding="utf8") as file: # question words file processing
         s2=[line for line in file if pattern1.match(line)] # if line in file match with pattern then make list
         aQS=len(s2) #storing the length of list in a variable
     print(aQS)
    if (len(r))>=2: # condition for not getting empty list error
        rSecond=r[1] # storing the sencond variable of list
        rSecondLast=r[-2]  # storing the sencond last variable of list
        rLast=r[-1] # storing the last variable of list
        print(rSecondLast)
        print(rLast)
        pattern=re.compile(r'%s'%rLast) # making pattern using re for last element.
        with open('./out.txt',encoding="utf8") as file: # dieseases words file processing
          s3=[line for line in file if pattern.match(line)]  #if line in file match with pattern then make list
          aDS=len(s3)  #storing the length of list in a variable
        print(aDS)
        pattern2 = re.compile(r'%s'%rSecond) # making pattern using re for last element.
        with open('./qt.txt',encoding="utf8") as file:  # question words file processing
            s4 = [line for line in file if pattern2.match(line)] #if line in file match with pattern then make list
            aQS1 = len(s4)   #storing the length of list in a variable
        print(aQS1)
    if(len(r))==3: # condition for not getting empty list error
        rSecond=r[1] # storing the sencond variable of list
        rThrid=r[2] # storing the thrid variable of list
        aTDS=rFirst + " " + rSecond # Structuring the two words into sentence and storing in variable
        aFC=rFirst + " " + rSecond + " " + rThrid # Structuring the three words into sentence and storing in variable
    elif(len(r))==4: # condition for not getting empty list error
        rSecond = r[1] # storing the sencond variable of list
        rThrid = r[2] # storing the thrid variable of list
        rForth = r[3] # storing the fourth variable of list
        aFD = rFirst + " " + rSecond + " " + rThrid + " " + rForth #Structuring the fourth words into sentence and storing in variable
    elif (len(r))==5: # condition for not getting empty list error
        rSecond = r[1]  # storing the sencond variable of list
        rThrid = r[2] # storing the thrid variable of list
        rForth = r[3] # storing the fourth variable of list
        rFifth = r[4] # storing the fifth variable of list
        aTD = rFirst + " " + rSecond + " " + rThrid + " " + rForth+" "+ rFifth #Structuring the fifth words into sentence and storing in variable
    aNVE= f+" "+g+" "+e # Structure of noun + verb + pronoun                            |
    aPIP= e+" "+q+" "+e # Sturcture of pronoun + infinity + pronoun                     |
    aNIP= f+" "+q+" "+e # Structure of noun + infinity + pronoun                        |
    aNDIP= f+" "+aLRB+" "+q+" "+e #Structure of noun + negation + infinity + pronoun    |---------SVO type Simple Sentence Structuring
    aNIN= aFN+" "+q+" "+aFSD #Structure of noun1 + infinity + noun2                     |
    aNVN= aFN+" "+g+" "+aFSD #Structure of noun1 + verb + noun2                         |
    aiIN= "i"+" "+q+" "+f #Structure of String"i" + infinity + noun                     |
    aiVN="i"+' '+g+" "+f #Structure of String"i" + verb + noun                          |
    aNVIN=aFN+" "+g+" "+q+" "+aFSD #Structure of noun1 + verb + infinity + noun2                    |
    aiVDN="i"+" "+g+" "+aFDT+" "+f #Structure of String"i"+ verb + determinant + noun               |
    aNVDN=aFN+" "+g+" "+aFDT+" "+aFSD #Structure of noun1+ verb + determinant + noun2               |--------SVOO type
    aIVDN=e+" "+g+" "+aFDT+" "+f #Structure of pronoun+ verb + determinant + noun                   |  Simple Structuring
    aNVRIN=aFN+" "+g+" "+z+" "+q+" "+aFSD #Structure of noun1 + verb + negation + infinity +noun2   |
    aNVA = f+" "+g+" "+j # Structure of noun + verb + adjective                    |
    aPVA = e+" "+g+" "+j # Structure of pronoun + verb + adjective
    aNVRA=f+" "+g+" "+z+" "+j # Structure of noun + verb + negation + adjective      |
    aIVRA=e+" "+g+" "+z+" "+j # Structure  of pronoun + verb + negation + adjective  |----------SVC and SVOC type Simple Structuring
    aNIVA=e+" "+f+" "+g+" "+j # Structure of pronoun + noun + verb + adjective       |

    print(pbar.update())
    if rFirst==h: # First word of type Wh question                     |
        if aAS !=0: # Sum of anger word not equal to zero              |
            print("Anger") #                                           |
        else:#                                                         |
           print("Question")#                                          |
    elif rFirst==u: # First word of type question                      |
        if aAS !=0: # Sum of anger word not equal to zero              |
            print("Anger") #                                           |
        else:#                                                         |
           print("Question")  #                                        |
    elif aQS !=0: # First word not equal to zero in question           |--------------Question and Quieries Processing
        print("Question")#                                             |
    elif aQS1 !=0: # Second word not equal to zero in question         |
        print("Question") #                                            |
    elif 'know about' in text: #  String "know about in text"          |
        print("Question")#                                             |
    elif 'about' in text: #  String "know about in text"          |
        print("Question")#                                             |
    elif aES !=0: # Exitment words sum not equal to zero process this loop                                              |
        text1=text.replace(rFirst,'') # Remove First word                                                               |
        blob = tb(text1) #                                                         |
        x121 = blob.sentiment.classification #classification labeling of  sentence removing first word into pos or neg  |
        if x121 is 'pos': #                                                                                             |
            print("Happy") #                                                                                            |
            print("HE21")
        elif x121 is 'neg': #                                                                                           |---Excitment Sentences
            if rLast==aFDT: #                                                                                           |    Processing
                print("Happy") #                                                                                        |
                print("1231") #                                                                                         |
            else:#                                                                                                      |
                 print("SAD")#                                                                                          |
                 print("1230")#                                                                                         |
    elif (rSecond==y1): # if Second word if of conjuntion type then Processing it |
        if x1=='pos': #                                                        |
           if aVNS !=0: #                                                        |
               print("SAD") #                                                    |
           else: #                                                               |
               if x112=='pos':
                 print("Happy")  #                                                |
                 print('211')#                                                    |
               elif x112=='neg':
                 print("SAD")
               else:
                  print("Happy")
                  print("H2S1")
        elif sum1 > 0:
            print("Happy")
            print("H2S2")
        else: #                                                                  |
            if x112=='neg':
              print("SAD") #                                                       |
              print('222') #                                                       |
            else:
              print("Neutral")
              print("H2S3")
    elif (rThrid==y1): # if Second word if of thrid type then Processing it       |
        if x1=='pos': #                                                        |--------Processing Conjuction Sentences which donot
            if aVNS != 0: #                                                      |        comes in Compound Sentence category
                print("SAD") #                                                   |
            else:#                                                               |
                if x112 == 'pos':
                    print("Happy")  # |
                    print('211')  # |
                elif x112 == 'neg':
                    print("SAD")
                else:
                    print("Happy")
        elif sum1 > 0:
            print("Happy")
            print("H2S4")
        else:#                                                                   |
            if x112=='neg':
              print("SAD") #                                                       |
              print('222') #                                                       |
            else:
              print("Neutral")
              print("H2S5")
    elif rSecondLast==y1:# if Second last word if of thrid type then Processing it|
        if x1 is 'pos':#                                                         |
          if aVNS != 0:
           print("SAD")
          else:
              if x112 == 'pos':
                  print("Happy")  # |
                  print('211')  # |
              elif x112 == 'neg':
                  print("SAD")
              else:
                  print("Happy")
                  print("H2S6")
        elif sum1 > 0:
            print("Happy")
            print("H2S7")
        else:#                                                                   |
            if x112=='neg':
              print("SAD") #                                                       |
              print('222') #                                                       |
            else:
              print("Happy")
              print("H2S8")
    elif(e or(f and g)or (rFirst==aFRB)or ( aFDT and f)or (g and k)or (g and z)or(g and q)or (g and aFDT)or (g and f)):
        if len(y)==1:#
            ti=time.time()#                                                                                 |
            a,b = text.split(y1) #  Spliting into two simple sentence                                        |
            blob = tb(a)#classification labeling ofsentence 1st word   |
            blob1 = tb(b)#classification labeling ofsentence 1st word  |
            x11 = blob.sentiment.classification #                                                           |
            x2 = blob1.sentiment.classification #                                                           |
            print((time.time()-ti)," Printing textblob time")#                                              |
            if(x11=='neg' and x2=='pos'): #                                                                 |
                if rLast in g2: #Sentence is incomplete                                                     |
                  print("SAD") #                                                                            |
                  print('101') #                                                                            |
                elif rLast == aFDT:#Sentence is incomplete                                                  |
                    print("SAD") #                                                                          |
                    print("1221") #                                                                         |
                else: #                                                                                     |
                    print("Happy") #                                                                        |
                    print("104") #                                                                          |
            elif(x11=='pos' and x2=='neg'): #                                                               |
                if rLast in g2: #                                                                           |
                    print("Happy") #                                                                        |
                    print("105")   #                                                                        |
                elif rLast == aFDT: #Sentence is incomplete                                                 |
                    print("Happy") #                                                                        |
                    print("1222") #                                                                         |----Processing of
                else: #                                                                                     |    Compound Setence
                  print("Sad")#                                                                             |
                  print("108")#                                                                             |
            elif(x11=='neg' and x2=='neg'):#                                                                |
                if rLast in g2: #                                                                           |
                    print("Happy") #                                                                        |
                    print("109") #                                                                          |
                elif rLast == aFDT:#Sentence is incomplete                                                  |
                    print("Happy") #                                                                        |
                    print("1223") #                                                                         |
                else:#                                                                                      |
                    print("Sad")#                                                                           |
                    print("112")#                                                                           |
            elif (x11 == 'pos' and x2 == 'pos'):#                                                           |
                if rLast in g2:#                                                                            |
                  print("SAD") #                                                                            |
                elif rLast == aFDT: #Sentence is incomplete                                                 |
                    print("Happy")#                                                                         |
                    print("1224")#                                                                          |
                else: #                                                                                     |
                    print("Neutral") #                                                                      |
        elif (not y)or len(y)>=2:    #                                                                            | Processing non Compound Sentence
            if aFC==aPIP:  #                                                      |
                if aVNS !=0:#                                                     |
                    print("Neutral")#                                             |
                    print("4")#                                                   |
                elif aAS !=0:#                                                    |
                    print("Neutral") #                                            |
                    print("5")       #                                            |
                elif rLast == aFDT:  #                                            |
                    print("Neutral") #                                            |
                    print("1221")    #                                            |
                else:                #                                            |
                   print("Neutral")  #                                            |
                   print("6")        #                                            |
            elif aFC==aNVE:          #                                            |
                if aDS !=0:          #                                            |
                   if sum1 > 0:
                     print("Happy")
                     print("H2S10")
                   else:
                    print("SAD")     #                                            |
                    print("8")       #                                            |
                elif rLast == aFDT:  #                                            |
                    print("Neutral") #                                            |
                    print("1221")    #                                            |
                else:                #                                            |
                   print("Happy")    #                                            |
                   print("9")        #                                            |
            elif aFC==aNIP:          #                                            |
                if aVNS !=0 :        #                                            |
                    print("Neutral") #                                            |
                    print("10")      #                                            |
                elif rLast == aFDT:  #                                            |
                    print("Neutral") #                                            |
                    print("1221")    #                                            |...... Processing Simple Sentence of type SVO
                elif aDS !=0:        #                                            |       and SVOO
                    print("Neutral") #                                            |
                    print("11")      #                                            |
                else:                #                                            |
                   print("Neutral")  #                                            |
                   print("12")       #                                            |
            elif aFC==aNVN:          #                                            |
                if aFS != 0:         #                                            |
                    print("Fear")    #                                            |
                elif aDS !=0:        #                                            |
                    if sum1 > 0:
                        print("Happy")
                        print("H2S11")
                    else:
                       print("SAD")  #                                            |
                       print("14")   #                                            |
                if aVNS !=0 :        #                                            |
                    print("SAD")     #                                            |
                    print("160")     #                                            |
                elif rLast == aFDT:  #                                            |
                    print("Neutral") #                                            |
                    print("1221")    #                                            |
                else:                #                                            |
                   print("Happy")    #                                            |
                   print("15")       #                                            |
            elif aFC==aNIN:          #                                            |
                if aFS != 0:         #                                            |
                    print("Fear")    #                                            |
                elif aDS != 0:       #                                            |
                    if sum1 > 0:
                        print("Happy")
                        print("H2S12")
                    else:
                      print("SAD")    #                                            |
                      print("881")    #                                            |
                else:                #                                            |
                    print("Neutral") #                                            |
                    print('223')     #                                            |
            elif aFC==aiIN:          #                                            |
                if aFS != 0:         #                                            |
                    print("Fear")    #                                            |
                elif aDS != 0:       #                                            |
                    if sum1 > 0:
                        print("Happy")
                        print("H2S13")
                    else:
                      print("SAD")   #                                            |
                      print("882")   #                                            |
                else:                #                                            |
                    print("Neutral") #                                            |
                    print('224')     #                                            |
            elif aFC==aiVN:          #                                            |
                if aFS != 0:         #                                            |
                    print("Fear")    #                                            |
                    print('1228')    #                                            |
                elif aDS != 0:       #                                            |
                    if sum1 > 0:
                        print("Happy")
                        print("H2S14")
                    else:
                      print("SAD")     #                                            |
                      print("883")     #                                            |
                else:                #                                            |
                  print("Neutral")   #                                            |
                  print('225')       #                                            |
            elif aFD==aNVIN:         #                                            |
                if aFS != 0:         #                                            |
                    print("Fear")    #                                            |
                    print('1128')    #                                            |
                elif aDS != 0:       #                                            |
                    if sum1 > 0:
                        print("Happy")
                        print("H2S15")
                    else:
                      print("SAD")     #                                            |
                      print("884")     #                                            |
                else:                #                                            |
                   print("Neutral")  #                                            |
                   print('226')      #                                            |
            elif aTD==aNVRIN:        #                                            |
                if aFS != 0:         #                                            |
                    print("Neutral") #                                            |
                    print('1028')    #                                            |
                elif aDS != 0:       #                                            |
                    print("Neutral") #                                            |
                    print("885")     #                                            |
                else:                #                                            |
                   print("Neutral")  #                                            |
                   print('227')      #                                            |
            elif aFD==aNVDN or aFD==aIVDN or aFD==aiVDN: #                        |
                if aFS != 0:          #                                           |
                    print("Fear")     #                                           |
                    print("776")      #                                           |
                elif aDS != 0:          #                                           |
                    if sum1 > 0:
                        print("Happy")
                        print("H2S20")
                    else:
                       print("SAD")      #                                           |
                       print("886")      #                                           |
                else:                 #                                           |
                    print("Neutral")  #                                           |
                    print("228")      #                                           |
            elif aFD == aNDIP:        #                                           |
                print("Neutral")      #                                           |
                print('230')          #                                           |
            elif aFC==aNVA or aFC==aPVA:                          #                                    |
                blob = tb(j)                                      #                                    |
                x12 = blob.sentiment.classification               #                                    |
                if z or aVRB:
                    print("Neutral")
                elif (aFS != 0):                                    #                                    |
                    print("Fear")                                 #                                    |
                    print('928')                                  #                                    |
                elif(aAS !=0):                                    #                                    |
                  print("Angry")                                  #                                    |
                elif x12=='pos':                                  #                                    |
                    print("Happy")                                #                                    |....Processing
                    print("16")                                   #                                    |    Simple Sentence
                else:                                             #                                    |     of type
                    print("Sad")                                  #                                    |     SVC and SVOC
                    print("18")                                   #                                    |
            elif aFD==aNVRA or aFD==aIVRA or aFD==aNIVA:          #                                    |
                blob = tb(j)                                      #                                    |
                x12 = blob.sentiment.classification               #                                    |
                if z or aVRB:                                     #                                    |
                    print("Neutral")                              #                                    |
                elif (x12 == "pos"):                              #                                    |
                    print("Neutral")                              #                                    |
                    print('229')                                  #                                    |
                elif (aAS != 0):                                  #                                    |
                    print("Angry")                                #                                    |
                else:                                             #                                    |
                     print("Sad")                                 #                                    |
            elif rFirst in f and rLast in e : #                                                                |
                if z or aVRB :                #                                                                |
                     if aVNS !=0 :            #                                                                |
                         print("Neutral")     #                                                                |
                         print("1")           #                                                                |
                     elif aFS != 0:  # |
                         print("Happy")  # |
                         print('82q')  # |
                     elif aAS !=0:
                        print("Neutral")
                        print("1")
                     else:                    #                                                                |
                          print("Sad")        #                                                                |
                          print("1")          #                                                                |
                elif not z:                   #                                                                |
                    if aVNS !=0 :             #                                                                |
                        print("SAD")          #                                                                |
                    elif aFS != 0:            #                                                                |
                        print("Fear")         #                                                                |
                        print('828')          #                                                                |
                    elif aAS !=0:             #                                                                |
                        print("Anger")        #                                                                |
                    else:                     #                                                                |
                      print("Happy")          #                                                                |
                      print("2")              #                                                                |
                else:                         #                                                                |
                        print("Neutral")      #                                                                |
                        print("3")            #                                                                |
            elif (z or aVRB) :                #                                                                |
              if( x1=='neg'):                 #                                                                |
                  if aVNS !=0:                #                                                                |
                      print("Neutral")        #                                                                |
                      print("19")             #                                                                |
                  elif aDS !=0:               #                                                                |
                      print("Happy")          #                                                                |
                      print("20")             #                                                                |
                  elif aAS !=0:               #                                                                |
                      print("Neutral")        #                                                                |
                      print("aFRB")           #                                                                |....Processing
                  else:                       #                                                                |       of
                      print("SAD")            #                                                                |    Complex Sentence
                      print("21")             #                                                                |
              elif( x1=='pos'):               #                                                                |
                  if aVNS !=0 :               #                                                                |
                      print("Neutral")        #                                                                |
                      print("22")             #                                                                |
                  elif aAS !=0:               #                                                                |
                      print("Neutral")        #                                                                |
                      print("23")             #                                                                |
                  else:                       #                                                                |
                      print("Neutral")        #                                                                |
                      print("24")             #                                                                |
            elif not (z or aVRB):             #                                                                |
              if ( x1=='neg'):                #                                                                |
                  if aFS != 0:                #                                                                |
                      print("Fear")           #                                                                |
                      print('28')             #                                                                |
                  if aAS !=0 :                #                                                                |
                      print("Anger")          #                                                                |
                      print('12111')          #                                                                |
                  else:                       #                                                                |
                     if x112=='pos':
                        print("Neutral")
                     else:
                        print("SAD")
              elif (x1=='pos'):               #                                                                |
                  if aFS !=0:                 #                                                                |
                      print("Fear")           #                                                                |
                      print('28')             #                                                                |
                  elif aDS !=0:               #                                                                |
                      if sum1 > 0:
                          print("Happy")
                      else:
                        print("SAD")             #                                                                |
                        print("26")              #                                                                |
                  elif aAS !=0:
                      print("Anger")
                      print("29")
                  elif aVNS !=0 :             #                                                                |
                     print("Sad")             #                                                                |
                     print("27")              #                                                                |
                  elif "want" in text:
                      print("Neutral")
                      print("2WQ")
                  else:                       #                                                                |
                     if(x112=='pos'):
                       if x31=='obj':
                         print("Happy")          #                                                                |
                         print("28")              #                                                                |
                       else:
                           print("Neutral")
                     elif(x112=='neg'):
                       print("SAD")
                       print("29")
                     else:
                       print("Happy")
                       print("31")
    else:
          print("Keywords") # Default Keywords
    print(pbar.update())
    print(time.time()-start)
