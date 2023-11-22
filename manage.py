def BSsearch(A, target):
    left = 0
    right = len(A)
    while right > left:
        mid = (left + right)//2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            left = mid+1
        else:
            right = mid

    return -1

print(BSsearch([1, 2, 5, 6, 8, 9], 8))