# Crie uma tupla preenchida com os 20 primeiros colocados na tabela do campeonato brasileiro de futebol, na ordem de
# colocação. Depois mostre: Apenas os 5 primeiros colocados. Os últimos 4 colocados. Uma lista com os times em ordem
# alfabética. Em que posição na tabela está o time da Chapecoense.

print('===== DESAFIO 73 =====\n')

times = ('Athletico PR', 'Atlético MG', 'Avaí', 'Bahia', 'Botafogo', 'Ceará', 'Chapecoense', 'Corinthians',
'Cruzeiro', 'CSA', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
'Santos', 'São Paulo', 'Vasco')

print(f'Os cincos primeiros colocados: {times[0:5]}')
print(f'Os quatro últimos colocados: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'Posição da Chapecoense: {times.index("Chapecoense") + 1}')
