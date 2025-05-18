def matches_template(a,s):
    if len(a) != len(s):
        return False
    
    num_to_char = {}
    char_to_num = {}
    
    for num,char in zip(a,s):
        if num not in num_to_char:
            num_to_char[num] = char
        elif num_to_char[num] != char:
            return False
        if char not in char_to_num:
            char_to_num[char] = num
        elif char_to_num[char] != num:
            return False                    
    return True    


t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    
    for _ in range(m):
        s = input().strip()
        if matches_template(a,s):
            print("YES")
        else:
            print("NO")    
            
      