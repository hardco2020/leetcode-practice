'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

https://leetcode.com/problems/trapping-rain-water/
'''

'''
def trap(self, height: List[int]) -> int:
    n = len(height)
    ans,current = 0,0
    stack = []
    while current < n:
        #print(stack,ans)
        while stack and height[current] > height[stack[-1]]:
            top = stack[-1] #2
            stack.pop() 
            if not stack:
                break
            distance = current - stack[-1] - 1 #3-1-1 = 1
            bounded_height = min(height[current],height[stack[-1]]) - height[top] #4 - 2 
            
            ans += distance * bounded_height
            #print(distance,bounded_height)
        stack.append(current)
        current+=1
    return ans
'''

'''
def trap(self, height: List[int]) -> int:
    #Two pointer
    #Time O(n)
    #Space O(1)
    n = len(height)
    left,right = 0,n-1
    left_max,right_max = height[left],height[right]
    res = 0
    while left < right:
        #Decide left_max and right_max of the current
        if height[left] > left_max: 
            left_max = height[left]
        if height[right] > right_max:
            right_max = height[right]
            
        #if left_max < right_max mean cur_left is bounded by left_max bar vis versa
        if left_max < right_max:
            res+= max(0,left_max-height[left])
            left+=1
        else:
            res+= max(0,right_max-height[right])
            right-=1
    return res
'''
def trap(height) -> int:
    # Time O(N)
    # Space O(N)
    
    # find left_max and right_max for each position 
    n = len(height)
    left_max = [ 0 for _ in range(n)]   
    right_max = [ 0 for _ in range(n)]   
    
    #initalize leftmost and rightmost 
    left_max[0] = height[0]
    right_max[-1] = height[-1]        
    res = 0
    
    # calculate left_max and right_max
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],height[i])
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],height[i])
    
    print(left_max,right_max)
    for i in range(1,n-1): # leftmost and rightmost can't count
        res += min(left_max[i],right_max[i]) - height[i]
        #print(res)
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))