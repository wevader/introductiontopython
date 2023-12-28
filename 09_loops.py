### Loops ###

my_condition = 0

while my_condition <= 10: ## se repite el bucle mientras la condicion se cumpla
  print(my_condition)
  my_condition += 1
else: #opcional
  print("mi condicion es mayor a 10")
  
  
while my_condition < 20:
  my_condition += 2
  if my_condition == 15:
    print("mi condicion es 15")
    break
  print(my_condition)
  
print("mi condicion es menor a 20")


my_list = [20, 230, 34, 54, 21, 52, 78]

for element in my_list: ## se imprime cada uno de los elementos
  print(element) 
  
my_tuple = (37, 1.78, "Daniel", "Mendez")

for element in my_tuple:
  print(element) 

my_set = {'Victor', 'Torres', 1.78}

for element in my_set:
  print(element) 
  
my_dict ={
  "Nombre": "Daniel",
  "Apellido": "Torres",
  "Edad":37,
  "Lenguajes": {"Python", "JavaScript", "C++"},
  1: 1.78
  } 

for element in my_dict.values():
  print(element) 
  
for element in my_dict:
  print(element)
  if element == "Edad":
    continue ## el break se sale del bucle por eso se usa continue aunque este no se usa actualmente
  print("se ejecuta")
else:
  print("el bucle FOR para diccionario ha finalizado")
  
  
print("sigue ejecucion")
  