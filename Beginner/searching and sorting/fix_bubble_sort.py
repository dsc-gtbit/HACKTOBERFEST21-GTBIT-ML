def bubblesort(l):

# Swap the elements to arrange in asc order(Done)
    for iter_num in range(len(l)-1,0,-1):
        for idx in range(iter_num):
            if l[idx]>l[idx+1]:
                temp = l[idx]
                l[idx] = l[idx+1]
                l[idx+1] = temp
l = [19,2,31,45,6,11,121,27]

bubblesort(l)
print(l)
