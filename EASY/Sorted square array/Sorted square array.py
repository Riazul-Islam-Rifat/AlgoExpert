def sortedSquaredArray(array):
    output = []

    left_pointer =  0
    right_pointer = len(array)-1

    for item in range(len(array)):
        left_num = abs(array[left_pointer])
        right_num = abs(array[right_pointer])

        if left_num>right_num:
            output.insert(0,left_num*left_num)
            left_pointer+=1

        else:
            output.insert(0,right_num*right_num)
            right_pointer-=1

    return output
