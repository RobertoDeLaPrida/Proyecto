import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QTextEdit
from PyQt5.QtCore import Qt 

app = QApplication(sys.argv)

# Crear una ventana principal
window = QMainWindow()
window.setWindowTitle("Steam Data")
window.setGeometry(100, 100, 1020, 600)

# Crear un ComboBox
combo_box = QComboBox(window)
combo_box.addItem("Elije una opcion") #placeholder
combo_box.addItem("Top 100 juegos con mas jugadores en estas 2 semanas")
combo_box.addItem("Top 100 juegos con mas jugadores desde el principio")
combo_box.addItem("Top 100 juegos mas vendidos")
combo_box.addItem("Todos los juegos")
combo_box.setGeometry(0, 0, 400, 30)

#deshabilitar el placeholder
combo_box.setItemData(0, 0, role=Qt.UserRole - 1)

# Establecer la opción predeterminada seleccionada en el índice 0
combo_box.setCurrentIndex(0)

# Crear un area de texto
text_area= QTextEdit(window)
text_area.setGeometry(400, 0, 620, 600)
text_area.setDisabled(True)


# Mostrar la ventana
window.show()
sys.exit(app.exec_())
