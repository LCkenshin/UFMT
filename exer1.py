#Exercicio 1
#

#Exercicio 2
#Escreva 2 n | leia | some,multiplique,divida,subtraia

def main():

a=int(input("Digite o n1: "))
b=int(input("Digite o n2: "))
print("Os valores digitados foram: ",a,b)

soma = a + b
print("A soma dos valores é: ", soma)

mult = a * b
print("A multiplicação dos valores é: ", mult)

sub = a - b
print("A soma dos valores é: ", sub)

div = a / b
print("A soma dos valores é: ", div)

if __name__="__main__":
  main()

#Exercicio 3
#leia 3 valor determine maior menor e igual

def main():
    a = int(input("Digite n1: "))
    b = int(input("Digite n2: "))
    c = int(input("Digite n3: "))
    print("Os valores são: ", a, " ", b, " ", c)

    #maior e menor
    maior = a
    menor = b
    
    # maior valor
    if a > b and a > c:
        maior = a
    elif b > a and b > c:
        maior = b
    else:
        maior = c

    # menor valor
    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    else:
        menor = c

    print("O maior valor é ", maior, "e o menor é ", menor)

if __name__ == "__main__":
    main()

  
#Exercicio 4
#Leia 3 valores e tire a media deles | verifcar qual é o menor e maior numero digitado

def main():

if __name__=="__main__"
  main()
