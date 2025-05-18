import math
def simplify(numerator,denominator):
    gcd = math.gcd(numerator,denominator)
    return numerator // gcd, denominator // gcd
    
def calculate_and_simplify(n1,d1,op,n2,d2):
    if op == '+':
        num = n1*d2 + n2*d1
        den = d1*d2
        
    elif op == '-':
        num = n1*d2 - n2*d1
        den = d1*d2    
    
    elif op == '*':
        num = n1*n2
        den = d1*d2  
    elif op == '/':
        num = n1*d2
        den = n2*d1 
        
    if den<0:
        num = -num  
        den = -den
        
    sim_num,sim_den = simplify(num,den)
    return f"{num}/{den}={sim_num}/{sim_den}"      


n = int(input())
for _ in range(n):
    expr = input().split()
    n1 = int(expr[0])
    d1 = int(expr[2])
    op = expr[3]
    n2 = int(expr[4])
    d2 = int(expr[6])
    
    print(calculate_and_simplify(n1,d1,op,n2,d2))    
    