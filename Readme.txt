Este proyeto se enfoca en la peticion y el procesamiento de datos  de una api no oficial de Steam, 
que es una plataforma online de venta de videojuegos. 

Para que funcione correctamente usaremos Python3, especificamente la version Python 3.9.5

Este programa requiere del uso de diferentes bibliotecas, para causar los menores dolores de cabezas solo tienes que ejecutar 'pip install -r requirements.txt'
En este archivo 'requirements.txt' contiene todas las bibliotecas necesarias y usadas en este programa.

Se debe de usar una api no oficial ya que la propia proveeida por Steam solo proporciona 
"appid" y "name" es decir el ID de el juego/aplicacion y su nombre.

Como en este programa se busca procesar una informacion mayor que simplemente el nombre y la id, he usado la api SteamSpy, que proporciona mayor alcance de datos
como puede ser, las ventas, el numero de jugadores, los precios, etc...

También se proporciona una barra de busqueda por si se desea buscar un juego en concreto.