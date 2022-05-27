
from heapq import *

heap = []
heapify(heap)

'''
heap sorts by the first index of the item if the item is a list
'''
heappush(heap, [1, 3])
heappush(heap, [6, 1])
heappush(heap, [3, 2])
heappush(heap, [4, 6])


print(heap)