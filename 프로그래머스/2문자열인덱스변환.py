ans='kjy'
a=ans.replace('j','2')
print(a, ans)

print('oxoxoxoxox'.replace('ox', '*'))
print('oxoxoxoxox'.replace('ox', '*', 2))

def solution(my_string, overwrite_string, s):
    answer = my_string.replace(my_string[s:len(overwrite_string)+s],overwrite_string)
    return answer

#뤼튼 정답코드 : 슬라이싱(slicing) 기능과 문자열 결합(concatenation)을 사용하여 원하는 결과
def solution(my_string, overwrite_string, s):
    # Get the length of the overwrite string
    o_len = len(overwrite_string)
    
    # Replace the substring from index s with the overwrite string
    answer = my_string[:s] + overwrite_string + my_string[s+o_len:]
    
    return answer