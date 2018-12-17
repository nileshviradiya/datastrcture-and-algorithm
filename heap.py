from heapq import heapify, heappushpop

def findKthLargest( nums, k):
        heap = nums[:k]
        heapify(heap)
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])
        
        return heap[0]

nums=[10,2,6,1,4,7]
k=3
findKthLargest(nums,k)