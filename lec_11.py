
import random
import time

#Create a file that will contain 100 lines, each line will contain  20 random  numbers. 

file_name = "lab_text"

def write_file_100_random_lines():
   file = open(file_name+".txt", "w")

   for i in range(100):
      for j in range(20):

         file.write(str(random.randint(0,100)))
         file.write(" ")
      file.write("\n")
   file.close()

      
def read_file_and_split():
   file = open(file_name+".txt", "r")
   listOfFilteredArrInt = []
   for i in range(100):
      #Read all the file lines and using map function convert the line into integer array.
      strLine = file.readline()
      arrInt = list(map(int,strLine.split()))
      #Using filter function filter the numbers which are > 40 
      filteredArrInt = list(filter(lambda x: x>40,arrInt))
      listOfFilteredArrInt.append(filteredArrInt)

   file.close()  
   #Write the data back to file
   file = open(file_name+".txt", "w")
   for i in range(len(listOfFilteredArrInt)):
      for j in range(len(listOfFilteredArrInt[i])):
         file.write(str(listOfFilteredArrInt[i][j]))
         file.write(" ")
      file.write("\n")
   file.close()

#Read the same file as a generetor(use yield to achieve that)
   
def decorator_time(func):
   def wrapper(*args, **kwargs):
      start= time.time()
      print ("start:"+ str(start))

      result =func(*args, **kwargs)

      end= time.time()
      print ("end:"+ str(end))

      print ("execution Time:"+ str(end-start))
      return result
   return wrapper


@decorator_time 
def i_read_file_as_generator():
   file = open(file_name+".txt", "r")
   for i in range(100):
      strLine = file.readline()
      arrInt = list(map(int,strLine.split()))
      for number in arrInt:
         yield number



#time_read_file_as_generator=decorator_time(i_read_file_as_generator)


      
if __name__=="__main__":

   write_file_100_random_lines()
   read_file_and_split()
   
   read_file_as_generator = i_read_file_as_generator()
   for i in read_file_as_generator:
      #print(i)
      pass
      
