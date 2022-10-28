# poo-python
![image](https://user-images.githubusercontent.com/90368949/198735748-c0d5f2c8-47f4-4349-bea1-ca4e5c12b2cb.png)

# Programación orientada a objetos en Python

Uno de los elementos más importantes de los lenguajes de programación es la utilización de clases para organizar programas en módulos y abstracciones de datos.

Las clases se pueden utilizar de diversas maneras. Pero en este artículo hablaremos de cómo utilizarlas en el contexto de la programación orientada a objetos. La clave para entender la programación orientada a objetos es pensar en objetos como agrupaciones de datos y los métodos que operan en dichos datos.

Por ejemplo, podemos representar a una persona con propiedades como nombre, edad, género, etc. y los comportamientos de dicha persona como caminar, cantar, comer, etc. De la misma manera podemos representar unos audífonos con propiedades como su marca, tamaño, color, etc. y sus comportamientos como reproducir música, pausar y avanzar a la siguiente canción.

Puesto de otra manera, la programación orientada a objetos nos permite modelar cosas reales y concretas del mundo y sus relaciones con otros objetos.

Las ideas detrás de la programación orientada a objetos tienen más de 50 años y han sido ampliamente aceptadas y practicadas en los últimos treinta. A mediados de la década de los setenta se comenzaron a escribir artículos académicos explicando los beneficios de esta aproximación a la programación. También durante esos años se comenzaron a escribir los primeros lenguajes de programación que incorporaban estas ideas (como Smalltalk y CLU). Pero no fue hasta la llegada de Java y C++ que la idea consiguió un número importante de seguidores.

Hasta ahora, en el curso previo de esta [serie](https://platzi.com/cursos/python-cs) hemos utilizado programación orientada a objetos de manera implícita. Cuando decimos “Los objetos son las principales cosas que un programa de Python manipula. Cada objeto tiene un tipo que define qué cosas puede realizar un programa con dicho objeto,” nos estamos refiriendo a las ideas principales de la programación orientada a objetos. Hemos utilizado los tipos lista y diccionario, entre muchos otros, así como los métodos asociados a dichos tipos.

Así como los creadores de un lenguaje de programación solo pueden diseñar una fracción muy pequeña de todas las funciones útiles (como `abs`, `float`, `type`, etc.), también pueden escribir una fracción muy pequeña de los tipos útiles (`int`, `str`, `dict`, `list`, etc.). Ya sabemos los mecanismos que nos permiten crear funciones, ahora veremos los mecanismos que nos permiten crear nuevos tipos (o clases).

## Clases en Python

Las estructuras primitivas con las que hemos trabajado hasta ahora nos permiten definir cosas sencillas, como el costo de algo, el nombre de un usuario, las veces que debe correr un bucle, etc. Sin embargo, existen ocasiones cuando necesitamos definir estructuras más complejas, por ejemplo un hotel. Podríamos utilizar dos listas: una para definir los cuartos y una segunda para definir si el cuarto se encuentra ocupado o no.

```python
cuartos_de_hotel = [101, 102, 103, 201, 202, 203]
cuarto_ocupado = [True,False,False,True,True,False]

```

Sin embargo, este tipo de organización rápidamente se sale de control. ¿Qué tal que quisiéramos añadir más propiedades, cómo si el cuarto ya fue aseado o no? ¿Si el cuarto tiene cama doble o sencilla? Esto nos lleva a una falta fuerte de organización y es justamente el punto que justifica la existencia de clases.

Las clases nos permiten crear nuevos tipos que contiene información arbitraria sobre un objeto. En el caso del hotel, podríamos crear dos clases `Hotel()` y `Cuarto()` que nos permitiera dar seguimiento a las propiedades como número de cuartos, ocupación, aseo, tipo de habitación, etc.

Es importante resaltar que las clases solo proveen estructura. Son un molde con el cual podemos construir objetos específicos. La clase señala las propiedades que los hoteles que modelemos tendrán, pero no es ningún hotel específico. Para eso necesitamos las instancias.

```python
class Persona:
    def __init__(self, nombre ,edad) -> None:
            self.nombre = nombre
            self. edad = edad
            
    def saluda (self , otra_persona):
            print( f'Hola {otra_persona.nombre} me llamo {self.nombre}')
        
david = Persona('David', 35)
santiago = Persona('santiago',32)
    
david.saluda(santiago)
```

## Instancias

Mientras que las clases proveen la estructura, las instancias son los objetos reales que creamos en nuestro programa: un hotel llamado PlatziHotel o Hilton. Otra forma de pensarlo es que las clases son como un formulario y una vez que se llena cada copia del formulario tenemos las instancias que pertenecen a dicha clase. Cada copia puede tener datos distintos, al igual que cada instancia es distinta de las demás (aunque todas pertenecen a una misma clase).

Para definir una clase, simplemente utilizamos el *keyword* `class`. Por ejemplo:

```python
class Hotel:
pass
```

Una vez que tenemos una clase llamada `Hotel` podemos generar una instancia llamando al constructor de la clase.

```python
hotel = Hotel()

```

# Atributos de la instancia

Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos el método especial `__init__` para definir el estado inicial de nuestra instancia. Recibe como primer parámetro obligatorio `self` (que es simplemente una referencia a la instancia).

```python
class Hotel:

def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20

```

# Métodos de instancia

Mientras que los atributos de la instancia describen lo que representa el objeto, los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase y normalmente operan en los mencionados atributos. Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben `self` como primer argumento.

```python
class Hotel:

    ...

def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

defocupacion_total(self):
return self.huespedes

hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2

```

Ahora que ya sabemos qué son las clases y cómo las podemos utilizar en nuestros programas, platícanos qué clases te serían útiles para modelar en uno de tus programas.

# Tipos de datos abstractos, clases e instancias

## Tipos de datos abstractos

### En Python todo es un objeto y tiene un tipo.

- Representación de datos y formas de interactuar con ellos.

### Formas de interactuar con un objeto:

- Creación
- Manipulación
- Destrucción

Cuando trabajamos con programación orientada a objetos tenemos varias ventajas:

- **De composición:** podemos estructurarlos en objetos mas pequeños.
- **Abstracción:** no nos preocupamos el funcionamiento del proceso de su comportamiento.
- **Encapsulación:** podemos esconder ciertos datos que solo son relevantes internamente en el objeto.

```python
# definición de clase

# Primero definimos el nombre de la clase y podemos determinar si hereda de otra clase.
class nombre_de_la_clase(super_clase):

    # El método init es un constructor, y siempre los métodos dentro
    # de los parámetros inician con el parámetro self
    def __init__(self, params):
        expresion

    # Las clases pueden tener comportamientos,
    # y estos los definimos con los métodos.
    def nombre_del_metodo(self, params):
        expresion# definición de clase

# Primero definimos el nombre de la clase y podemos determinar si hereda de otra clase.
class nombre_de_la_clase(super_clase):

    # El método init es un constructor, y siempre los métodos dentro
    # de los parámetros inician con el parámetro self
    def __init__(self, params):
        expresion

    # Las clases pueden tener comportamientos,
    # y estos los definimos con los métodos.
    def nombre_del_metodo(self, params):
        expresion
```

Para ver un ejemplo más a detalle crearemos una clase *Persona*

```python
# Definición
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso
david = Persona('David', 28)
karl = Persona('Karl', 26)

david.saluda(karl)
'Hola Karl, me llamo David'
```

**Instancias**

Mientras que la clase es un molde, a los objetos creados se les conoce como instancias. Cuando se crea una instancia, se ejecuta el método `__init__`, y todos los métodos de una clase reciben implícitamente como primer parámetro `self`.

Los atributos de clase nos permiten:

- Representar datos.
- Procedimientos para interactuar con los mismos (métodos).
- Mecanismos para esconder la representación.

Para acceder a los atributos de estos objetos se hace a través de la notación de punto. Además puede tener atributos privados (Por convención comienzan con _ ).

```python
class Coordenada:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__'
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))

    # Para ver si una variable es una instancia de una clase
    # podemos verificar con isinstance
    print(isinstance(coord_2, Coordenada))
```

## **Decomposición**

La **decomposición** es un concepto simple pero poderoso que implica:

- Dividir un problema en problemas más pequeños.
- Las clases permiten crear mayores abstracciones en forma de componentes.
- Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener.

Para realizar un ejemplo de decomposición modelaremos un automóvil.

```python
# Creamos la clase Automóvil.
class Automovil:

    # El constructor creara todas las características de la instancia.
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4) # Hacemos referencia a la clase Motor.

    # La clase automóvil tiene el método de acelerar.
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            # De la clase Motor ejecuta el método inyecta_gasolina.
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'

    def frenar(self):
        self._motor.inyecta_gasolina(0)
        self._estado = 'en_reposo'

# Creamos la clase Motor
class Motor:

    # Con el constructor definimos sus características.
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    # La clase motor tiene el método de inyecta_gasolina.
    def inyecta_gasolina(self, cantidad):
        passx
```

# ****Abstracción****

# ****Setters, getters y decorador property****

En este punto estamos comenzando a utilizar conceptos en Python que comienzan a ser más avanzados, por lo que es normal que puedan parecerte complejos o difíciles de asimilar, así que te animo a que los repases un par de veces.

Puedes tener la tranquilidad de que si bien, al inicio no los implementas en su totalidad, podrás seguir avanzando en el curso y poco a poco incorporarlos a tus proyectos donde lo más importante es que sepas que cuentas con estas herramientas.

---

## Entendiendo el concepto de *decorador*

Antes de comenzar me gustaría que analices el siguiente código:

```python
def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)

```

¿Qué pasará si llamamos a la función `zumbido()`? si logras determinar el resultado de salida o entenderlo con detalle, entonces podemos seguir adelante.

Lo que sucede es lo siguiente:

```python
>>> zumbido()
Este es el último mensaje...
Buzzzzzz
Este es el primer mensaje ;)

```

Si no diste con el resultado no te preocupes, solo hay que analizarlo con detalle y el truco está en la línea `zumbido = funcion_decoradora(zumbido)`. Sucede que la función `wrapper()` recibió la la función `zumbido()` cómo parámetro y coloca su salida entre los otros dos *prints*.

Todo lo que sucede se conoce en programación como *metaprogramación*(metaprogramming), ya que una parte del programa trata de modificar a otra durante el tiempo de compilación. En tanto un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.

## Mejorando la sintaxis

Definitivamente la forma en que decoramos la función es complejo, pero afortunadamente Python lo tiene en cuenta y podemos utilizar decoradores con el símbolo `@`. Volviendo al mismo ejemplo de `funcion_decoradora()`, podemos simplificarlo así:

```python
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

```

En solo tres líneas de código tenemos el mismo resultado que escribir `zumbido = funcion_decoradora(zumbido)`.

## ¿Qué son *getters* y *setters*?

A diferencia de otros lenguajes de programación, en Python los *getters* y *setters* tienen el objetivo de asegurar el encapsulamiento de datos. Cómo habrás visto, si declaramos una variable *privada* en Python al colocar un guión bajo al inicio de esta (`_`) y normalmente son utilizados para: añadir lógica de validación al momento de obtener y definir un valor y, para evitar el acceso directo al campo de una clase.

La realidad es que en Python no existen variables netamente privadas, pues aunque se declaren con un guión bajo podemos seguir accediendo a estas. En Programación Orientada a Objetos esto es peligroso, pues podemos alterar el método de alguna clase y tener efectos colaterales que afecten la lógica de nuestra aplicación.

### Clases sin *getters* y *setters*

Veamos un ejemplo con una clase que almacena un dato de distancia recorrida en millas (mi) y lo convierte a kilómetros (km):

```python
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

```

Ahora creemos un objeto que haga referencia a un viaje:

```python
# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos el atributo distancia
>>> print(avion.distancia)
200

# Obtenemos el método convertir_a_kilometros
>>> print(avion.convertir_a_kilometros())
321.8688

```

### Utilizando *getters* y *setters*

Incluyamos un par de métodos para obtener la distancia y otro para que no acepte valores inferiores a cero, pues no tendría sentido que un vehículo recorra una distancia negativa. Estos son métodos *getters* y *setters*:

```python
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

	# Método getter
	def obtener_distancia(self):
		return self._distancia

	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor

```

El método *getter* obtendrá el valor de la distancia que y el método *setter* se encargará de añadir una restricción. También debemos notar cómo `distancia` fue reemplazado por `_distancia`, denotando que es una variable privada.

Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizado. Esto no es nada escalable si tenemos cientos o miles de líneas de código.

## Función `property()`

Esta función está incluida en Python, en particular crea y retorna la propiedad de un objeto. La propiedad de un objeto posee los métodos `getter()`, `setter()` y `del()`.

En tanto la función tiene cuatro atributos: `property(fget, fset, fdel, fdoc)` :

- `fget` : trae el valor de un atributo.
- `fset` : define el valor de un atributo.
- `fdel` : elimina el valor de un atributo.
- `fdoc` : crea un *docstring* por atributo.

Veamos un ejemplo del mismo caso implementando la función `property()` :

```python
class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# Función para eliminar el atributo _distancia
	def eliminar_distancia(self):
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
>>> print(avion.distancia)
Llamada al método getter
Llamada al método setter
200

```

Aunque en este ejemplo hay una sola llamada a `print`, tenemos tres líneas como salida pues esta llama a los primeros dos métodos. Por lo que la propiedad `distancia` es una propiedad de objeto que ayuda a mantener el acceso de forma privada.

## Decorador `@property`

Este decorador es uno de varios con los que ya cuenta Python, el cual nos permite utilizar *getters* y *setters* para hacer más fácil la implementación de la programación orientada a objetos en Python cambiando los métodos o atributos de las clases de forma que no modifiquemos el código.

Pero mejor veamos un ejemplo en acción:

```python
class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
>>> print(avion.definir..distancia)
Llamada al método getter
Llamada al método setter
200

```

De esta manera usamos el decorador `@property` para utilizar *getters* y *setters* de una forma más prolija e incluimos una nueva funcionalidad a nuestro método `definir_distancia()` , al mismo tiempo protegemos el acceso a nuestras variables privadas y cumplimos con el principio de encapsulación.

[](https://pythones.net/propiedades-en-python-oop/)

[https://static.platzi.com/media/public/uploads/pensamiento-computacional-con-python-2_8a4741a5-a815-4516-8ee5-1965f5e71a9b.pdf](https://static.platzi.com/media/public/uploads/pensamiento-computacional-con-python-2_8a4741a5-a815-4516-8ee5-1965f5e71a9b.pdf)

# Herencia

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d88df81b-0c19-4095-8db8-d05c3fe09056/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68a4d54f-f028-41b1-a5f0-79746fa7e793/Untitled.png)

# Polimorfismo

**Polimorfismo** En computación, polimorfismo describe el concepto de que objetos de diferentes tipos pueden ser accedidos a través de la misma interfaz. Dicho de otra forma, es la habilidad de procesar objetos de forma distinta dependiendo de su tipo de dato o clase. Esto es la habilidad redefinir métodos para clases derivadas.Por ejemplo, dada la clase forma, el polimorfismo le permite al programador definir métodos para encontrar el área según la clase derivada, sea circulo, rectángulos, cuadrados, etc. Sin importar que forma sea el objeto, el área debería poder hallar el resultado correcto si se aplica el polimorfismo correctamente.

![https://www.w3schools.in/wp-content/uploads/2016/12/Polymorphism.png](https://www.w3schools.in/wp-content/uploads/2016/12/Polymorphism.png)

- *Existen dos tipos de polimorfismo: Dinámico y estático. ****En el dinámico** la creación del objeto ocurre en el run-time. Se le conoce también como ‘late-binding’ o ‘method overriding’ en diferentes clases (sobre escritura de método)**En el caso del estático** ocurre en el compile-time. Se le conoce también como ‘early binding’ o method overloading en diferentes clases (sobrecarga de métodos)Python sin embargo no soporta la sobrecarga de métodos por default, por lo que no es tan necesario tener en cuenta estos tipos de polimorfismo.Aunque herencia y polimorfismo están altamente relacionados no son exactamente lo mismo.

- *La mayor diferencia entre polimorfismo y herencia **es que el primeo busca cambiar el comportamiento de la super clase en la subclase, mientras que en la herencia solo se busca usar la estructura y comportamiento de la superclase en una subclase.

# ****Introducción a la complejidad algorítmica****

A continuación te dejo el código con una corrección en el `return`de la función recursiva:

```python
import time

def factorial(n):
    respuesta = 1

while n > 1:
        respuesta *= n
        n -= 1

return respuesta

def factorial_r(n):
if n == 1:
return 1

return n * factorial_r(n - 1)

if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)

```

Probablemente tu interprete de Python te este alertando:

`maximum recursion depth exceeded in comparison`

Esto se debe a que por seguridad Python tiene un limite de recursion (por defecto 1000, puedes leer más sobre ello en la [documentación oficial de python](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit)) que puedes averiguar realizando en tu main() un:

```python
print(sys.getrecursionlimit())

```

Antes de utilizarlo deberás hacer un import del modulo sys, al comienzo de tu script:

```python
import sys

```

Para ampliar este limite debes hacer un:

```python
sys.setrecursionlimit(numero_limite)

```

De esta manera, la recursion funcionara hasta el limite especificado.

Pero, tal como especifica la documentación de Python, debes ser cuidadoso con aumentar este limite.

Espero haberlos ayudado,

Saludos!

> EL problema de medir las implementaciones con tiempo es que es muy instable y depende de muchas cosas externas como el hardware,de los programas que tenga abiertos entonces no es muy confliable media la eficiencia del tiempo
> 

## **Conteo abstracto de operación**

Con esta técnica contamos los pasos que realiza nuestro algoritmo. En el siguiente ejemplo `respuesta` tendrá los números de pasos que realiza nuestro código al ejecutar.

```python
def f(x):

    respuesta = 0

    for i in range(1000):
        respuesta += 1

    for i in range(x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta
```

## **Notación asintótica**

Cuando hablamos de **notación asintótica** no importan las variaciones pequeñas, el enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito.

Siempre tenemos que estar preparados para cualquier caso, por lo que tenemos que saber medir a nuestro algoritmo en el mejor, promedio y peor de los casos.

Lo mejor que nos permite comparar nuestros algoritmos y su capacidad es medir el peor de los casos, ahí es donde entra el **Big O notation**, donde lo único que importa es el termino de mayor tamaño, sin importar las constantes que las acompañan.

```python
# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# En este caso el mayor término es n
# O(n) + O(n) = O(n + n) = O(2n) = O(n)
```

```python
# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# En este caso el mayor término es n²
# O(n) + O(n * n) = O(n + n²) = O(n²)
```

```python
# Ley de la multiplicación

def f(n):

    for i in range(n):

        for i in range(n):
            print(i, j)

# En este caso el mayor término es n²
# O(n) + O(n * n) = O(n * n) = O(n²)
```

`# Recursividad múltiple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) +  fibonacci(n - 2)

# En este caso el mayor término es 2**n (el símbolo ** denota "elevado a"),
# ya que realiza recursividad 2 veces por n veces.
# O(2**n)`

## **Clases de complejidad algorítmica**

Existen distintos tipos de complejidad algorítmica:

- **O(1) Constante:** no importa la cantidad de input que reciba, siempre demorara el **mismo tiempo**.
- **O(n) Lineal:** la complejidad crecerá de forma **proporcional** a medida que crezca el input.
- **O(log n) Logarítmica:** nuestra función crecerá de forma **logarítmica** con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
- **O(n log n) Log lineal:** crecerá de forma **logarítmica** pero junto con una **constante**.
- **O(n²) Polinomial:** crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
- **O(2^n) Exponencial:** crecerá de forma **exponencial**, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
- **O(n!) Factorial:** crece de forma **factorial**, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/big-o-complexity-chart.png](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/big-o-complexity-chart.png)

# **Algoritmos de búsqueda y ordenación**

## **Búsqueda lineal**

La **búsqueda lineal** es un algoritmo muy sencillo. Consta en buscar si un elemento se encuentra dentro de una lista, array o un sistema ordenado o no ordenado para poder determinar si el elemento se encuentra en el o forma parte de el.

¿Cuál es el peor caso del siguiente código? Si nos fijamos existe un **for loop** que crece según el tamaño de la lista, por lo cual nuestro Big O es O(n).

```python
import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
```

## **Búsqueda binaria**

La **búsqueda binaria** toma una estrategia llamada "Divide y conquista", la cual consiste en dividir el problema en 2 en cada iteración. Este algoritmo asume que la lista se encuentra ordenada, por lo que es necesario realizar este paso primero.

La **búsqueda binaria** es uno de los mejores algoritmos que se tienen hoy en día para búsqueda, ya que reduce significativamente el numero de pasos, y así disminuyendo nuestro Big O.

****Caso Promedio****

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/binary-and-linear-search-animations.gif](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/binary-and-linear-search-animations.gif)

****Peor de los Casos****

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/linear-vs-binary-search-worst-case.gif](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/linear-vs-binary-search-worst-case.gif)

****Mejor de los Casos****

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/linear-vs-binary-search-best-case.gif](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/linear-vs-binary-search-best-case.gif)

Para ver de forma practica haremos una búsqueda binaria a través de código. Lo primero que tenemos que realizar es ordenar nuestra lista antes de ejecutar la búsqueda.

```python
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
```

## **Ordenamiento de burbuja**

El primer algoritmo de ordenamiento que veremos es el **ordenamiento de burbuja**. Es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este procedimiento se repite hasta que no se requiere mas intercambios, lo que indica que la lista se encuentra ordenada.

1. Tenemos un array con elementos desordenados, el cual le medimos la longitud y la asignamos a una varaible llamada n.
2. Creamos el primer bucle i, este se basara en ser un bucle externo que ejecutara todas las veces que sea necesario el bucle interno.
3. creamos el bucle interno, este bucle utilizara la variable j. Este recorrera el array y comparara el elemento j y j + 1, al final cuando termine este primer bucle, habremos conseguido en el final del array el elemento mas grande. Pero este bucle tiene algo muy peculiar, que es el `(0, n - i -1)` De que trata esto? Sencillo, se basa en que SIEMPRE empezaremos en la posicion 0, pero cada vez que i, itere… iremos poniendo atras de todo en el array, los elementos mas grandes, por lo tanto, en la primer iteracion, con i = 0 dejaremos al elemento mas grande atras de todo el array, pero… ya en la segunda iteracion con i = 1, no nos interesa comparar el ultimo elemento del array, ya que este ya sabemos que es el mas grande de todos, por lo tanto, conseguiremos al segundo mas grande y este se posicionara en el ante ultimo lugar del array, como se consigue eso? `n - 1 -1` y por que siempre hay un -1 al final? bueno, eso es mas facil, eso lo debemos hacer, ya que estamos jugando con elementos basados en n, y n es la longitud del array, n = 8, pero resulta que al jugar con posiciones, nosotros siempre empezamos de 1, entonces son 8 posiciones, pero para acceder a la posicion numero 8, esta es n[7], porque siempre empezamos en 0!
4. 

```python
if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
return lista

```

y esto simplemente se basa en la asignacion y comparacion de el elemento 0, con el 1, el 1 con 2, el 2 con el 3. Lo unico curioso es que la sintaxis esta solo suce en python por lo tanto, si quiero hacerlo en js, debo ver en youtube como se escribe esta partesita.

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/bubble-sort.gif](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/bubble-sort.gif)

```python
import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
```

## **Ordenamiento por inserción**

El ordenamiento por inserción es uno de los algoritmos más comunes que estudian los Científicos del Cómputo. Es intuitivo y fácil de implementar, pero es muy ineficiente para listas de gran tamaño.

Una de las características del ordenamiento por inserción es que ordena en “su lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento ya que simplemente modifican los valores en memoria.

La definición es simple:

```
Una lista es dividida entre una sublista ordenada y otra sublista desordenada. Al principio, la sublista ordenada contiene un solo elemento, por lo que por definición se encuentra ordenada.

A continuación se evalua el primer elemento dentro la sublista desordenada para que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

La inserción se realiza al mover todos los elementos mayores al elemento que se está evauluando un lugar a la derecha.

Continua el proceso hasta que la sublista desordenada quede vacia y, por lo tanto, la lista se encontrará ordenada.

```

Veamos un ejemplo:

Imagina que tienes la siguiente lista de números:

7, 3, 2, 9, 8

Primero añadimos 7 a la sublista ordenada:

**7**, 3, 2, 9, 8

Ahora vemos el primer elemento de la sublista desordenada y lo guardamos en una variable para mantener el valor. A esa variable la llamaremos `valor_actual`. Verificamos que 3 es menor que 7, por lo que movemos 7 un lugar a la derecha.

**7**, 7, 2, 9, 8 (valor_actual=3)

3 es menor que 7, por lo que insertamos el valor en la primera posición.

**3, 7**, 2, 9, 8

Ahora vemos el número 2. 2 es menor que 7 por lo que lo movemos un espacio a la derecha y hacemos lo mismo con 3.

**3, 3, 7**, 9, 8 (valor_actual=2)

Ahora insertamos 2 en la primera posición.

**2, 3, 7**, 9, 8

9 es más grande que el valor más grande de nuestra sublista ordenada por lo que lo insertamos directamente en su posición.

**2, 3, 7, 9**, 8

El último valor es 8. 9 es más grande que 8 por lo que lo movemos a la derecha:

**2, 3, 7, 9**, 9 (valor_actual=8)

8 es más grande que 7, por lo que procedemos a insertar nuestro valor_actual.

**2, 3, 7, 8, 9**

Ahora la lista se encuentra ordenada y no quedan más elementos en la sublista desordenada.

Antes de ver la implementación en Python, trata de implementarlo por ti mismo y compártenos tu algoritmo en la sección de comentarios.

Esta es una forma de implementar el algoritmo anterior:

```python
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
```

## **Ordenamiento por mezcla**

El **ordenamiento por mezcla** creado por **John von Neumann** el cual aplica el concepto de "divide y conquista". Primero divide una lista en partes iguales hasta que quedan sublistas de 1 o 0 elementos. Luego las recombina en forma ordenada.

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/merge-sort.gif](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/merge-sort.gif)

```python
import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
```

# **Ambientes virtuales**

Los **ambientes virtuales** permiten aislar el ambiente para poder instalar diversas versiones de paquetes. A partir de *python 3* se incluye en la librería estándar en el módulo **venv**. Ningún ingeniero profesional de Python trabaja sin ellos.

**Pip** permite descargar paquetes de terceros para utilizar en nuestro programa, también permite compartir nuestros paquetes con terceros y también podemos definir la versión del paquete que necesitamos.

Para crear un ambiente virtual primer crearemos el directorio para nuestro proyecto.

```bash
mkdir graficado             # Creamos el directorio del proyecto.
cd graficado/               # Ingresamos al directorio.
python3 -m venv env         # Creamos un ambiente virtual en env.
source env/bin/activate     # Activamos el ambiente.
```

Para poder instalar librerías lo haremos con el comando pip.

```bash
pip install bokeh   # pip install instalara la librería.
pip freeze          # Con pip freeze veremos que librerías están instaladas.
```

Para desactivar el ambiente virtual lo haremos con el siguiente comando.

```python
deactivate          # Comando para desactivar ambiente Virtual
```

# **Graficado**

## **¿Por qué graficar?**

Es importante que podamos traducir los datos que nos arrojan nuestro programa en un elemento visual, así podemos realizar reconocimientos de patrones, predicción de series, simplifica la interpretación y la conclusión acerca de los datos.

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/grafico.svg](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/grafico.svg)

## **Graficado simple**

La librería **[Bokeh](http://docs.bokeh.org/en/latest/index.html)** permite construir gráficas complejas de manera rápida y con comandos simples, también nos permite exportar a varios formatos como html, notebooks, imágenes, etc. **[Bokeh](http://docs.bokeh.org/en/latest/index.html#)** se puede utilizar en el servidor con **Flask** y **Django**.

```python
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
```

# **Algoritmos de optimización**

## **Introducción a la optimización**

El concepto de **optimización** permite resolver muchos problemas de manera computacional. Cuando pensamos en un algoritmo de optimización debemos definir una función objetivo que debemos maximizar o minimizar, respetando una serie de limitantes que definamos.

[https://www.youtube.com/watch?v=UR2oDYZ-Sao](https://www.youtube.com/watch?v=UR2oDYZ-Sao)

## **El problema del morral**

![https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/backpack-problem.png](https://github.com/karlbehrensg/poo-y-algoritmos-python/raw/master/readme_img/backpack-problem.png)

Imagina que eres un ladrón que entra a un museo pero tienes un gran problema, nada mas tienes una mochila pero hay muchísimas cosas mas de las que puedes cargar, por lo cual debes determinar cuales artículos puedes cargar y te entregaran el mayor valor posible.

Para este problema sabemos que no podemos dividir los artículos, por lo que nuestra primera aproximación sera evaluar los artículos.

`def morral(tamano_morral, pesos, valores, n):

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 40
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)`

[](https://static.platzi.com/media/public/uploads/pensamiento-computacional-con-python-2_8a4741a5-a815-4516-8ee5-1965f5e71a9b.pdf)

Algunos sitios donde encontrar retos:

- [https://www.hackerrank.com](https://www.hackerrank.com/)
- [https://exercism.io/](https://exercism.io/)
- [https://www.freecodecamp.org/learn](https://www.freecodecamp.org/learn)

[https://www.hackerrank.com](https://www.hackerrank.com/)

[https://codewars.com](https://codewars.com/)

[http://codeforces.com/](http://codeforces.com/)

[https://coderbyte.com/](https://coderbyte.com/)

[https://www.codingame.com/](https://www.codingame.com/)

[https://www.codechef.com/](https://www.codechef.com/)

[https://www.topcoder.com/challenges/](https://www.topcoder.com/challenges/)
