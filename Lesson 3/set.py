my_set = {1,2,3}

my_set = set([1, 2, 3])

my_set = set()

my_set = {1,2,2,3,3,3}
print(my_set)

set1 = {1,2,3}
set2 = {3,4,5}
union_result_method = set1.union(set2)
union_result_operator = set1 | set2
print("rezultati i 2 seteve", union_result_operator)
print("Union of set1 and set2 using the | operator", union_result_operator)

intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2
print("intersection of set 1 and set2 using interestion method: ", intersection_result_method)
print("intersection of set 1 and set2 using operator method:", intersection_result_operator)

difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print("difference of set 1 and set2 using difference method: ", difference_result_method)
print("difference of set 1 and set2 using operator method:", difference_result_operator)

symmetric_difference_method = set1.symmetric_difference(set2)
symmetric_difference_operator = set1 ^ set2

print("Symetric difference of set1 and set2 using symetric_difference method: ", symmetric_difference_method)
print("Symetric difference of set1 and set2 using difference operator: ", symmetric_difference_operator)

my_set = {1,2,3,}
#add an element to a set
my_set.add(7)


#removing an element from the set
my_set.add(3)

my_set.discard(8)

print(my_set)

my_set.clear()

print(my_set)


