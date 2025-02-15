import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QTextEdit

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chatteau')
        self.setGeometry(100, 100, 500, 400)

        self.InitializeUI()
    
    def InitializeUI(self):

        ###### AREA FOR MESSAGE DISPLAY
        self.messageDisplay = QTextEdit(self)
        self.messageDisplay.setGeometry(50, 50, 400, 245)

        ##### AREA TO TYPE MESSAGE
        self.messageBody = QLineEdit(self)
        self.messageBody.setGeometry(50, 315, 290, 35)

        ##### BUTTON TO SEND THE TYPED MESSAGE
        self.send = QPushButton(self)
        self.send.setText('Send')
        self.send.setGeometry(350, 315, 100, 35)
        self.send.clicked.connect(self.sendMessage)

    def sendMessage(self):
        print("message sent")
        self.messageDisplay.append(self.messageBody.text())
        self.messageBody.clear()

app = QApplication(sys.argv)
window = ChatApp()
window.show()
sys.exit(app.exec_())