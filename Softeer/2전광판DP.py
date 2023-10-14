def solve(A: str,B: str):
    bulbs = [
    '1110111', 
    '0010010', 
    '1011101', 
    '1011011', 
    '0111010',
    '1101011',
    '1101111',
    '1010010',
    '1111111',
    '1111011'
    ]

    A = A.zfill(5)
    B = B.zfill(5)

    dp = [[0]*len(bulbs[0]) for _ in range(len(A))]

    for i in range(len(A)):
       a_on_positions = {idx for idx,val in enumerate(bulbs[int(A[i])]) if val == "1"}
       b_on_positions = {idx for idx,val in enumerate(bulbs[int(B[i])]) if val == "1"}

       dp[i] += len(a_on_positions.symmetric_difference(b_on_positions))

       if i > 0:
           dp[i] += min(dp[i-1])

    return min(dp[-1])

A=input()
B=input()

print(solve(A,B))
