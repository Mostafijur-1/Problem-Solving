numbers = input().split()

N1 = float(numbers[0])
N2 = float(numbers[1])
N3 = float(numbers[2])
N4 = float(numbers[3])


avg = (N1*2 + N2*3 + N3*4 + N4*1)/(2+3+4+1)

print(f'Media: {avg:.1f}')
if(avg >= 7.0):
    print("Aluno aprovado.")
elif(avg < 5.0):
    print("Aluno reprovado.") 
elif(5.0<=avg <= 6.9):
    print("Aluno em exame.")
    N5 = float(input())
    print(f'Nota do exame: {N5:.1f}')
    if(avg >= 5.0):
       print("Aluno aprovado.") 
    elif(avg <= 4.9):
       print("Aluno reprovado.")   
    print(f'Media final: {(avg+N5)/2:.1f}')           