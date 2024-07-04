arr = [10,95,37,33,19,92,94,16,2,18,50]


def minimizeCost(arr):
    # Write your code here
    total_cost = 0
    #arr.sort()

    while len(arr) > 1:
        arr.sort()
        first = arr.pop(0)
        second = arr.pop(0)

        cost = first + second
        total_cost += cost
        
        if len(arr)>2:
            first = arr.pop(0)
            second = arr.pop(0)
            cost2 = first + second
            total_cost += cost2
            arr.append(cost2)

        arr.append(cost)
        
        

    return total_cost

# def minimizeCost2(arr):
#     from sortedcontainers import SortedList
#     total_cost = 0
#     sorted_list = SortedList(arr)  # Initialize sorted list
    
#     while len(sorted_list) > 1:
#         # Get the two smallest elements
#         first = sorted_list.pop(0)
#         second = sorted_list.pop(0)
        
#         # Calculate the cost of merging these two elements
#         cost = first + second
#         total_cost += cost
        
#         # Insert the result back into the sorted list
#         sorted_list.add(cost)
    
#     return total_cost

print(minimizeCost(arr))