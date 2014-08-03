import MapReduce
import sys

"""
Multiply 2 matrices
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]

    if matrix=='a':
      for k in range(0,5):        
        mr.emit_intermediate((row,k),(matrix,col,value))
        #print ((row,k),(matrix,col,value))

    if matrix=='b':
      for k in range(0,5):
        mr.emit_intermediate((k,col),(matrix,row,value))        
        #print ((k,col),(matrix,row,value))

def reducer(key, list_of_values):    
    
    #print key
    total = 0    

    to_sum = {}
    for v in list_of_values:
      to_sum[(v[0],v[1])] = v[2]
    
    for j in range(0,5):
      if ('a',j) in to_sum and ('b',j) in to_sum:
        total += to_sum[('a',j)]*to_sum[('b',j)]
    
    # Return tuple to prevent submission error
    to_emit = (key[0],key[1],total)

    mr.emit(to_emit)    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  result = open('mr_result.txt','w')
  result.write(mr.execute(inputdata, mapper, reducer))
  result.close()
  

