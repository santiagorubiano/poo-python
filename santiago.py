
class Persona:
    def __init__(self, nombre ,edad) -> None:
            self.nombre = nombre
            self. edad = edad
            
    def saluda (self , otra_persona):
            print( f'Hola {otra_persona.nombre} me llamo {self.nombre}')
        
david = Persona('David', 35)
santiago = Persona('santiago',32)
    
david.saluda(santiago)        


