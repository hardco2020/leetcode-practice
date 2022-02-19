'''
You are given an array representing a row of seats where seats[i] = 1 
represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

'''

from collections import defaultdict


def maxDistToClosest(seats):
    '''
    distance between him and the closest person is max 
    '''
    #calculate all closest person on each empty seat and return max 
    #two pointer 
    #when encounter another sitted node refresh between left-right 
    
    #Time O(n) -> possible O(2n)
    #Space O(n)
    
    
    # left first 1 node right first 0 node
    left,right = 0,0
    
    # max_dis
    max_dis = 0
    
    # distance dic 
    dic = defaultdict(int)
    
    while seats[left]==0:
        left+=1
    n = len(seats)
    while right < n:
        # Pass the sitted node for now 
        #mean it is at more right so distance can be longer or shorter for node 
        if seats[right] == 1 and right > left : 
            #start calculate and update node  
            #left mean empty node right mean new sited node
            left +=1
            while left < right:
                dic[left] = min(dic[left],right-left)
                left+=1
                                    
        # if not sit,start calculate the distance
        dic[right] = abs(right-left)
        
        # add right
        right+=1
    #print(dic)
    return max(dic.values())

seats = [1,0,0,0,1,0,1]
print(maxDistToClosest(seats))