  ### Exceptions Handling   ### para manejo de errores ###
  
numberOne, numberTwo = 5, 1

numberTwo = "1"

"""
try: 
  print(numberOne + numberTwo)  ## se produjo un error *** TypeError: unsupported operand type(s) for +: 'int' and 'str'
  print("Todo correcto")    

except: ## se ejecuta si pasa un error 
  print("Error: Invalid Value")
else: # solo se ejecuta cuando no hay error
  print("La ejecucion continua correctamente")
finally: # se ejecuta bajo cualquier circunstancia
  print("La ejecucion continua")

"""
try: 
  print(numberOne + numberTwo)  ## se produjo un error *** TypeError: unsupported operand type(s) for +: 'int' and 'str'
  print("Todo correcto")    

except TypeError as error: ## ejecuta si pasa un error y se da informacion mas detallada sobre el error si es tipo TYpe
  print(error)
  
except ValueError as error: ## se ejecuta si pasa un error y se da informacion mas detallada sobre el error si es tipo value 
  print(error)
  
except Exception as exception: ## se controla de forma mas general cualquier tipo de error que ocurra 
  print(exception)