'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

https://leetcode.com/problems/kth-largest-element-in-an-array/
'''

import heapq

'''
def findKthLargest(self, nums: List[int], k: int) -> int:
    # Quick Select 
    # seperate left and right 
    # we want to right to be k so we can return the firstone on the right
    
    #1. find a random nums to be the one to seperate
    #2. after that return the left and right nums 
    #3. if right is more than 4 mean we have to do it on right 
    #4. other wise we have to do it on left 
    
    n = len(nums)
    
    def divide(left,right,anchor):# [3,2,1,5,6,4]   [3,2,1,4,5,6,]
        # start divide
        target = nums[anchor]
        # move pivot to end 
        nums[anchor],nums[right] = nums[right],nums[anchor]
        
        left_pointer = left
        for i in range(left,right):
            if nums[i] < target:
                nums[left_pointer],nums[i] = nums[i],nums[left_pointer]
                left_pointer+=1
        nums[right],nums[left_pointer] = nums[left_pointer],nums[right]
        return left_pointer
    def quick_select(left,right,k):
        # if the list contains only one element 
        if left == right:
            return nums[left]
        # pick a random number for seperate 
        anchor = random.randint(left,right)
        
        # return the divided position
        position = divide(left,right,anchor)
        
        #ex:  3 < 4   mean the position have to be righter
        if position < k: 
            return quick_select(position+1,right,k)
        #ex: 9-3-1 > 4  mean the position have to be lefter
        elif position> k:
            return quick_select(left,position-1,k)
        return nums[position] 
    
    return quick_select(0,n-1,len(nums)-k)
'''

def findKthLargest(nums, k: int) -> int:    
    # Heap 
    # K largest
    heap = []
    
    # Time O(NlogK) N-> len(nums) K-> k
    # Space O(k)
    for num in nums:
        # keep the size to be k 
        if len(heap) < k: 
            heapq.heappush(heap,num)
        else:
            # check if insert num is bigger than the k largest 
            pop_num = heapq.heappop(heap) 
            if num > pop_num:
                heapq.heappush(heap,num)
            else:
                heapq.heappush(heap,pop_num)
    return heapq.heappop(heap)


print(findKthLargest([3,2,1,5,6,4],2))