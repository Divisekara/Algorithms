def bubbleSort(arr): 
    n = len(arr)

    for i in range(n-1):

        swapped = False

        for j in range(0, 4): 

            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True

        if(swapped == False):
            break;

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
  
sorted_arr = bubbleSort(arr)

print (sorted_arr)

# time complexity
# best case : O(n)
# average case : O(n**2)
# worst case : O(n**2)
