'''
Merge Sort this array: [4, 1, 3, 2, 0, -1, 7, 10, 9, 20]

4, 1, 3, 2, 0 | -1, 7, 10, 9, 20

4, 1, 3 | 2, 0               -1, 7, 10 | 9, 20

4, 1, | 3      2 | 0              -1, 7 | 10            9|20

4 | 1     3       2  0                 -1  | 7       10          9|20

----

//base case is when the element array is one 
'''

def mergeSort(arr, start, end):
  def merge(arr, start, mid, end): 
    temp = []
    i, j, k = start, mid+1, 0

    while(i<=mid and j <=end):
      if arr[i] <= arr[j]:
        temp[k] = arr[i]
        i+=1
        k+=1
      else:
        temp[k] = arr[j]
        k+=1
        j+=1
    
    while (i<=mid):
      temp[k] = arr[i]
      k+=1
      i+=1
    
    while (j<= end):
      temp[k] = arr[j]
      k+=1
      j+=1
    
    # 


  if (start < end):
      mid = start + (end-start) // 2
      
      # left sub half
      mergeSort(arr, start, mid)
      # right sub half
      mergeSort(arr, mid+1, end)
      merge(arr, start, mid, end)
    
  return []



result = mergeSort([4, 1, 3, 2, 0, -1, 7, 10, 9, 20])
print(f"result {result} must be sorted")