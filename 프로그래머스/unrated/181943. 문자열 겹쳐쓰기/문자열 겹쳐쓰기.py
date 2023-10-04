def solution(my_string, overwrite_string, s):
    # Get the length of the overwrite string
    o_len = len(overwrite_string)
    
    # Replace the substring from index s with the overwrite string
    answer = my_string[:s] + overwrite_string + my_string[s+o_len:]
    
    return answer
