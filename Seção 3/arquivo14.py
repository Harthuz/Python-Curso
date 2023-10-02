velocidade = 100
local = 98 #mudar o local para passar pelo radar

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1 and (local == LOCAL_1 - RADAR_RANGE) or (local == LOCAL_1 + RADAR_RANGE) or (local == LOCAL_1):
    print('Você foi multado')
else:
    print('Você não foi multado')