
# Script para renombrar ficheros en un directorio

A menudo tenemos un montón de ficheros desordenados en algún directorio y nos gustaría renombrarlos todos a la vez, siguiendo algún patrón; un ejemplo pueden ser las fotos de un viaje. 

Queremos que, en lugar de llamarse algo así como "IMG001234.png", nuestras fotos tengan nombres del tipo "2016_03_Viaje_Noruega_001.png". Vamos a crear un script de Python que haga esta tarea por nosotros, dándole como información el directorio donde están nuestros ficheros y el nuevo nombre que queremos que tengan (patrón).

## Empecemos por el principio
Lo primero que veremos en la mayoría de scripts de Python (como en cualquier otro lenguaje) es la importación de las librerías que nos hacen falta.
En nuestro caso, necesitamos trabajar con directorios, ficheros, rutas, etc., por lo que necesitaremos el módulo `os` de Python.
En Python hay dos formas de importar módulos:
+ Importar clases o funciones sueltas dentro de un módulo:  `from _ import _`
+ Importar todo un módulo:  `import _`

Veamos dos ejemplos (para listar los ficheros de un directorio):


```python
from os import listdir
listdir('.')
```


```python
import os
os.listdir('.')
```

Cuándo usar uno u otro dependerá de las necesidades que tengamos en nuestro script. Como en este caso vamos a necesitar usar varias de las funciones del módulo `os`, será más cómoda la segunda opción.

## Demos forma a nuestro script
Con el anterior ejemplo hemos visto cómo listar los ficheros del directorio en el que nos encontramos (cuya ruta relativa se indica con '.'). Ahora vamos a recorrer dicha lista y vamos a separar el nombre del fichero y su extensión.


```python
import os

for file in os.listdir('.'):
    file_name, file_ext = os.path.splitext(file)
    print("Nombre:", file_name, "Extensión:", file_ext)
```

Con este código hemos visto algunas cosas interesantes de Python:
+ **Sintaxis del bucle for:** "por cada elemento `file` de la lista `os.listdir('.')`".
+ **Tuplas:** listas no mutables, se escriben entre paréntesis. En este caso, nos permiten que la función `os.path.splitext()` nos devuelva dos valores: en realidad nos está devolviendo una tupla, pero hemos simplificado la sintaxis.
+ **La función print** puede recibir más de un parámetro. También podríamos haber utilizado la función `format()` para pasarle a print un texto ya formateado (lo usaremos más adelante).
+ **Las cadenas de texto en Python** pueden escribirse tanto entre comillas simples ' ' como dobles " ".
+ Aunque las variables en Python pueden llamarse de (casi) cualquier manera, **la guía de estilo (PEP 8) recomienda usar el *snake case***, es decir, si hay varias palabras, poner _ entre ellas.

## Parámetros necesarios
Ahora que ya somos capaces de recorrer la lista de ficheros y separarlos en nombre y extensión, nos falta poco para poder modificarlos. 
Antes de dar ese paso, deberíamos proporcionarle a nuestro programa dos datos:
+ La ruta donde estén los ficheros que queremos renombrar 
+ El patrón del nuevo nombre que vamos a darles (al que añadiremos un número al final).

De momento, vamos a hacerlo mediante dos variables que más tarde sustituiremos. 


```python
import os

files_path = '/home/irene/Desktop/carpeta_prueba'

# Definimos el patrón del nombre dejando {} donde queremos que vaya el número 
name_pattern = '2016_12_Viaje_Noruega_{}'

# Iniciamos el contador para que el primer fichero tenga el número 1
count = 1

for file in os.listdir(files_path):
    file_name, file_ext = os.path.splitext(file)
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(count) + file_ext
    
    # Incrementamos el contador
    count += 1
    
    print("\nNombre antiguo:", file, "\nNombre nuevo:", new_file)
    
```

Qué cosas nuevas hemos aprendido:
+ En Python, los comentarios empiezan con #
+ Con la función *format* podemos tomar un *string* y sustituir parámetros, indicando su posición mediante {}

## ¡Por fin renombramos!
Vamos a añadir la instrucción que nos permite renombrar ficheros. Tendremos que tener en cuenta que necesita la ruta completa al fichero, no solamente los nombres antiguo y nuevo:


```python
import os

files_path = '/home/irene/Desktop/carpeta_prueba'

# Definimos el patrón del nombre dejando {} donde queremos que vaya el número 
name_pattern = '2016_12_Viaje_Noruega_{}'

# Iniciamos el contador para que el primer fichero tenga el número 1
count = 1

for file in os.listdir(files_path):
    file_name, file_ext = os.path.splitext(file)
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(count) + file_ext
    
    # Incrementamos el contador
    count += 1
    
    # Construimos la ruta completa al fichero
    old_file_path = os.path.join(files_path, file)
    # En este caso estamos dejando los ficheros en el mismo directorio, 
    # pero podríamos moverlos a otro
    new_file_path = os.path.join(files_path, new_file)

    # Renombramos
    os.replace(old_file_path, new_file_path)
    
    print("\nNombre antiguo:", file, "\nNombre nuevo:", new_file)
```

¿Ya hemos terminado? Bueno, tenemos resultados interesantes, pero todavía quedan muchos detalles que podemos pulir para que nuestro script funcione mejor y sea más usable...


## Mejoremos nuestro script
### Renombrar en orden
Hay varios aspectos que podemos mejorar, pero quizá lo primero y más importante es que los ficheros se renombren en orden. Si nos hemos fijado, la función `os.listdir()` no nos devuelve una lista ordenada, sino que recorre el directorio que le proporcionemos en un orden arbitrario. Para evitar este problema, podemos utilizar la función `sorted()`, que nos devuelve una lista ordenada.

Sustituiremos:


```python
for file in os.listdir(files_path):
```

Por:


```python
for file in sorted(os.listdir(files_path)):
```

Resultado:


```python
import os

files_path = '/home/irene/Desktop/carpeta_prueba'

# Definimos el patrón del nombre dejando {} donde queremos que vaya el número 
name_pattern = '2016_12_Viaje_Noruega_{}'

# Iniciamos el contador para que el primer fichero tenga el número 1
count = 1

for file in sorted(os.listdir(files_path)):
    file_name, file_ext = os.path.splitext(file)
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(count) + file_ext
    
    # Incrementamos el contador
    count += 1
    
    # Construimos la ruta completa al fichero
    old_file_path = os.path.join(files_path, file)
    # En este caso estamos dejando los ficheros en el mismo directorio, 
    # pero podríamos moverlos a otro
    new_file_path = os.path.join(files_path, new_file)

    # Renombramos
    os.replace(old_file_path, new_file_path)
```

### Números precedidos de ceros
Otra cuestión que mejoraría nuestro script es que, a la hora de numerar los ficheros, tengamos en cuenta cuántos hay para numerar con "001" en lugar de con "1" directamente y así conseguir que estén ordenados correctamente una vez renombrados.
Para ello, primero tendremos que convertir nuestros enteros a *string* y, después, rellenar con ceros por la izquierda. Podemos hacerlo con la función `rjust`, a la que debemos indicar la longitud del *string* que queremos y el carácter con el que rellenar:


```python
count = 1
str(count).rjust(3, '0')
```

Esto está muy bien, pero ¿cómo sabemos esta longitud? Si conocemos de antemano cuántos ficheros tenemos en nuestro directorio, podríamos *hardcodear* este parámetro. Pero lo ideal es calcularlo a partir del listado de ficheros que ya tenemos.
Con la función `len()` podemos saber la longitud de una lista; sólo nos queda averiguar el número de dígitos. Por ejemplo:
+ Con logaritmos en base 10 (tendremos que importar el módulo `math`)
+ Convirtiendo a *string* y, de nuevo, calculando la longitud

Veamos:


```python
files_path = '/home/irene/Desktop/carpeta_prueba'

# Número de ficheros
files_in_dir = os.listdir(files_path)
num_files = len(files_in_dir)
print ("Número total de ficheros: ", num_files)

# Cálculo de dígitos
# Opción 1: logaritmo y redondeo hacia arriba
from math import log10, ceil
num_digits = ceil(log10(num_files)) 
print ("Número de digitos (logaritmo): ", num_digits)

# Opción 2: longitud de un string
num_digits = len(str(num_files))
print ("Número de digitos (string): ", num_digits)
```

¡Cómo molan las matemáticas y la programación! :)
Con esto, elijamos la opción que más nos guste y completemos nuestro código. Yo, como soy muy fan de las matemáticas, me quedo con los logaritmos.

Lo que sí deberíamos tener en cuenta en nuestro código es no llamar a la función `os.listdir()` más de una vez. Almacenamos la lista devuelta en una variable y luego la utilizamos tanto para calcular su longitud como para recorrerla y hacer nuestro renombrado:


```python
import os
from math import log10, ceil

files_path = '/home/irene/Desktop/carpeta_prueba'

# Definimos el patrón del nombre dejando {} donde queremos que vaya el número 
name_pattern = '2016_12_Viaje_Noruega_{}'

# Obtenemos el listado de ficheros en el directorio indicado
files_in_dir = os.listdir(files_path)

# Obtenemos el número de dígitos a partir del número de ficheros
# - no os asuste encadenar funciones ;) -
num_digits = ceil(log10(len(files_in_dir))) 

# Iniciamos el contador para que el primer fichero tenga el número 1
count = 1

for file in sorted(files_in_dir):
    file_name, file_ext = os.path.splitext(file)
    
    # Convertimos el contador al string precedido de los ceros necesarios
    filled_count = str(count).rjust(num_digits, '0')
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(filled_count) + file_ext
    
    # Incrementamos el contador
    count += 1
    
    # Construimos la ruta completa al fichero
    old_file_path = os.path.join(files_path, file)
    # En este caso estamos dejando los ficheros en el mismo directorio, 
    # pero podríamos moverlos a otro
    new_file_path = os.path.join(files_path, new_file)

    # Renombramos
    os.replace(old_file_path, new_file_path)
```

### Contemos de la forma "pythonista"
Estoy segura de que a más de una le ha parecido un poco "fea" la manera de programar el contador... Ahora que ya sabemos algo de Python, intuimos que tiene que haber otra forma más elegante, más "compacta".

¡Pues sí, la hay! Y se llama `enumerate()`. 
Veamos cómo funciona: 


```python
lst = ['a', 'b', 'c']
for count, elem in enumerate(lst):
    print(count, elem)
```

En Python, el bucle `for` puede iterar sobre varias variables (en realidad es una forma de escribir una tupla sin paréntesis). Con esto y con la función `enumerate()` podemos iterar a la vez sobre un contador y sobre el elemento de la lista en cuestión.

Obviamente, podemos implementar esto mismo de muchas otras formas. Probablemente, para las que programen en otros lenguajes, les parecerá mucho más claro algo así:


```python
lst = ['a', 'b', 'c']
for i in range(0, len(lst)):
    print(i, lst[i])
```

Como siempre, esto ya es a gusto de cada programadora. Yo, personalmente, estoy encantada con la sintaxis de Python y recomiendo adaptarse al estilo de cada lenguaje de programación.

Para incorporar el anterior código a nuestro script, lo único que tendremos que tener en cuenta es que Python empezará a contar desde 0. Si queremos empezar a renombrar desde 1, tendremos que sumar.


```python
import os
from math import log10, ceil

files_path = '/home/irene/Desktop/carpeta_prueba'

# Definimos el patrón del nombre dejando {} donde queremos que vaya el número 
name_pattern = '2016_12_Viaje_Noruega_{}'

# Obtenemos el listado de ficheros en el directorio indicado
files_in_dir = os.listdir(files_path)

# Obtenemos el número de dígitos a partir del número de ficheros
num_digits = ceil(log10(len(files_in_dir))) 

for count, file in enumerate(sorted(files_in_dir)):
    file_name, file_ext = os.path.splitext(file)
    
    # Convertimos el contador al string precedido de los ceros necesarios
    # Le añadimos 1 porque enumerate empieza a contar desde 0
    filled_count = str(count + 1).rjust(num_digits, '0')
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(filled_count) + file_ext   
    
    # Construimos la ruta completa al fichero
    old_file_path = os.path.join(files_path, file)
    # En este caso estamos dejando los ficheros en el mismo directorio, 
    # pero podríamos moverlos a otro
    new_file_path = os.path.join(files_path, new_file)

    # Renombramos
    os.replace(old_file_path, new_file_path)
```

#### Hablando de compacto y "pythonista"
Si hay algo que me requetencanta de Python son las "list comprehension", una forma de generar listas en una sola línea... 

Aunque en este caso no necesitamos utilizarlas, todo curso introductorio debería al menos nombrarlas. Os propongo como ejemplo que nos implementemos la función `enumerate()` de forma "casera" - y de paso vemos cómo se definen funciones en Python).

Lo podemos hacer a partir de la forma "típica" de recorrer una lista que hemos visto antes. 


```python
# Definimos la nueva función
def my_enumerate(lst):
    # ¡Cómo molan las list comprehension!
    return [(i, lst[i]) for i in range(0, len(lst))]

# Utilizamos la nueva función
lst = ['a', 'b', 'c']
for count, elem in my_enumerate(lst):
    print(count, elem)
```

### "Des-hardcodeemos" nuestro script
Para que nuestro script sea el más molón del mundo, habrá que dotarlo de cierta usabilidad y que nos pueda servir para renombrar ficheros en distintos directorios y con distintos nombres (y que no tengamos que modificar el código para ello). 

Vamos a añadir que podamos proporcionarle la ruta al directorio y el nuevo patrón de renombrado como parámetros:
+ En la llamada al script
+ Menú por consola

#### Menú por consola
Empecemos por la forma más sencilla. Para hacer un menú por consola lo único que necesitamos aprender es la función `input()` (o `raw_input()` si utilizamos Python2).

Tan fácil como:


```python
import os
from math import log10, ceil

print('Escribe la ruta al directorio donde están los ficheros:')
files_path = input()
print('Escribe el nuevo nombre de los ficheros poniendo {} donde vayan los números:')
name = input()

# Si el patrón del nombre proporcionado no contiene {}, se lo añadimos al final 
name_pattern = name if '{}' in name else name + '_{}'

# Obtenemos el listado de ficheros en el directorio indicado
files_in_dir = os.listdir(files_path)

# Obtenemos el número de dígitos a partir del número de ficheros
num_digits = ceil(log10(len(files_in_dir))) 

for count, file in enumerate(sorted(files_in_dir)):
    file_name, file_ext = os.path.splitext(file)
    
    # Convertimos el contador al string precedido de los ceros necesarios
    # Le añadimos 1 porque enumerate empieza a contar desde 0
    filled_count = str(count + 1).rjust(num_digits, '0')
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(filled_count) + file_ext   
    
    # Construimos la ruta completa al fichero
    old_file_path = os.path.join(files_path, file)
    # En este caso estamos dejando los ficheros en el mismo directorio, 
    # pero podríamos moverlos a otro
    new_file_path = os.path.join(files_path, new_file)

    # Renombramos
    os.replace(old_file_path, new_file_path)
```

¿Qué pasa si, cuando el usuario escribe el nuevo nombre de los ficheros, no añade {} en ninguna parte?

En ese caso, tal y como hemos programado el script, la función `format()` no añadirá ningún número al nombre y todos nuestros ficheros se llamarán igual. Entonces, al intentar renombrar a un nombre que ya existe, puede pasar que nos dé un error o que sobreescribamos el fichero anterior (dependiendo del sistema operativo). 

Para solucionar esto, si nos fijamos, hemos incluido en nuestro script la siguiente línea:


```python
# Si el patrón del nombre proporcionado no contiene {}, se lo añadimos al final
name_pattern = name if '{}' in name else name + '_{}'
```

Esta es la forma "pythonista" de hacer algo equivalente al operador ternario. Y es bastante más legible...

"La variable `name_pattern` valdrá `name` si hay '{}' dentro de `name`, o, en caso contrario, valdrá `name` seguido de '\_{}'".

#### Argumentos en la llamada
Hay distintas formas de "procesar" los datos que pasamos como argumentos al ejecutar nuestro script. Una de ellas, es utilizando el módulo `argparse` que, además, nos facilita varias tareas como indicar si nuestros argumentos son obligatorios o no, de qué tipo tienen que ser, qué texto de ayuda hay que proporcionar al usuario si no sabe cómo ejecutar nuestro script, etc.

Por ejemplo, en nuestro caso, queremos parsear o procesar dos argumentos: uno correspondiente a la ruta (*path*) y otro al nuevo nombre de los ficheros (*name*). En el siguiente código vemos cómo podríamos configurar nuestro *parseador* de argumentos con los parámetros básicos:


```python
import argparse

# Creamos un parseador para los argumentos de entrada
parser = argparse.ArgumentParser(description='Renombrado de ficheros')
parser.add_argument('-p', '--path',
                    required=True,
                    type=str,
                    help='Ruta al directorio donde se encuentran los ficheros')
parser.add_argument('-n', '--name',
                    required=True,
                    type=str,
                    help='Nuevo nombre para los ficheros. Incluye {} donde quieras que vaya el número')
args = parser.parse_args()
print (args.path)
print (args.name)
```

Una vez que hemos visto que esto funciona, lo incorporamos a nuestro código:


```python
import os
from math import log10, ceil
import argparse

parser = argparse.ArgumentParser(description='Renombrado de ficheros')
parser.add_argument('-p', '--path',
                    required=True,
                    type=str,
                    help='Ruta al directorio donde se encuentran los ficheros')
parser.add_argument('-n', '--name',
                    required=True,
                    type=str,
                    help='Nuevo nombre para los ficheros. Incluye {} donde quieras que vaya el número')
args = parser.parse_args()

files_path = args.path

# Si el patrón del nombre proporcionado no contiene {}, se lo añadimos al final 
name_pattern = args.name if '{}' in args.name else args.name + '_{}'

# Obtenemos el listado de ficheros en el directorio indicado
files_in_dir = os.listdir(files_path)

# Obtenemos el número de dígitos a partir del número de ficheros
num_digits = ceil(log10(len(files_in_dir))) 

for count, file in enumerate(sorted(files_in_dir)):
    file_name, file_ext = os.path.splitext(file)
    
    # Convertimos el contador al string precedido de los ceros necesarios
    # Le añadimos 1 porque enumerate empieza a contar desde 0
    filled_count = str(count + 1).rjust(num_digits, '0')
    
    # Construimos el nuevo nombre de fichero con la función format
    new_file = name_pattern.format(filled_count) + file_ext   
    
    # Construimos la ruta completa al fichero
    old_file_path = os.path.join(files_path, file)
    # En este caso estamos dejando los ficheros en el mismo directorio, 
    # pero podríamos moverlos a otro
    new_file_path = os.path.join(files_path, new_file)

    # Renombramos
    os.replace(old_file_path, new_file_path)
```

### Sigamos aprendiendo
Hay muchas otras mejoras que se pueden añadir al script... ¿te atreves a buscarlas por tu cuenta?
+ Lo más importante es la gestión de errores: qué pasa, por ejemplo, si la ruta indicada no existe. **Investiga la sentencia `try... except...`**
+ También podemos querer mover los ficheros a una nueva carpeta, con otro nombre. O renombrar los ficheros teniendo en cuenta su fecha de creación o de modificación. **Investiga el módulo `os` y todas las funcionalidades que tiene.**
+ Estaría muy bien tener una interfaz gráfica que nos permitiera seleccionar la ruta a los ficheros. O incluso con un campo para escribir el nuevo nombre. **Investiga el módulo `tkinter`** (puede requerir instalar algún programa o paquete)
