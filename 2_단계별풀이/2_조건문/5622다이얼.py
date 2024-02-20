import sys

input_string = sys.stdin.readline()
times=[]
for i in range(2,10):
    if i==7 or i==9:
        for _ in range(4):
            times.append(i+1)
    else:
        for _ in range(3):
            times.append(i+1)

