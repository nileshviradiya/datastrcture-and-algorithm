class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def maxHeap(heap, heapsize, root):
            left = 2*root + 1
            right = left + 1
            larger = root
            if left<heapsize and heap[larger]<heap[left]:
                larger = left
            if right<heapsize and heap[larger]<heap[right]:
                larger = right
            if larger != root:
                heap[larger], heap[root] = heap[root], heap[larger]
                maxHeap(heap,heapsize,larger)
        
        def buildMaxHeap(heap):
            heapSize = len(heap)
            for i in range(heapSize//2-1,-1,-1):
                maxHeap(heap,heapSize,i)
        
        def heapSort(heap,k):
            buildMaxHeap(heap)
            # modify
            for i in range(len(heap)-1,len(heap)-k-1,-1):
                heap[0], heap[i] = heap[i], heap[0]
                maxHeap(heap, i, 0)
            return heap

        
        if len(nums) == 1:
            return nums[0]
        else:
             return heapSort(nums,k)[-k]

s= Solution()
nums=[10,2,6,1,4,7]
k=5
print(s.findKthLargest(nums,k))