item, capacity = [int(i) for i in input().split()]              # no of bags and max capacity he can take
mylist = []
if capacity == 0:                                               # agr no capacity so items lene ka faida ni
    print(0)
    quit()
for _ in range(item):                                           #ab jitny items hain utny p value or capacity lo
    value, weight = [int(i) for i in input().split()]
    if value == 0:                                          # if agr kisi ki value zero bhi define kry so no issue keep acceptin
        continue
    mylist.append((value, weight))                          # append in list
mylist.sort(key = lambda index: index[0]/index[1], reverse = True)       #now  list ky jo items hain value/capacity krky jo ans aye ussy sort then reverse
#print(mylist)
total_item = 0
for value,weight in mylist:
    if capacity==0:                         # if i have no capacity then i cant add anything
        print("Sum of above values",total_item)
        quit()                      #terminate
    wrt_capacity = min(weight, capacity)    # choose minimum value comparing to the capacity i have and the capacity i can pick
    #print(wrt_capacity)
    newval=wrt_capacity*value/weight
    print("Value to be choose:",newval)
    total_item += newval
    capacity -= wrt_capacity
print("Sum of above values",total_item)