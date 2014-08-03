import MapReduce
import collections
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    person = record[0]
    friend = record[1]

    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)

def reducer(person, list_of_friends):
    
    existing_relationships = []

    for friend in list_of_friends:
      existing_relationships.append(friend)

    # Since mapped both (friend,person) and (person,friend),
    # those that exist only once in list of existing relationships are asymmetric friends

    asymmetric_friends = [x for x, y in collections.Counter(existing_relationships).items() if y==1]    

    for friend in asymmetric_friends:
      # Only need to emit once. The reducer of the friend will emit
      # the other to ensure symmetry
      mr.emit((person,friend))
      


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  result = open('mr_result.txt','w')
  result.write(mr.execute(inputdata, mapper, reducer))
  result.close()
  

