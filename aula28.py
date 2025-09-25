nome = input('Digite seu Nome: ')
if not nome:
    print("Você não digitou nada!")
else:
    print(f"Seu nome é {nome}.") 
invertido = print('Seu nome invertido é:',nome [::-1])
espaco = " "
if " " in nome:
    print("Seu nome tem espaço")
else:
    print("Não Contem espaço no seu nome.")

print(f"Seu nome tem {len(nome)} caracteres.")

print("A primeira letra do seu nome é:",nome [0:1:])

print('A Ultima letra do seu nome é:',nome [-1])
