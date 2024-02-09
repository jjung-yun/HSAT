import sys

T=int(sys.stdin.readline())
results=[]
for _ in range(T):
    number, word = sys.stdin.readline().split()
    result=''
    for i in word:
        result+=i*int(number)
        #results.append(''.join(i*int(number))) # join 앞에 글자는 구분기호임. ''인 경우 구분기호 없이 출력
    results.append(result)
print(*results, sep='\n')