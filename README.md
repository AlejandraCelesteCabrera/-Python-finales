# Clase 09 python

## > Abrir la terminal de Git Bash o terminal en Linux, debe ser como administrador en Window
### > Creamos una carpeta o directorio:
* mkdir python-final
* Entramos en ella:
* cd python-final
* Iniciamos el repositorio:
* git init

## >Creamos un archivo:
* toque finales.py

## >Abrimos VSC:
* código .

## >En la terminal ingresamos el comando para saber la versión de Python que tenemos instalada:
* Python -V
* python3 -V

## >Creamos el entorno virtual en Python:
* python3 -m venv venv #Creamos el entorno virtual

## >Activamos el entorno virtual:
* source venv/bin/activate #Activamos el entorno virtual en Linux
* venv/scripts/activate #En Windows

## >Hacemos actualización del pip de Python
* python3 -m pip install --upgrade pip #Actualizamos el pip

## Investigar ¿Qué es el pip y porque lo actualizamos?
>"Trabajo práctico de python"
### ¿Para qué sirve pip?


>Cuando programas en Python, muchas veces necesitas herramientas que otras personas ya crearon para no escribir código desde cero (por ejemplo, para conectar con una base de datos, analizar datos o crear una página web).
 > pip se conecta automáticamente al repositorio oficial Python Package Index (PyPI), descarga la librería que le pidas y la configura en tu computadora al instante.
 > Una de sus mayores ventajas es la gestión de dependencias: si la librería que quieres instalar necesita de otras tres librerías para funcionar,pip las detecta y las instala todas por ti de manera automática.Comandos más utilizadospip se ejecuta desde la terminal de comandos (Consola, CMD o Terminal) y utiliza instrucciones muy sencillas:Instalar un paquete:pip install nombre_del_paquete(Por ejemplo:pip install requests para descargar una librería de peticiones web)Desinstalar un paquete:pip uninstall nombre_del_paqueteActualizar un paquete a su última versión:pip install --upgrade nombre_del_paqueteVer qué paquetes tienes instalados:pip listInstalar múltiples dependencias desde un archivo:pip install -r requirements.txt(Muy útil para compartir proyectos, ya que este archivo de texto lista todas las herramientas necesarias de golpe).A partir de las versiones de Python 3.4 en adelante, pip ya viene preinstalado automáticamente. 
 >En algunos sistemas(como Linux o macOS), es posible que debas invocarlo escribiendo pip3 en lugar de pip para asegurar que estás interactuando con la versión de Python 3.Si estás comenzando con un proyecto, te puedo explicar cómo crear un entorno virtual para usar pip de forma limpia y ordenada,o enseñarte a estructurar tu propio archivo requirements.txt. 

### Tarea
* Hacer al primer commit de este trabajo y unirlo al repositorio remoto.
* Enviar el enlace del repositorio remoto donde tiene que tener un README.md con todos los detalles de lo que les fui mostrando en comandos, y la respuesta del punto 11 de más arriba.