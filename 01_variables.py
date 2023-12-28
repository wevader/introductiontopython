# variables 

my_variable = "My string variable"
print(my_variable)

my_int_variable= 20
print(type(my_int_variable))

re_my_int_variable= str(my_int_variable)
print(type(re_my_int_variable))

print("este es el valor de int variable:", my_int_variable)
#concatenacion de variables en print
print(my_variable, my_int_variable, re_my_int_variable)



#algunas funciones del sistema
print(len(re_my_int_variable))


#variables en una sola linea
name, surname, alias, age = "Victor", "Mendez", "wevader",  37
print("me llamo:", name, surname, "mi alias es:", alias,"y mi edad es:", 37)


#inputs

name = input("cual es tu nombre:")
age = input("cual es tu edad:")

#forzamos tipo

address: str = "Mi direccion"
address = True
address = 5
