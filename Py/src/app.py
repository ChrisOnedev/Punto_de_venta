
import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication
    ,QMainWindow
    ,QPushButton
    ,QLineEdit
    ,QLabel
    ,QVBoxLayout
    ,QWidget
)






# MAIN window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Xomo")
        self.setFixedSize(QSize(800, 500)) #TamaNo fijo de Window
        #self.setMaximumSize(QSize())

        #Button
        self.button = QPushButton("Press here")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_was_clicked)     
        #self.setCentralWidget(self.button) # Add Button   

        #Label
        self.label = QLabel()

        #InputEdit
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        #Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container) # Add Container



    def titleChanged(self):
        print("title changed")

    #Slot - Clicked button 
    def button_was_clicked(self):
        self.setWindowTitle("Kivu.inc")
        #self.button.setDisabled(True)




#=============================== Aplicacion ===================================#
app = QApplication(sys.argv)

# SHOW
window = MainWindow()
window.show()


#
app.exec()
