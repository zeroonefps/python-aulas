'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
contador = 0

while contador <= 100:
    contador += 1 #Essa linha controla meu codigo.
    
    if contador == 6:
        print('Nao existe 6.')
        continue
    
    if contador >= 10 and contador <= 27:
        print('Nao vou mostrar o', contador)
        continue
    
    print(contador)
    
    if contador == 40: 
        break
    
print('Acabou')

