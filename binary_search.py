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


