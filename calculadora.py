def soma(a,b):
    return a+b


def sub(a,b):
    return a-b


def main():
    a= int(input("Digite um número: "))
    b= int(input("Digite um número: "))
    resultado = soma(a,b)
    resultado2 = sub(a,b)
    print("Resultado eh: ", resultado)
    print("Resultado da subtracao eh: ", resultado2)

main()
