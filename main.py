num = int(input("Digite um número inteiro: "))

if num <= 0:
    print("Número inválido")
else:
    primo = True
    i = 2
    while i < num:
        if num % i == 0:
            primo = False
            break
        i += 1
    if primo:
        print("Primo")
    else:
        print("Não primo")
        