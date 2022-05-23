'''
arr = [0, 1, 2, 5, 7, 8, 9], target = 6 // answer should be 4

left = 0
right = len(arr) - 1 = 6

while left <= right (does this work rather than left <= right):
  midpoint = left + (right-left/2) 
  if arr[midpoint] === target:
    return midpoint
  elif arr[midpoint] < target: 
    left = midpoint + 1
  elif arr[midpoint] > target: 
    right = midpoint - 1

return left

---

left = 0 
right = 6

while 0 <= 6:
  midpoint = 0 + 3 = 3
  5 < 6:
    left = 4

---

left = 4
right = 6

while 4 <= 6: 
  midpoint = 4 + 1 = 5
  8 > 6: 
    right = 4

---
left = 4
right = 4

while 4 <= 4
  midpoint = 4 + 0 = 4
  7 > 6:
    right = 4 - 1


---
left = 4
right = 3
no more. 
  
'''


'''
arr = [0, 3, 5, 6], target = 2 // answer should be 1

left = 0
right = len(arr) - 1 = 3

while left < right (does this work rather than left <= right, NOPE! for this exact case):
  midpoint = left + (right-left/2) 
  if arr[midpoint] === target:
    return midpoint
  elif arr[midpoint] < target: 
    left = midpoint + 1
  elif arr[midpoint] > target: 
    right = midpoint - 1

return left

---

left = 0 
right = 3

while 0 <= 3:
  midpoint = 0 + 1 = 1
  3 > 2:
    right = 1 - 1

---

left = 0
right = 0

while 0 < 0: 
  midpoint = 4 + 1 = 5
  8 > 6: 
    right = 4

---

This would return 0
  
'''

# return the index where the target is or should be in sorted array
# solving it recursively

'''
algorithm is as follows:

left = beginnign of the array
right = end of the array

find the midIndex of an array

if the target is bigger than the value at midIndex, 
  call itself on right half side of the array after the midpoint by updating left
if the target is smaller than the value at midIndex, 
  call itself on left half side of the array before the midpoint by updating right

if the value at midIndex is equal to target:
  return midIndex

return left
'''

def binarySearch(array, target):
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = left + (right-left) // 2
    if target == array[mid]:
      return mid
    elif target > array[mid]:
      left = mid + 1
    elif target < array[mid]:
      right = mid -1
  
  return left

exactMatch = binarySearch([4, 6, 8, 9, 10, 15], 6)
print(f"Exact Match Binary Search, the answer should be 1 and the actual answer is {exactMatch}")

noExactMatch = binarySearch([4, 5, 8, 9, 10, 15], 6)
print(f"No Exact Match Binary Search, the answer should be 2 and the actual answer is {noExactMatch}")


