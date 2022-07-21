def solution(s, n):
    ans = ''
    for x in s:
        ord_x = ord(x)
        move_x = ord_x + n
        
        if x == ' ':
            ans += x
            continue
        
        if 65 <= ord_x <= 90:     # A~Z > 65~90 
            st, end = 65, 90
        elif 97 <= ord_x <= 122:  # a~z > 97~122
            st, end = 97, 122
            
        move_x = move_x if move_x <= end else move_x - end+st-1
        ans += chr(move_x)
    return ans
