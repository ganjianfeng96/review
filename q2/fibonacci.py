
'''
decription:
    This file implements file content parsing and handling function for the feature.

#Input:File name and the path of the file
#Output: The assigned type num and the total value of all numbers  
#Key Points:
   1. Get content in the file line by line
   2. Get all the numbers in the RegExp
   3. Cal the total value of all numbers

#Todos:
   1.generalize the function
   2.Configuration-based development

# modification history:
# ----------------------------------------------------
# 2016/03/19, Jeff Gan, Create
# 
'''

def fibonacci(n):
    arr_result = []
    #arr_result.append(0)
    #arr_result.append(1)
    #arr_result.append(1)

    if n == 0:
        arr_result.append(0)
        print(arr_result)
        return arr_result
	
    if n == 1:
        arr_result.append(0)
        arr_result.append(1)
        #arr_result.append(1)
        print(arr_result)
        return arr_result
    
    if n == 2:
        arr_result.append(0)
        arr_result.append(1)
        arr_result.append(1)
        print(arr_result)
        return arr_result

    arr_result.append(0)
    arr_result.append(1)
    arr_result.append(1)
    a = 0
    b = 1
    c = 1
    n = n -1
    for i in range(1,n):
        a = b + c
        c = b
        b = a
        arr_result.append(a)
    
    print(arr_result)
    return arr_result


#fibonacci(10)
#fibonacci(8)
#fibonacci(5)
#fibonacci(4)
#fibonacci(1)
#fibonacci(0)
