import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLineEdit, QTextEdit #type: ignore
from PyQt5.QtCore import QRect #type:ignore

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
        self.messageDisplay.setFocusPolicy(False)

        ##### AREA TO TYPE MESSAGE
        self.messageBody = QLineEdit(self)
        self.messageBody.setGeometry(50, 315, 290, 35)

        ##### BUTTON TO SEND THE TYPED MESSAGE
        self.send = QPushButton(self)
        self.send.setText('Send')
        self.send.setGeometry(350, 315, 100, 35)
        self.send.clicked.connect(self.sendMessage)

        self.room_name = QLineEdit(self)
        self.room_name.setGeometry(50, 183, 290, 35)
        self.room_pass = QLineEdit(self)
        self.room_pass.setGeometry(350, 183, 100, 35)

        self.mini_layout = QHBoxLayout(self)
        self.mini_layout.setGeometry(QRect(0, 0, 500, 400))
        self.mini_layout.addWidget(self.messageBody)
        self.mini_layout.addWidget(self.send)

        self.layout = QVBoxLayout(self)
        self.layout.setGeometry(QRect(0, 0, 500, 400))
        self.layout.addWidget(self.messageDisplay)
        self.layout.addLayout(self.mini_layout)

        self.create_room_layout = QVBoxLayout(self)
        self.create_room_layout.setGeometry(QRect(0, 0, 500, 200))
        self.create_room_layout.addWidget(self.room_name)
        self.create_room_layout.addWidget(self.room_pass)

        self.room_auth = QWidget(self)
        self.room_auth.setLayout(self.create_room_layout)

        self.chat_room = QWidget(self)
        self.chat_room.setLayout(self.layout)

        self.display = QStackedWidget(self)
        self.display.addWidget(self.room_auth)
        self.display.addWidget(self.chat_room)
        self.display.setCurrentWidget(self.room_auth)
        self.display.setGeometry(0,0, 500, 400)
        self.display.show()

        self.gettingMessages()

    def sendMessage(self):
        ##### SENDING MESSAGE TO API AND RE-APPENDING UPDATED DATA
        if self.messageBody.text() != '':
            requests.post('http://127.0.0.1:8000/api/messages', data={'author': 'Praise', 'body': self.messageBody.text()})
            data = requests.get('http://127.0.0.1:8000/api/messages')
            i = data.json()['data'][-1]
            self.messageDisplay.append(f'{i['author']}:   {i['body']}\n')
        else:
            pass
        
        self.messageBody.clear()

    def gettingMessages(self):
        data = requests.get('http://127.0.0.1:8000/api/messages')
        for i in data.json()['data']:
            self.messageDisplay.append(f'{i['author']}:   {i['body']}\n')

app = QApplication(sys.argv)
window = ChatApp()
window.show()
sys.exit(app.exec_())