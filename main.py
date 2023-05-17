numero = int(input("Digite um número inteiro: "))

if numero <= 0:
    print("Número inválido")
else:
    divisor = 2
    eh_primo = True
    
    if numero == 1:
        eh_primo = False
    else:
     while divisor < numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print("Primo")
    else:
        print("Não primo")
        