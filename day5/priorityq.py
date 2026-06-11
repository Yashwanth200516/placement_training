import heapq

patients=[]

heapq.heappush(patients,(3,"A"))
heapq.heappush(patients,(1,"B"))
heapq.heappush(patients,(5,"C"))

while patients:
    print(heapq.heappop(patients)[1])