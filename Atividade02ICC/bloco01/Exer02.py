anoNasc = eval(input("Informe o ano de nascimento: "))
idade = 2021 - anoNasc

if (idade >= 18 and idade <= 67):
    print(idade, "anos. Pode doar sangue!")
else:
    print(idade, "anos. Não pode doar sangue!")