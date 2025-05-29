"""

1) Seleccionar los Números del RUT sin el Dígito Verificador: 27.962.409

2 Reordenar los Números de Derecha a Izquierda: 9 0 4 2 6 9 7 2

3 Multiplicar Cada Número por la Serie 2, 3, 4, 5, 6, 7 Repetidamente:

 """

rut = input("Escriba el RUT: ")
contador = 2
suma = 0

rut_1 = rut.replace(".", "")
rut_2 = rut_1.replace("-", "")

sin_d = rut_2[:-1]
invertir = sin_d [:: -1]
#print(invertir)
for digito in invertir:

  digito = int(digito)
  a = (f"{contador * digito}" )
  #print("numeros sin sumar: ", a)
  contador +=1
  suma = suma + int(a)
  #print("suma:", suma)
  if contador > 7:
    contador = 2

dividir = suma / 11
entero = int(dividir)
m = entero * 11
resta = suma - m
digito_v = 11 - resta
print("es un rut valido", digito_v)