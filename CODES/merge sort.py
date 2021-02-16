def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2 # Finding the mid of the array
 
        L = arr[:mid] ##Left side
 
        R = arr[mid:] ##Right Side
 
        mergeSort(L) # Sorting the first half
 
        mergeSort(R) # Sorting the second half
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L): # Checking if any element was left in left side
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R): # Checking if any element was left in right side
            arr[k] = R[j]
            j += 1
            k += 1
 
 
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)