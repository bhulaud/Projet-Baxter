import os, sys

def analyseMetrics():

  with open("metrics.txt",'r') as f:
  
    lines = f.readlines()
    
    with open("results.tap",'w') as resultFile :
      
      if float(lines[0]) > 0.3:
      
        line = "1..2 \nok 1 - MOTA \nnot ok 2 - MOTP # TODO: not written yet"

      else:
      
        line = "1..2 \nnot ok 1 - MOTA \nnot ok 2 - MOTP # TODO: not written yet"

      resultFile.writelines(line)
      
analyseMetrics()
