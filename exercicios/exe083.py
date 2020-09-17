from rx.operators import join

abertos = 0
fechados = 0
count = 0

exp = list(input('Digite: '))

for n in exp:
    if n == '(':
        abertos += 1
    elif n == ')':
        fechados += 1
    else:
        continue
if abertos == fechados:
    print(f'{"".join(exp)} está correta!')
else:
    print(f'{"".join(exp)} está errada!')
