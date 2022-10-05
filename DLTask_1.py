import time
from datetime import timedelta
import secrets
from array import *

sizes = array('i', [8,16,32,64,128, 256, 512, 1024, 2048, 4096])

def GetNumberOfUniKeys():                                                # 1. Простір ключів
  for x in sizes:
     print("Size : ", x, "Number of unique keys : ", 2**x, "( 2^",x,")") 

def GetRandomKeys():                                                     # 2. Генерація випадкового значення ключа
 
    
 for x in sizes:
    print(x,"-bit key",":",secrets.token_hex(x))                        
  
def BruteForceTime(size):                                                # 3. Брутфорс функція, що виводить час потрібний для підбору ключа розміру size
    t_start = time.time()

    key = secrets.token_hex(size)
    keyInt =int(key, 16)
    resultInt = 0

    while resultInt := resultInt + 1:

      if resultInt == keyInt:

        break

    result = hex(resultInt)

    print(time.time() - t_start)

key = secrets.token_hex(16)
keyInt =int(key, 16)
print(key, ' ',keyInt)