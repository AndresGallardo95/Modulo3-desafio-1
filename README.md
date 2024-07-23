# Desafío Evaluado - Introducción a Python

Este repositorio contiene las soluciones a las actividades del desafío evaluado 1 en el curso de Introducción a Python. 
## Actividades

### Actividad 1 - Velocidad de Escape

La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un planeta venciendo la gravedad. La fórmula para calcular la velocidad de escape es:

\[ V_e = \sqrt{2gr} \]

- **Ve**: Velocidad de Escape en [m/s].
- **g**: Constante gravitacional en [m/s²].
- **r**: Radio del planeta en [m].

#### Script: `escape.py`

Este script solicita al usuario ingresar el radio del planeta (en kilómetros) y la constante gravitacional (en m/s²). Luego, calcula y muestra la velocidad de escape.

**Uso:**
1. Ejecutar el script `escape.py`.
2. Ingresar el radio en kilómetros y la constante gravitacional cuando se solicite.
3. El resultado mostrará la velocidad de escape en m/s.

#### Ejemplo de entrada:
Ingrese el radio en kilómetros (km): 6371
Ingrese la constante g en (m/s^2): 9.8


#### Ejemplo de salida:
La velocidad de escape es 11174.61 m/s




### Actividad 2 - Rentabilidad

Un emprendedor desea calcular las utilidades de su proyecto de entrega de comida para mascotas. Las utilidades se calculan usando la fórmula:

\[ \text{Utilidades} = P \times U - GT \]

- **P**: Precio de Suscripción
- **U**: Número de Usuarios
- **GT**: Gastos Totales

Esta actividad se desarrolla en tres versiones del script.

#### Versión 1: `emprendedor1.py`

Este script calcula las utilidades del proyecto solicitando al usuario el precio de suscripción, el número de usuarios y los gastos totales.

**Uso:**
1. Ejecutar el script `emprendedor1.py`.
2. Ingresar el precio de suscripción, número de usuarios y gastos totales cuando se solicite.
3. El resultado mostrará las utilidades del proyecto.

#### Versión 2: `emprendedor2.py`

Esta versión considera dos tipos de usuarios: normales y premium. Los usuarios premium pagan un 50% más por la suscripción.

**Uso:**
1. Ejecutar el script `emprendedor2.py`.
2. Ingresar el precio de suscripción para usuarios normales, número de usuarios normales y premium, y gastos totales.
3. El resultado mostrará las utilidades del proyecto.

#### Versión 3: `emprendedor3.py`

Esta versión calcula las utilidades actuales y compara con las utilidades del año anterior, mostrando la razón entre ambas.

**Uso:**
1. Ejecutar el script `emprendedor3.py`.
2. Ingresar el precio de suscripción, número de usuarios, gastos totales y utilidades del año anterior.
3. El resultado mostrará las utilidades actuales y la razón entre las utilidades actuales y las del año anterior.

### Requisitos

Para ejecutar los scripts, necesitas tener instalado Python 3 en tu sistema.

### Ejecución de los scripts

Para ejecutar cualquiera de los scripts, abre una terminal y navega al directorio donde se encuentran los archivos. Luego, ejecuta el script deseado con el comando:

```sh
python nombre_del_script.py


