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

# Exercicio 3
# Leia do usuário 3 valores inteiros. Encontre o maior e o menor valor entre eles
# imprimindo o resultado encontrado.

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

  
# Exercicio 4
# Leia do usuário 3 valores inteiros. Calcule a media entre eles. Então imprima todos
# os valores menores que a media e todos maiores que a media.

def main():
  a = int(input("Digite n1: "))
  b = int(input("Digite n2: "))
  c = int(input("Digite n3: "))
  print("Os valores são: ", a, " ", b, " ", c)

  media = (a+b+c)/3
  maior = media
  menor = media

 # maior valor
  

  print("O maior valor é ", maior, "e o menor é ", menor)

if __name__ == "__main__":
    main()

---chatgpt====
def main():
    # Leitura dos 3 valores inteiros
    valores = []
    for i in range(3):
        valores.append(int(input(f"Digite o valor {i+1}: ")))

    # Calculando a média
    media = sum(valores) / len(valores)

    # Imprimindo a média
    print(f"A média é: {media:.2f}")

    # Criando listas para os valores menores e maiores que a média
    menores = []
    maiores = []

    # Separando os valores menores e maiores que a média
    for valor in valores:
        if valor < media:
            menores.append(valor)
        elif valor > media:
            maiores.append(valor)

    # Exibindo os resultados
    print(f"Valores menores que a média: {menores}")
    print(f"Valores maiores que a média: {maiores}")

if __name__ == "__main__":
    main()


# Exercicio 5
# Leia do usuario 1 valor inteiro. Imprima a tabuada deste numero (de 1 a 10).
