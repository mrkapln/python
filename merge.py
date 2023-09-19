def sort(A):
    if len(A) <= 1:
        return A
    midt = len(A) // 2
    left = sort(A[:midt])
    right = sort(A[midt:])
    return Merge(left, right, A)


def Merge(left, right, A):
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[i+j] = left[i]
            i +=1 
        else:
            A[i+j] = right[j]
            j += 1
    while i < len(left):
        A[i+j] = left[i]
        i = i +1
    while j < len(right):
        A[i+j] = right[j]
        j += 1
    return A