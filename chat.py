import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLineEdit, QTextEdit, QListWidget #type: ignore
from PyQt5.QtCore import QRect, QSize #type:ignore
from PyQt5.QtGui import QPixmap #type:ignore

class ChatApp(QMainWindow):
    style = '''
                #room_name{
                    background-color: #ffffff;
                    height: 35px;
                    margin: 0 80px;
                    transform: translateY(-100px);
                    border-radius: 10px;
                    padding: 0 10px;
                }
                #room_pass{
                    background-color: #ffffff;
                    height: 35px;
                    margin: 0 80px;
                    border-radius: 10px;
                    padding: 0 10px;
                }
                #room_label{
                    margin: 0px 48px;
                    padding: 0px 60px;
                    color: #333333;
                    font-size: 27px;
                }
                #create_room{
                    height: 35px;
                    margin: 0 80px;
                    border: none;
                    border-radius: 5px;
                    background-color: #1995ad;
                    color: #333;
                }
                #create_room:hover{
                    background-color: #1989ad;
                    color: #fff;
                }
                #create_room_layout{
                    background-color: #a1d6e2;
                    margin: 50px;
                    padding: 0 30px;
                    border: none;
                    border-radius: 10px;
                }
                #window{
                    background-color: #1995ad;
                }
                #send{
                    height: 30px;
                    width: 100px;
                    border: none;
                    border-radius: 5px;
                    background-color: white;
                    color: #333333;
                }
                #send:hover{
                    background-color: #333;
                    color: #fff;
                }
                #messagebody{
                    height: 30px;
                    width: 350px;
                    border: none;
                    border-radius: 5px;
                    padding: 0px 5px;
                }
                #image{
                    height: 300px;
                    width: 300px;
                    border-radius: 10px;
                    margin: 90px 90px;
                    border-image: url("img.jpg");
                }
                #users{
                    width: 500px;
                    margin-right: 500px;
                }
                #u_label{
                    background-color: #fff;
                    border: none;
                    font-size: 20px;
                    border-radius: 5px;
                    padding-left: 5px;
                    color: #333333;
                }
                #u_list{
                   
                }
            '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chatteau')
        #self.setGeometry(100, 100, 1000, 400)
        self.setMinimumSize(1000, 400)
        self.setObjectName('window')

        self.InitializeUI()

    def InitializeUI(self):
        ###### AREA FOR MESSAGE DISPLAY
        self.messageDisplay = QTextEdit(self)
        self.messageDisplay.setFocusPolicy(False)
        self.messageDisplay.setStyleSheet('border-radius: 10px; padding: 5px; color: #333333; width: 2px; border: none; background-color: #a1d6e2; height: 200px;')

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
        
        self.users_label = QLabel(self)
        self.users_label.setText('Members')
        self.users_label.resize(30, 50)
        self.users_label.setObjectName('u_label')

        self.user_list = QListWidget(self)
        self.user_list.addItem('hello')
        self.user_list.setObjectName('u_list')
        #self.user_list.resize(200, 200)

        self.users = QVBoxLayout(self)
        self.users.setGeometry(QRect(20, 50, 300, 100))
        self.users.addWidget(self.users_label)
        self.users.setSpacing(5)
        self.users.addWidget(self.user_list)
        self.users.addStretch()
        self.users.setObjectName('users')

        self.room_label = QLabel(self)
        self.room_label.setText('Create Room Details')
        self.room_label.setObjectName('room_label')

        self.room_name = QLineEdit(self)
        self.room_name.setObjectName('room_name')
        self.room_name.setPlaceholderText('Room name')

        self.room_pass = QLineEdit(self)
        self.room_pass.setObjectName('room_pass')
        self.room_pass.setEchoMode(QLineEdit.Password)
        self.room_pass.setPlaceholderText('Room passcode')

        self.create_room = QPushButton(self)
        self.create_room.setText('Create')
        self.create_room.resize(200, 30)
        self.create_room.setObjectName('create_room')
        self.create_room.clicked.connect(self.createRoom)

        self.mini_layout = QHBoxLayout(self)
        self.mini_layout.setGeometry(QRect(0, 0, 500, 400))
        self.mini_layout.addWidget(self.messageBody)
        self.mini_layout.setObjectName('mini_layout')
        self.mini_layout.addWidget(self.send)

        self.layout = QVBoxLayout(self)
        self.layout.setGeometry(QRect(0, 0, 500, 400))
        self.layout.addWidget(self.messageDisplay)
        self.layout.setSpacing(10)
        self.layout.addLayout(self.mini_layout)

        self.chat_layout = QHBoxLayout()
        self.chat_layout.addLayout(self.users)
        self.chat_layout.setSpacing(50)
        self.chat_layout.addLayout(self.layout)
        self.chat_layout.setObjectName('chat_layout')

        self.image = QPushButton(self)
        self.image.setObjectName('image')
        self.image.setGeometry(QRect(0, 0, 300, 300))

        self.create_room_layout = QVBoxLayout(self)
        self.create_room_layout.addSpacing(100)
        self.create_room_layout.addWidget(self.room_label)
        self.create_room_layout.addSpacing(50)
        self.create_room_layout.addWidget(self.room_name)
        self.create_room_layout.addWidget(self.room_pass)
        self.create_room_layout.addWidget(self.create_room)
        self.create_room_layout.addSpacing(200)

        self.room_create_layout = QHBoxLayout(self)
        self.room_create_layout.setGeometry(QRect(50, 50, 900, 300))
        self.room_create_layout.addLayout(self.create_room_layout)
        self.room_create_layout.addWidget(self.image)

        self.room_auth = QWidget(self)
        self.room_auth.setLayout(self.room_create_layout)
        self.room_auth.setObjectName('create_room_layout')

        self.chat_room = QWidget(self)
        self.chat_room.setLayout(self.chat_layout)
        self.chat_room.setObjectName('chat_room')

        self.display = QStackedWidget(self)
        self.display.setObjectName('display')
        self.display.addWidget(self.room_auth)
        self.display.addWidget(self.chat_room)
        self.display.setCurrentWidget(self.room_auth)
        self.display.setGeometry(0,0, 1000, 400)
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

    def createRoom(self):
        if self.room_name != '' and self.room_pass != '':
            requests.post('http://127.0.0.1:8000/api/rooms', data={'room_name': self.room_name.text(), 'room_pass': self.room_pass.text()})
        self.room_name.clear()
        self.room_pass.clear()

app = QApplication(sys.argv)
app.setStyleSheet(ChatApp.style)
window = ChatApp()
window.show()
sys.exit(app.exec_())