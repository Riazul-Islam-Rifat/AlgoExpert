def insertionSort(array):

    for item in range(1,len(array)):
        j = item

        # We will iterate the assumed list
        while j>0 and array[j]<array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
            j-=1

    return array