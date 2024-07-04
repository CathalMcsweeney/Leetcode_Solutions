n = 25
#power = [5,0,0,3,1,5,3,4,3,2,4,2,0,7]
weight = [8, 5, 4, 7, 2]

def findMaximumBalancedShipments(weight):
    # Write your code here
    ans = 0
    for parcels in range(len(weight)):
        print(weight[parcels])

        for other_weight in weight[parcels + 1:]:

            if weight[parcels] <= other_weight:
                
                break
        #if weight[parcels] > weight[parcels +1]:
        
    return ans

print(findMaximumBalancedShipments(weight))

def makePowerNonDecreasing(power):
    # Write your code here
    Ascending = False
    ans = 0
    while not Ascending: 
        Ascending = True
        for num in range(len(power)-1):
       
            if power[num] > power[num+1]:
                
                #get difference
                toadd = power[num] - power[num+1]
                # subarray to be added to
                #for i in range(num+1, len(power)):
                power[num] += ans

                Ascending = False
                ans += toadd

    return(ans)

print(findMaximumBalancedShipments(weight))

def fizzbuzz(n):
    # Write your code here
    for i in range(n):
        if i == 0:
            continue
        if not (i % 3 == 0 or i % 5 == 0):
            print(i)  
        elif i % 3 == 0 and i % 5 != 0:
            print("fizz") 
        elif i % 3 != 0 and i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz") 
        else:
            print("uh-oh")

