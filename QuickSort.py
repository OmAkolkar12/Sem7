import time
import random
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)
    
def rand_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index= random.randint(0,len(arr)-1) 
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i!= pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i!= pivot_index]
    return rand_quick_sort(left) + [pivot] + rand_quick_sort(right)
    
def analyze_quick_sort():
    n = int(input("Enter the number of elements in array : "))
    arr = [int(x) for x in input("enter elements seperated by space : " ).split()]
    
    arr1 = arr.copy()
    start = time.time()
    deterministically_sorted = deterministic_quick_sort(arr1)
    end = time.time()
    deterministic_time = end - start
    
    arr2 = arr.copy()
    start = time.time()
    randomised_sorted = rand_quick_sort(arr2)
    end = time.time()
    rand_time = end - start
    
    print("deterministic quick sort : \n")
    print("Deterministically sorted array : ", deterministically_sorted)
    print("Deterministic time : ", deterministic_time)
    
    
    print("Randomised quick sort : \n")
    print("randomised sorted array : ", randomised_sorted)
    print("Randomised time : ", rand_time)
    
if __name__ == "__main__":
    analyze_quick_sort()
