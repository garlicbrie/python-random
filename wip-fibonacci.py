'''
fibonnaci sequence example:

              8th fibonacci number
                     v    
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...

the next value is addition of previous two values
'''

# recursive solution
def recursiveFib(index) -> int:
  # base case
  if index == 0 or index == 1:
    return index
  else: 
    return recursiveFib(index-1) + recursiveFib(index-2)

# while loop
def whileFib(index):
  n1, n2 = 0, 1
  count = 2

  nth = 0
  
  if index == 0:
    return n1
  elif index == 1:
    return n2
  else:
    while count < index:
      nth = n1+n2
      n1 = n2
      n2 = nth
      count += 1
      
  return nth


# recursiveRes = recursiveFib(8)
# print(f"recursive: fibonacci number at index 8 is {recursiveRes}")

whileRes = whileFib(8)
print(f"while: fibonacci number at index 8 is {whileRes}")