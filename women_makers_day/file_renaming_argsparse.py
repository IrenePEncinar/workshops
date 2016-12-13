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
