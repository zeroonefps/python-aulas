"""
CONSTANTE = "Variáveis" que não vão mudar
muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)      
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # valocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou:
    print('Velocidade carro passou do radar 1')
    
if  carro_multado_radar_1 and velocidade_carro_passou:
        print('Carro multado em radar 1')