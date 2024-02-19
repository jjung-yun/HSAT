import sys

lst2=[]
for _ in range(20):
    lst=list(sys.stdin.readline().split())
    lst2.append(lst)

# for lst in lst2:
#     print(*lst)

score={
    'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,
    'F':0.0
}

total_score=0
weight=0

for i in range(20):
    kjy=float(lst2[i][1])
    if lst2[i][2] == 'P':
        #weight+=kjy
        continue
    else:
        total_score+=kjy*score[lst2[i][2]]
        weight+=kjy

print(total_score/weight)
