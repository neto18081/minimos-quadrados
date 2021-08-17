tam = int(input('Quantos valores são? '))
valx = []
valy = []

print('Digite os valores de X ')
for i in range(tam):
  val = float(input('X: '))
  valx.append(val)

print('Digite os valores de Y ')
for i in range(tam):
  val = float(input('Y: '))
  valy.append(val)

# Derivada parcial de B

list_b = []
sb_x = 0
sb_y = 0
sb_b = 2*tam
for x, y, index in zip(valx, valy, range(0, tam)):
  list_b.append({'x': 2*x, 'y': 2*y})
  sb_x += list_b[index]['x']
  sb_y -= list_b[index]['y']

sb_x = '{:.3f}'.format(sb_x)
sb_y = '{:.3f}'.format(sb_y)

print(sb_x,"a","+",sb_b,"b",sb_y)

# Derivada parcial de A

list_a = []
sa_x = 0
sa_y = 0
sa_b = 0
for x, y, index in zip(valx, valy, range(0, tam)):
  list_a.append({'x': 2*x*x, 'b': 2*x, 'y': 2*x*y})
  sa_x += list_a[index]['x']
  sa_y -= list_a[index]['y']
  sa_b += list_a[index]['b']

sa_x = '{:.3f}'.format(sa_x)
sa_y = '{:.3f}'.format(sa_y)
sa_b = '{:.3f}'.format(sa_b)

print(sa_x,"a","+",sa_b,"b",sa_y)



