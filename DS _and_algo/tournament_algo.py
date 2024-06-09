def tournament_two(A):
    """Returns the two largest number of an arrays"""
    N = len(A)
    winner = [None] * (N-1)
    looser = [None] * (N-1)
    prior = [-1] * (N-1)
    idx = 0
    for i in range(0,N,2):
        if A[i] < A[i+1]:
           winner[idx] = A[i+1]
           looser[idx] = A[i]
        else:
           winner[idx] = A[i]
           looser[idx] = A[i+1]
        idx+=1
        m = 0
    while idx < N-1:
        if winner[m] < winner[m+1]:
           winner[idx] = winner[m+1]
           looser[idx] = winner[m]
           prior[idx] = m+1
        else:
           winner[idx] = winner[m]
           looser[idx] = winner[m+1]
           prior[idx] = m
        m+=2
        idx+=1
    largest = winner[m]
    second = looser[m]
    m = prior[m]
    while m>=0:
        if second < looser[m]:
            second = looser[m]
        m = prior[m]
    return (largest,second)

print(tournament_two([32,23,45,67,54,23,76,98]))