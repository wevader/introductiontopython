### strings ###

my_string = "mi string"
my_other_string = 'mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + "" + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es mi string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un strin \\n escapado"
print(my_scape_string)

### Formateo ###

name, surname, age = "daniel", "mendez", 37

print("mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age)) 
print(f"mi nombre es {name} {surname} y mi edad es {age}")

### Desempaquetado de caracteres ###

language = "python"

a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#reversa

reversed_language = language[::-1]
print(reversed_language)


#funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().islower())