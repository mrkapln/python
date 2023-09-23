def insertion(A):
    for i in range(1, len(A)):
        verdi = A[i]
        j = i - 1
        while j >= 0 and verdi < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = verdi
    return A
