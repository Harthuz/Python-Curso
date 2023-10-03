velocidade = 60 #mudar a velocidade
local = 100 #mudar o local para passar pelo radar

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Você passou pelo radar 1')

if local >= (LOCAL_1 - RADAR_RANGE) and local <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Você foi multado no radar 1')