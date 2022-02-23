
import heapq

'''
def mincostToHireWorkers(quality, wage, k: int) -> float:
    n workers 
    quality[i]  => quality
    wage[i] => minimum wage expectation
    
    least money to hire k worker 
    at leat their minimum wage expectation
    paid in the ratio of their quality compare to other
    # make a dict so we can know sort wage so we can apply greedy stratedy 
    # Won't pass N^2logN
    payable_plan = []
    min_pay = float("inf")
    cur_hire = 0
    dic = sorted(zip(wage,quality), key=lambda x:x[0])
    #print(dic)
    N = len(dic)
    pay = 0
    for i in range(N):
        # decide a ratio we gonna use 
        pay = dic[i][0] #  
        ratio = dic[i][0]/dic[i][1]
        cur_hire = 1
        heap = []
        for j in range(N):
            # can't hire the same worker and stop when we find enough worker
            #if cur_hire == k:
            #    payable_plan.append(pay)
            #    break
            if i!=j:
                # mean the salary is more than min expect , so can hire
                if ratio*dic[j][1] >= dic[j][0]:
                    # add money into a heap
                    heapq.heappush(heap,ratio*dic[j][1])
                    #pay+= ratio*dic[j][1]
                    #cur_hire+=1
        if len(heap)>=k-1:
            while cur_hire < k:
                #print(heap)
                #print(pay)
                pop = heapq.heappop(heap)
                pay += pop
                cur_hire+=1
        if cur_hire == k:
            #print(pay)
            min_pay = min(pay,min_pay)
    return(min_pay)  
'''
def mincostToHireWorkers(quality,wage, k: int) -> float:     

    #quality mean people's wage when time ratio , so we have to select people out based on quality,
    #since it will determine wage
    #after that the way to determine order is based on ratio if we pay ratio x then we can afford any person who is ratio <=x happy

    #sort eveything by ratio first
    workers = sorted([(w/q,q,w) for q,w in zip(quality,wage)])
    print(workers)
    heap = []
    sumq = 0
    ans = float("inf")
    # using heap to let go the person who cost most quality 
    for ratio,q,w in workers:
        #input the quality into ratio represent worker
        print(heap,sumq)
        heapq.heappush(heap,-q)
        sumq+=q
        
        if len(heap) > k:
            # sumq will minus the extra q ( cut down worker)
            sumq += heapq.heappop(heap)
        if len(heap) == k:
            ans = min(ans,ratio*sumq)
    return ans  