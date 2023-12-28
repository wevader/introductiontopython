 ### CLASSES ###
 
class MyPerson:
  pass

print (MyPerson) ## las clases pueden llmarse con o sin parentesis
print (MyPerson())

class Person:
  def __init__(self, name, surname, alias = "sin alias"): ## palabra reservada para hacer un constructor def __init___(self)
   # self.name = name
   # self.surname = surname
    self.full_name = f"{name} {surname} ({alias})"  ## en este formato el fullname es publico
    #pass ## cuando no se tiene codigo se pone pass
    self.__name = name  ## en este formato name es privado
    self.__surname = surname ## privado surname // no se puede modificar a los valores
  
  def get_name(self): # funcion para poder acceder a los valores privados ** SOLO PARA LECTURA DE LOS VALORES NO SE PUEDEN MODIFICAR
    return self.__name
  
  def walk(self):
    print(f"{self.full_name} esta caminando")
  
my_person = Person("victor", "mendez")
#print(my_person.name)
#"print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)


my_person.walk()

my_other_person = Person("Daniel", "Torres", "wevader")
my_other_person.walk()
my_other_person.full_name= "Hector de Leon"
print(my_other_person.full_name)
my_other_person.walk()


