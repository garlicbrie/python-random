def twoSum(self, numbers, target):
    for i in range(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1

'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

[1, 3, 5, 7, 8, 11, 17], target = 9 // answer  = [2, 4]

  for 0 in 7:
    left = 1
    right = 6
    tmp = 9 - array[0] = 9 - 1 = 8

    while 1 <= 6: 
      mid = 1 + 2 = 3
      
      if 7 < 8 (tmp):
        left = 4
    
    ---
    while 4 <= 6:
      mid = 4 + 1 = 5
      if 11 > 8:
        right = 4

    while 4 <= 4:
      mid = 4 + 0 = 4
      
      8 == target:
        return [1, 5]

'''                


6BF15DB668762B0DFFDC58CF8792CF9D