"Trabajo práctico de python"
## ¿Para qué sirve pip?
Cuando programas en Python, muchas veces necesitas herramientas que otras personas ya crearon para no escribir código desde cero
 (por ejemplo, para conectar con una base de datos, analizar datos o crear una página web).
  pip se conecta automáticamente al repositorio oficial Python Package Index (PyPI), 
  descarga la librería que le pidas y la configura en tu computadora al instante.
  
  Una de sus mayores ventajas es la gestión de dependencias: si la librería que quieres instalar necesita de otras tres librerías para funcionar,
   pip las detecta y las instala todas por ti de manera automática.Comandos más utilizadospip se ejecuta desde la terminal de comandos 
   (Consola, CMD o Terminal) y utiliza instrucciones muy sencillas:Instalar un paquete:pip install nombre_del_paquete(Por ejemplo:
    pip install requests para descargar una librería de peticiones web)Desinstalar un paquete:pip uninstall nombre_del_paqueteActualizar un 
    paquete a su última versión:pip install --upgrade nombre_del_paqueteVer qué paquetes tienes instalados:pip listInstalar múltiples dependencias 
    desde un archivo:pip install -r requirements.txt(Muy útil para compartir proyectos, ya que este archivo de texto lista todas las herramientas 
    necesarias de golpe).A partir de las versiones de Python 3.4 en adelante, pip ya viene preinstalado automáticamente. 
    En algunos sistemas
     (como Linux o macOS), es posible que debas invocarlo escribiendo pip3 en lugar de pip para asegurar que estás interactuando con la versión 
     de Python 3.Si estás comenzando con un proyecto, te puedo explicar cómo crear un entorno virtual para usar pip de forma limpia y ordenada,
      o enseñarte a estructurar tu propio archivo requirements.txt. ¿Te gustaría ver un ejemplo de ello?