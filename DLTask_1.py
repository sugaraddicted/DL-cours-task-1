import time
from datetime import timedelta
from array import *
import random
sizes = [8,16,32,64,128, 256, 512, 1024, 2048, 4096]
size_of_hex_num: int = 4 # size of 0x is 4 bits
def GetNumberOfUniKeys():                                                # 1. Простір ключів
  for x in sizes:
     print("Size : ", x, "Number of unique keys : ", 2**x, "or" ,"( 2^",x,")") 

def GetRandomKeys():                                                     # 2. Генерація випадкового значення ключа
 
 for x in sizes:
    key = random.randint(0, pow(2, x))
    print(x,"-bit key",":", hex(key))                        
  
def BruteForceTime(size: int):                                           # 3. Брутфорс функція, що виводить час потрібний для підбору ключа з простору ключів розміру size у мілісекундах 
    start = timedelta(seconds=time.time())

    key = random.randint(0, pow(2, size))
    print(hex(key))
    resultInt = 0

    while True:
        resultInt+=1
        if resultInt == key:
            finish = timedelta(seconds=time.time())
            break
 
    print(hex(resultInt))
    execution_time = finish - start
    print(execution_time.microseconds / 1000)
BruteForceTime(16)
