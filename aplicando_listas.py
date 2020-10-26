my_list = list(range(101))
print(my_list)
print("""
#############################
Doble del anterior:
""")
# su doble
double = [i*2 for i in my_list]
print(double)
print("""
#############################
Solo numeros pares:
""")

# numeros pares aplicando filtro
pares = [i for i in my_list if i % 2 == 0]
print(pares)
print("""
#############################
Solo numeros impares o primos:
""")
# numeros impares y primos
impares = [i for i in my_list if i % 2 != 0]
print(impares)

print("""
#############################
Clonar lista de impares:
""")
# clonar lista impar
clonar = list(impares)
print(clonar)
