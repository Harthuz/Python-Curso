velocidade = 100 #mudar a velocidade
local = 100 #mudar o local para passar pelo radar

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_passou_pelo_radar = local >= LOCAL_1
carro_esta_dentro_do_range = local >= (LOCAL_1 - RADAR_RANGE) and local <= (LOCAL_1 + RADAR_RANGE)
carro_esta_acima_da_velocidade = velocidade > RADAR_1

print(f'Você está no quilometro {local}')

if carro_passou_pelo_radar:
    print('Você passou pelo radar 1')
else:
    print('Você naõ passou pelo radar 1')

if carro_esta_dentro_do_range and carro_esta_acima_da_velocidade:
    print('Você foi multado no radar 1')