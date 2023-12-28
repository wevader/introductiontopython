### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) ## <class 'dict'>
print(type(my_other_dict)) ## <class 'dict'>

my_other_dict = {'Nombre:':'Victor', 'Apellido':'Mendez', 'Edad': 37, 1: 'Python'}

my_dict ={
  "Nombre": "Daniel",
  "Apellido": "Torres",
  "Edad":37,
  "Lenguajes": {"Python", "JavaScript", "C++"},
  1: 1.78
  }

print(my_other_dict) ## {'Nombre:': 'Victor', 'Apellido': 'Mendez', 'Edad': 37, 1: 'Python'}
print(my_dict) ## {'Nombre': 'Daniel', 'Apellido': 'Torres', 'Edad': 37, 'Lenguajes': {'JavaScript', 'Python', 'C++'}, 1: 1.78}
print(len(my_dict)) ##  5


print(my_dict["Nombre"]) ## Daniel

my_dict["Nombre"] = "Victor"

print(my_dict["Nombre"]) ## Victor

my_dict["Calle"] = "Nueva Calle"
print(my_dict) ## {'Nombre': 'Victor', 'Apellido': 'Torres', 'Edad': 37, 'Lenguajes': {'Python', 'C++', 'JavaScript'}, 1: 1.78, 'Calle': 'Nueva Calle'}


del my_dict["Calle"] ### si se puede borrar un solo elemento 
print(my_dict) ## {'Nombre': 'Victor', 'Apellido': 'Torres', 'Edad': 37, 'Lenguajes': {'JavaScript', 'Python', 'C++'}, 1: 1.78}

print("Victor" in my_dict) ### busca las claves no el valor
print("Nombre" in my_dict)

print(my_dict.items()) ## dict_items([('Nombre', 'Victor'), ('Apellido', 'Torres'), ('Edad', 37), ('Lenguajes', {'Python', 'JavaScript', 'C++'}), (1, 1.78)])
print(my_dict.values()) ## dict_values(['Victor', 'Torres', 37, {'Python', 'JavaScript', 'C++'}, 1.78])
print(my_dict.keys()) ## dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])


my_new_dict = dict.fromkeys(("Nombre", 1)) ## crea nuevo diccionario con las claves
print(my_new_dict) ## {'Nombre': None, 1: None}

my_new_dict = dict.fromkeys(my_dict) ## se crea un nuevo dictionarie con los valores en 0 de my_dict
print(my_new_dict) ## {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}




