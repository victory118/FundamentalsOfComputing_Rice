def Mystery(A, l, r):
    if l > r:
        return -1
    
    m = int((l + r)/2)

    if A[m] == m:
        return m
    else:
        if A[m] < m:
            return Mystery(A, m+1, r)
        else:
            return Mystery(A, l, m-1)

print(Mystery([-2,0,1,3,7,12,15],0,6))
print(Mystery(range(5),0,4))
print(Mystery([3,2,1,0],0,3))
print(Mystery([0,2,3,1],0,3))
print(Mystery([3,2,1,3],0,3))
print(Mystery([1,2,1,3],0,3))
print(Mystery([1,2,3,1],0,3))
print(Mystery([1,0,2,3],0,3))
