def cantor_set(sequence, start, end):
    if end - start < 3: #선의 길이가 3보다 작을 때는 더 이상 나눌 수 없으므로 종료
        return
    segment_length=(end-start)//3
    for i in range(start+segment_length,start+2*segment_length):
        sequence[i]=' ' #가운데 구간을 공백으로 채움.
    
    #재귀적으로 왼쪽, 오른쪽 세그먼트에 같은 과정 수행.
        cantor_set(sequence, start, start+segment_length)
        cantor_set(sequence,start+2*segment_length,end)

def main(N):
    length=3**N #문자열의 길이
    sequence=['-']*length #초기 문자열 생성
    cantor_set(sequence,0,length) #칸토어 집합근사
    print(''.join(sequence)) #결과출력

# sequence = ['안', '녕', '하', '세', '요']일 경우
# print(sequence) = ['안', '녕', '하', '세', '요']를 출력
# print(''.join(sequence))는 구분기호가 없는 값들을 연속적으로 출력


#입력 횟수가 지정되지 않았을 때, try except 구문
while True:
    try:
        N=int(input())
        main(N)
    except:
        break
