# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar 
# númerose underline_.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'Heverton De Oliveira Silva'
soma_dois_mais_dois = 2 + 2
int_um = bool('1') #Aqui acontece uma pratica contraria de clean code, eu uso o nome "int_um" mas ela é uma bool.
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois) # Aparece meu Nome!

nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)