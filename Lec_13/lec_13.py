#Write a Python program that reads a large text file and counts the occurrences of each word in parallel using both
#multithreading and multiprocessing. Compare the performance of these two approaches.

import time
import random
import threading


#Create a large text file containing random words and sentences. The file should be of sufficient size to demonstrate the benefits of parallel processing.

def write_file(file_name, wordCount):
   file = open(file_name+".txt", "w")

   list1 = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "house", "ice", "jungle",
    "kite", "lemon", "mountain", "notebook", "orange", "pencil", "queen", "river", "sun", "tree",
    "umbrella", "vase", "window", "xylophone", "yogurt", "zebra", "actor", "beach", "candle", "drum",
    "engine", "forest", "garden", "hotel", "island", "jacket", "king", "lake", "mirror", "night",
    "ocean", "picture", "quiet", "rain", "star", "tiger", "uniform", "valley", "water", "yarn",
    "zoo", "arrow", "bridge", "cloud", "dance", "earth", "fire", "gold", "heart", "idea",
    "jewel", "key", "light", "music", "north", "oasis", "peace", "question", "road", "stone",
    "time", "unity", "victory", "world", "yawn", "zest", "angel", "book", "castle", "dream",
    "energy", "freedom", "globe", "hero", "island", "joy", "kindness", "love", "moon", "nature"
]

   for i in range(int(wordCount)):
      file.write(random.choice(list1))
      file.write(" ")
   file.close()

#Implement a function count_words(filename) that reads a text file and returns a dictionary containing word frequencies. Use a simple word tokenization approach (splitting by spaces).

def getWords(file_name):
   file = open(file_name+".txt", "r")
   db = file.read().lower().split()
   file.close()
   return db

def count_words(words, wordsDict, lock):
   
   localWordsDict = {}

   for word in words:
      if word in localWordsDict:
         localWordsDict[word]+=1
      else:
         localWordsDict[word]=1

   #synchronize

   with lock:
        for word, count in localWordsDict.items():
            if word in wordsDict:
               wordsDict[word] += count
            else:
                wordsDict[word] = count

   
def printDict(my_dict):
   for word, count in my_dict.items():
      print(f"{word}: {count}")

#Implement a multithreading version of the word counting function. Divide the file into chunks, and assign each chunk processing to a separate thread. Ensure proper synchronization to update the word frequency dictionary.

def getChunkWordsList(chunkCount,words):
   chunkWordsList = []
   chunk_size = len(words) // chunkCount

   for i in range(chunkCount):
      chunkWordsList.append(words[i*chunk_size:(i+1)*chunk_size])

   return chunkWordsList


if __name__ == "__main__":
    
    #write_file("lec_13_text", 10000000)

    #w/o thread
    words = getWords("lec_13_text")
    
    start= time.time()
    my_dict = {}
    count_words(my_dict, words,threading.Lock())
    printDict(my_dict)
    end= time.time()
    print ("execution Time:"+ str(end-start))

    #thread
    chunkWordsList = getChunkWordsList(4,words)
    start= time.time()

    my_dict = {}
    lock = threading.Lock()
    threads = []

    for words in chunkWordsList:
           thread = threading.Thread(target=count_words, args=(words,my_dict,lock))
           threads.append(thread)
           thread.start()
           #count_words(words, my_dict) 

    for thread in threads:
        thread.join()  

    printDict(my_dict)
    end= time.time()
    print ("execution Time:"+ str(end-start))
   
