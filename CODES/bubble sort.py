def bubbleSort(arr): 
    n = len(arr) 

    for i in range(n-1): # 7

        #6
        for j in range(0, 4): #5
            #4

            if arr[j] > arr[j+1]: #4
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]  # n = 7
  
bubbleSort(arr) 

print (arr) 

# time complexity
# best case : O(n)
# average case : O(n**2)
# worst case : O(n**2)

