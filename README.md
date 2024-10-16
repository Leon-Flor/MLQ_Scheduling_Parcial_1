# Algoritmo MLQ (Multi-Level Queue Scheduling)

Este repositorio contiene la implementación del algoritmo de planificación Multi-Level Queue (MLQ), utilizando el paradigma de programación orientada a objetos en Python. El objetivo del proyecto es simular la planificación de procesos en un sistema operativo utilizando colas multinivel con diferentes políticas de planificación, como Round Robin (RR), Shortest Job First (SJF), y First Come First Served (FCFS).

## Información del estudiante

- **Nombre**: León Alejandro Flor Sandoval
- **Universidad**: Universidad del Valle
- **Semestre**: Tercer semestre de Tecnología en Desarrollo de Software
- **Código de estudiante**: 2342924-2724

## Descripción del Proyecto

El algoritmo MLQ agrupa los procesos en diferentes colas de acuerdo con su prioridad. Cada cola puede tener diferentes políticas de planificación, y el algoritmo se encarga de despachar los procesos de manera ordenada respetando las prioridades y políticas de cada cola.

### Objetivos:

1. **Evidenciar problemas** de ejecución concurrente y discutir mecanismos para mitigar estos problemas a nivel de sistemas operativos.
2. **Comparar y contrastar** algoritmos de planificación expropiativa y no expropiativa de procesos.
3. **Aplicar la lógica** de los algoritmos de planificación a otros dominios como agendamiento en redes y planificación de proyectos.

### Especificaciones:

- **Entradas**: Archivos de texto con una lista de procesos que incluyen datos como el identificador del proceso, tiempo en CPU requerido, tiempo de llegada, cola de prioridad, y prioridad dentro de su cola.
- **Salidas**: Archivo de texto con los tiempos de espera, tiempos de finalización, tiempos de respuesta, y Turnaround Time para cada proceso, así como los promedios de estas métricas.

### Estructura de las entradas:

Cada archivo de entrada tiene el siguiente formato:
```

# Archivo: mlq001.txt

Etiqueta; Burst Time (BT); Arrival Time (AT); Queue (Q); Priority (Pr)
A;6;0;1;5
B;9;0;1;4
C;10;0;2;3
D;15;0;2;3
E;8;0;3;2

```

### Estructura de las salidas:
La salida es un archivo con el siguiente formato:

```

# Archivo: salida_mlq001.txt

Etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT
A;6;0;1;5;3;9;0;9
B;9;0;1;4;6;15;3;15
C;10;0;2;3;20;30;15;30
D;15;0;2;3;25;40;20;40
E;8;0;3;2;40;48;40;48
WT=23.5; CT=35.5; RT=19.5; TAT=35.5;

````

## Requisitos

- **Lenguaje de programación**: Python 3.x
- **Librerías**:
  - `tabulate`: Para formatear los resultados en forma de tabla en la salida por consola.

  Para instalar la librería `tabulate`, ejecuta el siguiente comando:

  ```bash
  pip install tabulate
````

## Estructura del proyecto

```bash
├── main.py                # Archivo principal donde se implementa el algoritmo MLQ
├── mlq_scheduling.py       # Módulo con la implementación del algoritmo MLQ
├── process.py             # Módulo que define la clase Process
├── input_files            # Carpeta que contiene los archivos de entrada
│   └── mlq001.txt         # Archivo de entrada de ejemplo
├── output_files           # Carpeta donde se guardan los archivos de salida
│   └── salida_mlq001.txt  # Archivo de salida generado
├── README.md              # Documentación del proyecto
```

## Ejecución del Proyecto

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd tu_repositorio
   ```

3. Asegúrate de tener instalado Python 3 y las dependencias necesarias. Instala `tabulate` si aún no lo tienes:

   ```bash
   pip install tabulate
   ```

4. Ejecuta el script principal para correr el simulador de MLQ:

   ```bash
   python main.py
   ```

5. El programa leerá los archivos de entrada en la carpeta `input_files` y generará los resultados en la carpeta `output_files`.

## Ejemplo de Salida por Consola

El resultado de la ejecución del programa se muestra también en la consola en forma de tabla:

```
+-----------+----+----+---+----+----+----+----+-----+
| Etiqueta  | BT | AT | Q | Pr | WT | CT | RT | TAT |
+-----------+----+----+---+----+----+----+----+-----+
|     A     |  6 |  0 | 1 |  5 |  3 |  9 |  0 |  9  |
|     B     |  9 |  0 | 1 |  4 |  6 | 15 |  3 |  15 |
|     C     | 10 |  0 | 2 |  3 | 20 | 30 | 15 |  30 |
|     D     | 15 |  0 | 2 |  3 | 25 | 40 | 20 |  40 |
|     E     |  8 |  0 | 3 |  2 | 40 | 48 | 40 |  48 |
+-----------+----+----+---+----+----+----+----+-----+

Promedios:
WT promedio: 23.5
CT promedio: 35.5
RT promedio: 19.5
TAT promedio: 35.5
```

## Video Explicativo

Un video con la explicación de la implementación y la ejecución de los archivos de entrada se puede encontrar en el siguiente enlace:

[Link al video explicativo](https://link_a_tu_video.com)

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
