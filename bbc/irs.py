import os
import numpy as np

# Finding and opeing folder for news
num = 0
while(True):
    if(os.path.exists("news"+str(num)) == True):
        os.chdir("news" + str(num))
        break
    num += 1
num = 0

# Getting number of files
nof = next(os.walk(os.getcwd()))[2]
numOfFiles = len(nof)
print(str(numOfFiles) + " files found!")

# Finding total and unique words
words = []
w = []
i = 0
while (i < numOfFiles):
    fileName = "file"+str(i) + ".txt"
    f = open(fileName, 'r')
    line = f.read()
    splitLine = line.split()
    for eachWord in splitLine:
        w.append(eachWord)
        if eachWord not in words:
            words.append(eachWord)
    f.close()
    i += 1

numOfWords = len(words)
print("Total words"+str(len(w)))
print("Unique words " + str(numOfWords))
print(words)

# Zeros matrix
tdm = np.zeros((numOfFiles, numOfWords))
print(tdm.shape)

r = wordIndex = 0

# Creating term document matrix tdm
i = 0
while (i < numOfFiles):
    fileName = "file"+str(i) + ".txt"
    f = open(fileName, 'r')
    line = f.read()
    splitLine = line.split()
    f.close()
    for eachWord in splitLine:
        if eachWord in words:
            wordIndex = words.index(eachWord)
            tdm[r][wordIndex] = 1
    r += 1
    i += 1

# Printing tdm
print(tdm, end=' ')

# Getting input to search in files
inp = input("\nEnter your string: ")
splitLine = inp.split()

# Finding query in files
inpt = np.zeros((1, numOfWords))
for eachWord in splitLine:
    if eachWord in words:
        index = words.index(eachWord)
        inpt[0][index] = 1

# Taking dot product to find maximum similar texts in files
result = 0
arr = []
for row in tdm:
    result = np.dot(inpt, row)
    arr.append(result)

# Finding indexes for similar searches to get file names
i = 0
ind = []
pref = []
for item in arr:
    if int(item) > 0:
        ind.append(i)
        pref.append(int(item))
    i += 1

# Sorting the search results
i = 0
fin = []
while i < len(ind):
    maximum = max(pref)
    num = pref.index(maximum)
    fin.append(ind[num])
    pref[num] = -1
    i += 1

print("\n\nYour query matches " + str(len(ind)) +
      " results in the following order.....: \n")
for all in fin:
    f = open("file"+str(all)+".txt", 'r')
    print(f.read(), end='\n\n')
