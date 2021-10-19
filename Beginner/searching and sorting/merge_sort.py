from sys import stdin

def merge(arr1, n, arr2, m) :
    i=0
    j=0
    len1=len(arr1)
    len2=len(arr2)
    arr=[]
    while((i<len1)and(j<len2)):
        if (arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i=i+1
        else:
            arr.append(arr2[j])
            j=j+1
    while(i<len1):
        arr.append(arr1[i])
        i=i+1
    while(j<len2):
        arr.append(arr2[j])
        j=j+1
    return arr
    #Your code goes here
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0
#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()

#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
