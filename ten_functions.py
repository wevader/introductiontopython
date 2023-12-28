  ### Functions ###


def my_function (): ## una funcion se define sin llaves solo con la identacion, es decir, todo lo que este en la misma identacion es parte de la funcion
  print("Esto es una funcion")
  
my_function()

first_value = 20
second_value = 30

def sum_two_values (first_value, second_value):
  print(first_value + second_value)
  
sum_two_values(first_value, second_value)


def sum_two_values_with_return (first_value, second_value):
  return first_value + second_value ## return lleva el resultado fuera de la funcion para usarlo en otra parte del programa

my_result = sum_two_values_with_return(first_value, second_value) ## se guardo el resultado de la funcion a la variable my_result

def print_name (name, surname):
  print(f"{name} {surname}") ## con la f se formatea y se imprimen los variables name en surne en el orden elegido
  
print_name("victor", "mendez")


def print_name_with_default (name, surname, alias = "Sin alias"): ## se le asigna un valor defaul en caso de no existir
  print(f"{name} {surname} ({alias})")
  

print_name_with_default("victor", "mendez") ## se imprime el valor defaul en el alias ya que no se introdujo el dato
print_name_with_default("victor", "mendez", "wevader")


def print_upper_text(*texts):
  for text in texts:
    print(text.upper())
    
print_upper_text("Hola", "python", "wevader")

