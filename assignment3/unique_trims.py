import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    
    identifier = record[0]
    string = record[1]    

    # Remove last 10 characters as unique key; value is not important
    mr.emit_intermediate(string[:-10], identifier)

def reducer(key, list_of_values):    
    
    # Make use of uniqueness of the keys
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  result = open('mr_result.txt','w')
  result.write(mr.execute(inputdata, mapper, reducer))
  result.close()
  

