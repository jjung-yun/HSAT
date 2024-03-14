def recursion(word,left,right,cnt):
    # 왼쪽 인덱스가 오른쪽 인덱스와 같을 땐 홀수길이 단어를, 크면 짝수길이 단어를 모두 확인한 것이니 palindrome이다.
    if left>=right:
        return 1, cnt
    # 왼쪽과 오른쪽이 다르면 아님.
    elif word[left]!=word[right]:
        return 0, cnt
    # 팰린드롬이고 인덱스 확인할게 있다면 계속확인하기.
    else:
        return recursion(word,left+1,right-1,cnt+1) #함수가 돌 때 마다 횟수 1증가.

def isPalindrome(word):
    ans,cnt=recursion(word,0,len(word)-1,1) # 함수가 도는 순간 1회 체크
    return ans,cnt

for _ in range(int(input())):
    a,c=isPalindrome(input())
    print(a,c)