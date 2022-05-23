'''
decimal to binary is 
keep diving the decimal by 2 and collect all of its remainders in reverse order 

for example, 58 is 111010

58 // 2 = 29 remainder 0
29 // 2 = 14 remainder 1
14 // 2 = 7  remainder 0
7 // 2 = 3   remainder 1
3 // 2 = 1   remainder 1
1 // 2 = 0   remainder 1

we can do this recursively
'''

def convertToBinary(integer):
  # base case
  if integer == 0:
    return ""
  
  # as the previous call stack is getting resolved
  # the resolved values are appended
  return convertToBinary(integer // 2) + str(integer % 2)

answer = convertToBinary(58)
print(answer)
  