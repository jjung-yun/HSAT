N=int(input())
#numbers=[int(input()) for _ in range(N)] 
# for 을 통해 바로 리스트로 만드는 법 => 여러줄의 input일 때 유용함.

numbers=list(map(int,input().split()))
print(min(numbers), max(numbers))
