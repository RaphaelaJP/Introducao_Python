angulo = float(input('Digite o valor do ângulo: '))
import math

seno = math.sin(math.radians(angulo))
print('O ângulo de  {}, tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {}, tem COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))
