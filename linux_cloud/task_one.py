A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]

def solution(A):
    counter = 0
    for x in range(len(A) - 1):
        if x == 0:
            if A[x] == A[x + 1]:
                continue
            else:
                counter += 1
        elif x == (len(A) - 1):
            if (A[x] - 1) == A[x]:
                continue
            else:
                counter += 1
        else:
            pass


    print(counter)


print(solution(A))
