def sum_array(arr):
    #find max and min
    maximum = max(arr)
    minimum = min(arr)
    
    #pull em out
    arr.remove(maximum)
    arr.remove(minimum)
    #return sum
    result = sum(arr)
    print(result)

sum_array([6, 2, 1, 8, 10 ])