def solve(A: str,B: str):
    bulbs = [
        '1110111', #0
        '0010010', #1
        '1011101', #2
        '1011011',
        '0111010',
        '1101011',
        '1101111',
        '1110010', #7 이 생긴게 이상했음.
        '1111111',
        '1111011', #9
        "XXXXX"
    ]

    A = A.rjust(5, "X")
    B = B.rjust(5, "X")

    total_difference = 0
    
    for i in range(len(A)):
       a_on_positions = {idx for idx,val in enumerate(bulbs[int(A[i]) if A[i].isdigit() else -1]) if val == "1"}
       b_on_positions = {idx for idx,val in enumerate(bulbs[int(B[i]) if B[i].isdigit() else -1]) if val == "1"}
       
       total_difference += len(a_on_positions.symmetric_difference(b_on_positions))
           
    return total_difference

N=int(input())
result=[]

for _ in range(N):
    a,b=input().split()
    result.append(solve(a,b))
    
print(*result, sep='\n')
