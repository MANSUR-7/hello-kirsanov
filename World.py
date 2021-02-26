# count = 0;  
# word = "";  
# maxCount = 0;  
# words = [];  
   
# #Opens a file in read mode  
# file = open("data-1.txt", "r",-1,'UTF-8')  
      
# #Gets each line till end of file is reached  
# for line in file:  
#     #Splits each line into words  
#     string = line.lower().replace(',','').replace('.','').split(" ");  
#     #Adding all words generated in previous step into words  
#     for s in string:  
#         words.append(s);  
   
# #Determine the most repeated word in a file  
# for i in range(0, len(words)):  
#     count = 1;  
#     #Count each word in the file and store it in variable count  
#     for j in range(i+1, len(words)):  
#         if(words[i] == words[j]):  
#             count = count + 1;  
              
#     #If maxCount is less than count then store value of count in maxCount  
#     #and corresponding word to variable word  
#     if(count > maxCount):  
#         maxCount = count;  
#         word = words[i];  
          
# print("Most repeated word: " + word);  
# file.close();  
   # СЧИТАЕТ НАИБОЛЬШЕ ВСТРЕЧ СЛОВА
# f=open('data-1.txt','r') # cчитываю файл
# line=f.readline().lower()
# s={}
# while line:
#     line=line.split()    
    
#     i1=0
#     i2=''
#     q=0
#     t=[]
#     min1=0
#     for i in line: # ввожу слова в словарь
#         if i not in s: # проверяю есть ли слово в словаре,если есть,то добавляю1 
#             s[i]=1
#         else:
#             s[i]+=1
#     for values in s.values(): # нахожу максимальное повторение
#         if values>i1:
#             i1=values
#     for keys , values in s.items():
#         if values==i1:
#             min1=keys
#     for keys , values in s.items(): # если слова встречаются одинаковое кол-во,
#         if values==i1:              # то находим  лексикографически первое 
#             if min1>keys:
#                 min1=keys
#     print(min1,i1)
#     line=f.readline().lower()
# f.close()

#   #  ЧАСТО встречаются СЛОВА.
# import urllib
# import operator
# txtFile = open('data-2.txt','r').readlines()
# txtFile = " ".join(txtFile) # this with .readlines() replaces new lines with spaces
# txtFile = "".join(char for char in txtFile if char.isalnum() or char.isspace()) # removes everything that's not alphanumeric or spaces.

# word_counter = {}
# for word in txtFile.split(" "): # split in every space.
#     if len(word) > 0 and word != '\r\n':
#         if word not in word_counter: # if 'word' not in word_counter, add it, and set value to 1
#             word_counter[word] = 1
#         else:
#             word_counter[word] += 1 # if 'word' already in word_counter, increment it by 1

# for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse=True)[:10]):
#     # sorts the dict by the values, from top to botton, takes the 10 top items,
#     print ("%s: %s - %s"%(i+1,word,word_counter[word]))


#      #    СРЕДНИЙ БАЛЛ
# with open('math-1.txt') as f:
#     strings = [s.rstrip() for s in f.readlines()]
# otsenki = [s.split(';')[1:] for s in strings]
# for x in otsenki:
#     print(sum(map(int, x))/len(x))
# sr_mat = sum([int(x[0]) for x in otsenki]) / len(otsenki)
# sr_fiz = sum([int(x[1]) for x in otsenki]) / len(otsenki)
# sr_rus = sum([int(x[2]) for x in otsenki]) / len(otsenki)
# print(sr_mat, sr_fiz, sr_rus)

#   #ДЛИНА ОКРУЖНОСТИ
# import math 
# r = float(input())
# p = math.pi*r*2
# print(p)

# import sys
# s = ''
# s2 = ''
# for i in range(1,len(sys.argv)):
#     s = s + sys.argv[i]+' '
# s2 = s
# print(s2,end=' ')

# import sys
# print(' '.join(sys.argv[1:]))