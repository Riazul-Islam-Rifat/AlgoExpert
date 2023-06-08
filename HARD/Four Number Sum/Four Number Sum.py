def fourNumberSum(array, targetSum):
    pairSum = {}
    quadruplets = []

    for i in range(1,len(array)-1):

        for j in range(i+1,len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum

            if diff in pairSum:
                for pair in pairSum[diff]:
                    quadruplets.append(pair+[ array[i] , array[j]])

        # This loop is used so that we don't create same quadruplets more than once with different variation
        for k in range(0,i):
            currentSum = array[i] + array[k]

            if currentSum not in pairSum:
                pairSum[currentSum] = [[array[i] , array[k]]]

            else:
                pairSum[currentSum].append([array[i] , array[k]])

    return quadruplets
