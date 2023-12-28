## conditionals ##

my_condition = False

if my_condition:
  print("se ejecuta la condicion if")

my_condition = 5 * 2
  
if my_condition == 11: ## la condicion no se cumple por lo cual el if no se ejecuta
  print("se ejecuta la condicion del segundo if")
  
if my_condition == 10: ## la condicion se cumple por lo cual el if se ejecuta
  print("se ejecuta la condicion del tercer if")
  
if my_condition > 10:
  print("se ejecuta la condicion del tercer if")
else:
  print("Es menor o igual a 10")
  
if my_condition > 10 and my_condition < 20: ## pueden ser mas de una condicion a evaluar
  print("se ejecuta la condicion del tercer if")
else:
  print("Es menor o igual a 10 o mayor o igual que 20")
  

if my_condition > 10 and my_condition < 20: ## pueden ser mas de una condicion a evaluar
  print("se ejecuta la condicion del tercer if")
else:
  print("Es menor o igual a 10 o mayor o igual que 20")
  
  
if my_condition > 10 and my_condition < 20: ## pueden ser mas de una condicion a evaluar
  print("se ejecuta la condicion del tercer if")
elif my_condition == 1: ## es parte del mismo if, es decir si el if no se cumple no se ejecuta el elif 
  print("Es igual a 1")
else: ## se ejecuta si no se cumple ninguna de las condiciones
  print("Es menor o igual a 10 o mayor o igual que 20")
  
print("la ejecucion continua")


my_string = ""

if my_string: ## cuando el string es vacio python lo toma como false por lo tanto la condicion no se cumple y no ejecuta el if
  print("mi cadena de texto no esta vacia")
  
my_string = "Texto existe"

if my_string == "Texto existe": ## la condicion se cumple es True se ejecuta el if 
  print("mi cadena de texto no esta vacia")
  
my_string = ""

if not my_string: ## la condicion se vuelve False debido al not y por lo tanto se cunple la condicion, ya que string vasio es False
  print("mi cadena de texto esta vacia")