import heapq

'''
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
    #Time Sorting cost O(nlogn)
    #Space O(n)
    
    #seperate start_time and end_time and sort in order
    start_times = sorted([time[0] for time in intervals])
    end_times = sorted([time[1] for time in intervals])
    
    #define pointer
    start_pointer,end_pointer = 0,0
    
    #define return 
    max_using_room = 0
    using_room = 0
    
    [0, 5,15]    #15
    [10,20,30]    
    #until start_pointer reach the end 
    while start_pointer < len(intervals):
        #mean meeting can start after the ending , so we can release the room
        if start_times[start_pointer] >= end_times[end_pointer]:
            using_room-=1
            end_pointer+=1
        
        #either way we move start_pointer ahead and start a new room
        start_pointer+=1
        using_room+=1
        
        #compare 
        max_using_room = max(max_using_room,using_room)
    
    return max_using_room    
'''

def minMeetingRooms(intervals) -> int:
    #[[0,30],[5,10],[15,20],[16,23],[24,30],[32,34],[50,60],[51,55],[52,56],[53,55]]
    #2,4 7,10
    pass
    '''
    if the time begin is > then the smallest ending time 
    then mean there's room 
    else input the time end to it 
    5,30
    '''
    # Time ONlogN
    # Space ON
    
    # return answer 
    max_using_room = 1
    
    # sort the array base on begin time 
    intervals.sort(key=lambda x:x[0])
    
    # start to put time into heap
    heap = []
    for begin,end in intervals:
        #if there's no room,like first one,directly input
        if not heap:
            heapq.heappush(heap,end)
            continue

        #decide if there's empty room in the beginning time
        #pop the first available time
        first_available = heapq.heappop(heap)
        
        #if begin time is bigger or equal than first_available, mean it's available
        #otherwise we input the unavailable room back and add new room
        if begin < first_available:
            heapq.heappush(heap,first_available)
        heapq.heappush(heap,end)
        
        #determine max_using_room 
        max_using_room = max(max_using_room,len(heap))
        #print(heap)
    return max_using_room


print(minMeetingRooms([[0,30],[5,10],[15,20],[16,23],[24,30],[32,34],[50,60],[51,55],[52,56],[53,55]]))