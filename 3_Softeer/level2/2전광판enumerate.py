bulbs = [
        '1110111', #0
        '0010010', #1
        '1011101', #2
        '1011011',
        '0111010',
        '1101011',
        '1101111',
        '1010010',
        '1111111',
        '1111011' #9
    ]

A='00111'
B='00011'

for i in range(5):
       a_on_positions = {idx for idx,val in enumerate(bulbs[int(A[i])]) if val == "1"}
       b_on_positions = {idx for idx,val in enumerate(bulbs[int(B[i])]) if val == "1"}
       
