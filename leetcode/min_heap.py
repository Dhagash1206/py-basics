import heapq

def kth_smallest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

    for _ in range(k - 1):
        heapq.heappop(min_heap)

    return heapq.heappop(min_heap)



import heapq

def kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]