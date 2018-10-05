
## 1. Construyendo nuestro "edificio"

Vamos a crear un "edificio" con dos personas:


```python
neighbours = ["Antonia", "Francisca"]
```

Uy, me he equivocado con el nombre de la de la planta baja...


```python
neighbours[0] = "Angustias"
```

Con lo que hemos aprendido, ¿podrías crear un "edificio" con 6 vecinos?


```python

```

Ahora resulta que la del 4º se ha mudado y hay que cambiar el nombre por uno nuevo... 


```python

```

Investiga cómo añadir otro vecino más o una lista de vecinos

## 2. Aprendiendo a saludar

Podríamos dejarles un mensaje escrito en el buzón...


```python
print('Hola')
```

Pero es mucho más divertido hacerlo a viva voz...

Calentamos las cuerdas vocales


```python
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'es')
```

Y saludamos


```python
engine.say('Hola')   
engine.runAndWait()
```

En ambos casos, querré decir el nombre después del saludo...


```python
'Hola {0}'.format('Antonia')
```

¡Estupendo! ¿Sabrías combinar lo que hemos aprendido para saludar a Antonia tanto por escrito como de viva voz?


```python

```

## 3. Automatizando una tarea repetitiva...

Así podemos recorrer la lista de vecinos e imprimir el nombre de cada uno


```python
for neighbour in neighbours:
    print(neighbour)
```

¿Sabrías combinarlo con todo lo aprendido anteriormente para escribir un programa que salude a todos los vecinos por escrito y en voz?


```python

```
