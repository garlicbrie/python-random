
test_list = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]
  
# printing original list 
print ("The original list is : " + str(test_list))

#lambda param: return statement  
test_list.sort(key = lambda list: list[1])
  
# printing result
print ("List after sorting by 2nd element of lists : " + str(test_list))