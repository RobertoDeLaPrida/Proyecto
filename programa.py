import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QTextEdit
from PyQt5.QtCore import Qt

def ventana():
    app = QApplication(sys.argv)

    # Crear una ventana principal
    window = QMainWindow()
    window.setWindowTitle("Steam Data")
    window.setGeometry(100, 100, 1020, 600)

    # Crear un ComboBox
    combo_box = QComboBox(window)
    combo_box.addItem("Elije una opcion")  # placeholder
    combo_box.addItem("Top 100 juegos con mas jugadores en estas 2 semanas")
    combo_box.addItem("Top 100 juegos con mas jugadores desde el principio")
    combo_box.addItem("Top 100 juegos mas vendidos")
    combo_box.addItem("Todos los juegos")
    combo_box.setGeometry(0, 0, 400, 30)

    # Deshabilitar el placeholder
    combo_box.setItemData(0, 0, role=Qt.UserRole - 1)

    # Establecer la opción predeterminada seleccionada en el índice 0
    combo_box.setCurrentIndex(0)

    # Crear un área de texto
    text_area = QTextEdit(window)
    text_area.setGeometry(400, 0, 620, 600)
    text_area.setReadOnly(True)

    # Conectar el ComboBox a la función que maneja la selección
    combo_box.activated[str].connect(lambda text: compruebaOpcion(text, text_area))

    # Mostrar la ventana
    window.show()
    sys.exit(app.exec_())

def obtener_info_juego(juego):
    precio = juego.get('price', 'N/A')
    if precio == '0':
        precio_formateado = "Gratis"
    else:
        # Convertir el precio a entero y formatearlo en euros
        precio = int(precio)
        euros, centavos = divmod(precio, 100)
        precio_formateado = "{}'{}".format(euros, centavos)
    
    return {
        'Nombre': juego.get('name', 'N/A'),
        'Desarrollador': juego.get('developer', 'N/A'),
        'Publisher': juego.get('publisher', 'N/A'),
        'Jugadores': juego.get('owners', 'N/A'),
        'Precio': precio_formateado,
        'Descuento': "No se muestra"  # No mostrar el descuento
    }

def compruebaOpcion(opcion_seleccionada, text_area):
    url = 'https://steamspy.com/api.php'

    if opcion_seleccionada == "Top 100 juegos con mas jugadores en estas 2 semanas":
        params = {'request': 'top100in2weeks'}
    elif opcion_seleccionada == "Top 100 juegos con mas jugadores desde el principio":
        params = {'request': 'top100forever'}
    elif opcion_seleccionada == "Top 100 juegos mas vendidos":
        params = {'request': 'top100owned'}
    elif opcion_seleccionada == "Todos los juegos":
        params = {'request': 'all'}
    else:
        # Opción predeterminada (no válida), muestra un mensaje de error
        text_area.clear()
        text_area.insertPlainText("Opción no válida")
        return

    # Limpiar el área de texto antes de mostrar nueva información
    text_area.clear()

    # Realizar la solicitud a la API de SteamSpy
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Filtrar y formatear la información de los juegos
        juegos_info = [obtener_info_juego(juego) for juego in data.values()]

        # Mostrar los datos en el área de texto
        for juego_info in juegos_info:
            text_area.insertPlainText("Nombre: {}\n".format(juego_info['Nombre']))
            text_area.insertPlainText("Desarrollador: {}\n".format(juego_info['Desarrollador']))
            text_area.insertPlainText("Publisher: {}\n".format(juego_info['Publisher']))
            text_area.insertPlainText("Jugadores: {}\n".format(juego_info['Jugadores']))
            text_area.insertPlainText("Precio: {}\n".format(juego_info['Precio']))
            if juego_info['Precio'] != "Gratis":
                text_area.insertPlainText("Descuento: {}\n".format(juego_info['Descuento']))
            text_area.insertPlainText("\n---\n")  # Separador entre juegos
    else:
        text_area.clear()
        text_area.insertPlainText("Error al recuperar datos de SteamSpy")

ventana()
