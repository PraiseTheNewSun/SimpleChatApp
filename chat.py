import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLineEdit, QTextEdit #type: ignore
from PyQt5.QtCore import QRect #type:ignore

class ChatApp(QMainWindow):
    style = '''
                #room_name{
                    background-color: #ffffff;
                    height: 35px;
                    width: 290px;
                }
                #create_room{
                    height: 30px;
                    width: 100px
                }
                #create_room_layout{
                    padding: 50px;
                }
                #window{
                    padding: 50px;
                    border-radius: 25px;
                    background-color: #a1d6e2;
                }
            '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chatteau')
        self.setGeometry(100, 100, 500, 400)
        self.setObjectName('window')

        self.InitializeUI()

    def InitializeUI(self):
        ###### AREA FOR MESSAGE DISPLAY
        self.messageDisplay = QTextEdit(self)
        self.messageDisplay.setFocusPolicy(False)
        self.messageDisplay.setStyleSheet('border-radius: 5px; color: red; width: 100%;')

        ##### AREA TO TYPE MESSAGE
        self.messageBody = QLineEdit(self)
        self.messageBody.setGeometry(50, 315, 290, 35)
        self.messageBody.setObjectName('messagebody')

        ##### BUTTON TO SEND THE TYPED MESSAGE
        self.send = QPushButton(self)
        self.send.setText('Send')
        self.send.setGeometry(350, 315, 100, 35)
        self.send.clicked.connect(self.sendMessage)
        self.send.setObjectName('send')

        self.room_label = QLabel(self)
        self.room_label.setText('Python programming')
        self.room_label.resize(300, 35)

        self.room_name = QLineEdit(self)
        self.room_name.setObjectName('room_name')

        self.room_pass = QLineEdit(self)
        self.room_pass.setObjectName('room_pass')

        self.create_room = QPushButton(self)
        self.create_room.setText('Create room')
        self.create_room.resize(200, 30)
        self.create_room.setObjectName('create_room')

        self.mini_layout = QHBoxLayout(self)
        self.mini_layout.setGeometry(QRect(0, 0, 500, 400))
        self.mini_layout.addWidget(self.messageBody)
        self.mini_layout.addWidget(self.send)

        self.layout = QVBoxLayout(self)
        self.layout.setGeometry(QRect(0, 0, 500, 400))
        self.layout.addWidget(self.messageDisplay)
        self.layout.addLayout(self.mini_layout)

        self.create_room_layout = QVBoxLayout(self)
        self.create_room_layout.setObjectName('create_room_layout')
        self.create_room_layout.addWidget(self.room_label)
        self.create_room_layout.addWidget(self.room_name)
        self.create_room_layout.addWidget(self.room_pass)
        self.create_room_layout.addWidget(self.create_room)

        self.room_auth = QWidget(self)
        self.room_auth.setLayout(self.create_room_layout)
        self.room_auth.setObjectName('create_room_layout')

        self.chat_room = QWidget(self)
        self.chat_room.setLayout(self.layout)
        self.chat_room.setObjectName('chat_room')

        self.display = QStackedWidget(self)
        self.display.setObjectName('display')
        self.display.addWidget(self.room_auth)
        self.display.addWidget(self.chat_room)
        self.display.setCurrentWidget(self.chat_room)
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
app.setStyleSheet(ChatApp.style)
window = ChatApp()
window.show()
sys.exit(app.exec_())