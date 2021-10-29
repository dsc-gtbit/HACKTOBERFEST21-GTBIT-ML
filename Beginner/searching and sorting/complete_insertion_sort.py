def insertion_sort(InputList):
   for i in range(1, len(InputList)):
      j = i-1
      nxt_element = InputList[i]
      
      while j >= 0 and nxt_element < InputList[j]:
            InputList[j + 1] = InputList[j]
            j -= 1
        InputList[j + 1] = nxt_element
    return InputList

    
arr = [5,2,8,6,1]
print(insertion_sort(arr))
# Compare the current element with next one and write the subsequent code to complete insertion sort
