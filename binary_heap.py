'''
binary heap 
- two children at most
- complete tree (from left to right) except for the last level
'''

'''
will be representing as an array
     0         1            2            3           4              5            6
- [root, level1-left, level1-right, level2-left, level2-right, level2-left, level2-right]

index access logic: (helper function)
parent = (index - 1) // 2 

left = index * 2 + 1
right = index * 2 + 2

- hasParents, hasleftchild, hasrightchild, swap

shift_up (heapify)
- check with its parents value 
    - if parent value is smaller, flip 
    - else leave

sift_down
- check with its children's value
  - swap the element with w/e children's min value if element is smaller than min value

insert
- insert at the end of the array
- while parent index is 0 or bigger
  - sift_up

delete
- replace the first element with the last element of the array
- while either children exists
  - sift_down
'''

class MinHeap: 
  def __init__(self):
      self.heap_list =  []
      self.current_size = 0
    
  def getParentIndex(self, index):
    return (index-1) // 2
  
  def getLeftChildIndex(self, index):
    return index * 2 + 1

  def getLeftChildIndex(self, index):
    return index * 2 + 1  

  def getRightChildIndex(self, index):
    return index * 2 + 2
  
  def hasParent(self, index) -> bool:
    return self.getParentIndex(index) >= 0
  
  def hasLeftChild(self, index):
    return self.getLeftChildIndex(index) < self.current_size

  def hasRightChild(self, index):
    return self.getRightChildIndex(index) < self.current_size

  def swap(self, index1, index2):
    tempIndex1 = self.heap_list[index1]
    self.heap_list[index1] = self.heap_list[index2]
    self.heap_list[index2] = tempIndex1

  def insert(self, value):
    self.heap_list.append(value)
    self.current_size += 1
    self.sift_up()
  
  def sift_up(self):
    currIndex = self.current_size - 1
    while self.hasParent(currIndex):
      parentIndex = self.getParentIndex(currIndex)
      if self.heap_list[parentIndex] > self.heap_list[currIndex]:
        self.swap(parentIndex, currIndex)
        currIndex = parentIndex
      else:
        return
  
  def delete(self):
    if not self.heap_list:
      print("Heap list is empty")
      return

    self.heap_list[0] = self.heap_list[self.current_size-1]
    self.heap_list.pop()
    self.current_size -= 1
    self.sift_down()
  
  def sift_down(self):
    currIndex = 0
    while self.hasLeftChild(currIndex):
      smallerChildIndex = self.getLeftChildIndex(currIndex)
      if (self.hasRightChild(currIndex) and self.heap_list[self.getRightChildIndex(currIndex)] < self.heap_list[smallerChildIndex]):
        smallerChildIndex = self.getRightChildIndex(currIndex)
      
      if self.heap_list[smallerChildIndex] < self.heap_list[currIndex]:
        self.swap(smallerChildIndex, currIndex)
        currIndex = smallerChildIndex
      else:
        return
    
minHeap = MinHeap()
minHeap.insert(2)
minHeap.insert(1)
minHeap.insert(3)
minHeap.insert(4)
minHeap.insert(5)
print(minHeap.heap_list)
minHeap.delete()
print(minHeap.heap_list)
minHeap.delete()
print(minHeap.heap_list)