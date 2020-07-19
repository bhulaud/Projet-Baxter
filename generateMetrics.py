import os, sys
import random

def generateRandomMetric():

  with open("metrics.txt",'w') as metricsFile:
    
    randomValue = str(random.random())
    
    print(randomValue)
  
    metricsFile.writelines(randomValue)
    
generateRandomMetric()
