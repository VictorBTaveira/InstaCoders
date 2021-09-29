def mergesort(_list, begin=0, end=None):
    if end is None:
        end = len(_list)

    lengh = end - begin
    if lengh > 1:
        middle = begin + lengh // 2
        
        mergesort(_list, begin, middle)
        mergesort(_list, middle, end)

        merge(_list, begin, middle, end)

    return _list

def merge(_list, begin, middle, end):
    leftSide = _list[begin:middle]
    rightSide = _list[middle:end]

    i = 0
    j = 0

    for index in range(begin, end):
        if j == end - middle:
            _list[index] = leftSide[i]
            i += 1
        elif i == middle - begin:
            _list[index] = rightSide[j]
            j += 1
        elif leftSide[i] <= rightSide[j]:
            _list[index] = leftSide[i]
            i += 1
        else:
            _list[index] = rightSide[j]
            j += 1
        
def quicksort(_list, begin=0, end=None):
    if end is None:
        end = len(_list) - 1

    if (end - begin) > 0:
        index = partition(_list, begin, end)
        quicksort(_list, begin, index-1)
        quicksort(_list, index+1, end)
    return _list

def partition(_list, begin, end):
    sep = begin
    pivot = _list[end]
    for i in range(begin, end):
        if _list[i] < pivot:
            _list[i], _list[sep] = _list[sep], _list[i]
            sep += 1
    _list[sep], _list[end] = _list[end], _list[sep]
    return sep

def mySort(_list, alg=None):
    if alg == "mergesort":
        return mergesort(_list)
    return quicksort(_list)