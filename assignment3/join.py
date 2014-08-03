import MapReduce
import sys

"""
Relational join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # item_type: order or line item
    # item_id: order_id
    item_type = record[0]
    item_id = record[1]          
    
    mr.emit_intermediate(item_id, record)

def reducer(key, list_of_values):    

    single_record = []
    list_record = []

    order_item = []

    for v in list_of_values:           
        
      if v[0]=='order':
        order_item = v

      if 'order' not in single_record:
        single_record += order_item

      if v[0]=='line_item':
        single_record += v

      if 'order' in single_record and 'line_item' in single_record:
        mr.emit(single_record)
        single_record = []
      
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  result = open('mr_result.txt','w')
  result.write(mr.execute(inputdata, mapper, reducer))
  result.close()
  

