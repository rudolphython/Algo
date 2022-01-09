# heap
import heapq

# 1. 기본 힙(최소힙) 만들기
heap = []

heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
heapq.heappush(heap, 15)
heapq.heappush(heap, 88)
heapq.heappush(heap, 45)
heapq.heappush(heap, -1)

print(heap)
# [-1, 8, 1, 88, 45, 15]



# 2. heap 원소 빼기
print(heapq.heappop(heap))
# -1



# 3. 최소힙 만들기(정렬)
make_heap = [5, 8, 9, 1, 3, -1]
heapq.heapify(make_heap)
print(make_heap)
# [-1, 1, 5, 8, 3, 9]



# 4. 최대힙 만들기
heap_sample = [5, 8, 9, 1, 3, -1]
max_heap = []

for number in heap_sample:
    heapq.heappush(max_heap, (-number, number))

print(max_heap)
# [(-9, 9), (-5, 5), (-8, 8), (-1, 1), (-3, 3), (1, -1)]
# 인덱스 1만 추출하면 됨