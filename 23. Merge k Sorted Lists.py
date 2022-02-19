'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

https://leetcode.com/problems/merge-k-sorted-lists/
'''
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
def mergeKLists(self, lists): 
    # merge 2 list 
    # merge log k time 
    def merge2Lists(list1,list2):
        head = cur = ListNode(0)
        while list1 and list2:
            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")
            
            #compare val
            if val1 < val2:
                cur.next = ListNode(val1)
                cur = cur.next
                list1 = list1.next if list1 else None
            else:
                cur.next = ListNode(val2)
                cur = cur.next
                list2 = list2.next if list2 else None
        # append the rest 
        if list1:
            cur.next = list1 
        if list2:
            cur.next = list2 
        return head.next
    amount = len(lists)
    interval = 1 
    while interval < amount:
        for i in range(0,amount-interval,interval*2):
            lists[i] = merge2Lists(lists[i],lists[i+interval])
        interval*=2
    return lists[0] if amount > 0 else None
'''
def mergeKLists(lists): 
    # Time O(nlogk) -> k the number of lists n-> number of nodes
    # Space O(k) -> heap space 
      
    #answer 
    head = point = ListNode(0)
    
    #making a heap queue
    queue = []
    for l in lists:
        if l:
            heapq.heappush(queue,(l.val,id(l),l))
        
    #start to pop 
    while queue:
        val,nodeId,node = heapq.heappop(queue)
        # point the smallest val to answer
        point.next = ListNode(val)
        point = point.next
        
        # put the rest back to the queue
        node = node.next
        if node:
            heapq.heappush(queue,(node.val,id(node),node))
    return head.next

def ListNodeMaker(list):
    head = cur = ListNode(0)
    for num in list:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next

def PrintListNode(list):
    nums = []
    while list:
        nums.append(list.val)
        list = list.next
    print(nums)

lists = []
lists.append(ListNodeMaker([1,4,5]))
lists.append(ListNodeMaker([1,3,4]))
lists.append(ListNodeMaker([2,6]))

PrintListNode(mergeKLists(lists))
