# recursively
str = "flipme"

def reverseString(string):
  if not string:
    return ""
  
  return reverseString(string[1:]) + string[0]

result = reverseString(str)
print(result)