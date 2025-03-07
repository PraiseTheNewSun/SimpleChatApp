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
                    margin: 0px 20px;
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
                #auth_label{
                    margin: 0px 48px;
                    padding: 0px 60px;
                    color: #333333;
                    font-size: 27px;
                }
                #r_title{
                    color: #333333;
                    font-size: 27px;
                    font-style: italic;
                    font-weight: 3;
                }
                #back{
                    font-size: 50px;
                    height: 50px;
                    width: 50px;
                    margin-left: 450px;
                    border-radius: 25px;
                    background-color: #a1d6e2;
                    padding: 0 5px 5px 0;
                    color: #333333;
                }
                #back:hover{
                    background-color: #ffffff;
                }
                #or{
                    margin: 0 230px;
                }
                #or_create{
                    margin: 0 80px;
                    background-color: transparent;
                    text-decoration: underline;
                    color: blue;
                    border: none;
                }
                #or_create:hover{
                    color: purple;
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

        # THE FIELD HOLDING ROOM NAME
        self.hideRoom = QLineEdit(self)
        self.hideRoom.setGeometry(50, 315, 290, 35)
        self.hideRoom.setObjectName('messagebody')
        self.hideRoom.hide()

        ##### BUTTON TO SEND THE TYPED MESSAGE
        self.send = QPushButton(self)
        self.send.setText('Send')
        self.send.setGeometry(350, 315, 100, 35)
        self.send.clicked.connect(self.sendMessage)
        self.send.setObjectName('send')

        # THE TEXT SHOWN ON THE CREATE ROOM PAGE
        self.room_label = QLabel(self)
        self.room_label.setText('Create Room Details')
        self.room_label.setObjectName('room_label')

        # THE TEXT SHOWN ON THE ROOM AUTHENTICATION OR LOGIN PAGE
        self.auth_label = QLabel(self)
        self.auth_label.setText('Log In to Room')
        self.auth_label.setObjectName('auth_label')

        self.roomTitle = QLabel(self)
        #self.roomTitle.setText(f'Welcome to {self.room_name_auth.text()} Chat Room,')
        self.roomTitle.setObjectName('r_title')

        self.back = QPushButton(self)
        self.back.setText('<')
        self.back.setObjectName('back')
        self.back.clicked.connect(self.returnToLogin)

        self.head = QHBoxLayout(self)
        self.head.addWidget(self.roomTitle)
        self.head.addWidget(self.back)

        # THE AREA TO INPUT ROOM NAME
        self.room_name = QLineEdit(self)
        self.room_name.setObjectName('room_name')
        self.room_name.setPlaceholderText('Room name')

        # THE AREA TO INPUT ROOM PASSCODE
        self.room_pass = QLineEdit(self)
        self.room_pass.setObjectName('room_pass')
        self.room_pass.setEchoMode(QLineEdit.Password)
        self.room_pass.setPlaceholderText('Room passcode')

        # BUTTON TO TRIGGER THE ROOM CREATION PROCESS
        self.create_room = QPushButton(self)
        self.create_room.setText('Create')
        self.create_room.resize(200, 30)
        self.create_room.setObjectName('create_room')
        self.create_room.clicked.connect(self.createRoom)

        # THE AREA TO INPUT ROOM NAME FOR AUTHENTICATION
        self.room_name_auth = QLineEdit(self)
        self.room_name_auth.setObjectName('room_name')
        self.room_name_auth.setPlaceholderText('Room name')

        # THE AREA TO INPUT ROOM PASSCODE FOR AUTHENTICATION
        self.room_pass_auth = QLineEdit(self)
        self.room_pass_auth.setObjectName('room_pass')
        self.room_pass_auth.setEchoMode(QLineEdit.Password)
        self.room_pass_auth.setPlaceholderText('Room passcode')

        # BUTTON TO TRIGGER LOG IN
        self.login = QPushButton(self)
        self.login.setText('Log In')
        self.login.resize(200, 30)
        self.login.setObjectName('create_room')
        self.login.clicked.connect(self.roomAuth)

        self.Or = QLabel('Or') 
        self.Or.setObjectName('or')

        self.orCreate = QPushButton('create room here')
        self.orCreate.setObjectName('or_create')
        self.orCreate.clicked.connect(self.returnToCreate)

        # THE LAYOUT THAT ENCOMPASSES THE AREA TO INPUT MESSAGE AND THE SEND BUTTON
        self.mini_layout = QHBoxLayout(self)
        self.mini_layout.setGeometry(QRect(0, 0, 500, 400))
        self.mini_layout.addWidget(self.messageBody)
        self.mini_layout.setObjectName('mini_layout')
        self.mini_layout.addWidget(self.send)
        
        # THE LAYOUT FOR THE CHAT DISPLAY
        self.layout = QVBoxLayout(self)
        self.layout.setGeometry(QRect(0, 0, 500, 400))
        self.layout.addLayout(self.head)
        self.layout.addWidget(self.messageDisplay)
        self.layout.setSpacing(10)
        self.layout.addLayout(self.mini_layout)

        # THE LAYOUT THAT HOUSES THE ENTIRE WIDGETS AND LAYOUT OF THE CHAT PAGE
        self.chat_layout = QHBoxLayout()
        self.chat_layout.setSpacing(50)
        self.chat_layout.addLayout(self.layout)
        self.chat_layout.setObjectName('chat_layout')

        # IMAGE TO BE DISPLAYED ON THE ROOM CREATION AND ROOM AUTHENTICATION PAGE
        self.image = QPushButton(self)
        self.image.setObjectName('image')
        self.image.setGeometry(QRect(0, 0, 300, 300))

        # THE LAYOUT THAT HOUSES THE INPUT FIELDS FOR ROOM DETAILS AND CREATE BUTTON
        self.create_room_layout = QVBoxLayout(self)
        self.create_room_layout.addSpacing(250)
        self.create_room_layout.addWidget(self.room_label)
        self.create_room_layout.addSpacing(30)
        self.create_room_layout.addWidget(self.room_name)
        self.create_room_layout.addWidget(self.room_pass)
        self.create_room_layout.addWidget(self.create_room)
        self.create_room_layout.addSpacing(200)

        # THE LAYOUT THAT HOUSES ALL WIDGETS AND LAYOUTS OF THE ROOM CREATION PAGE
        self.room_create_layout = QHBoxLayout(self)
        self.room_create_layout.setGeometry(QRect(50, 50, 900, 300))
        self.room_create_layout.addLayout(self.create_room_layout)
        self.room_create_layout.addWidget(self.image)

        # THE LAYOUT THAT HOUSES THE INPUT FIELDS FOR ROOM AUTHENTICATION
        self.room_auth_layout = QVBoxLayout(self)
        self.room_auth_layout.addSpacing(100)
        self.room_auth_layout.addWidget(self.auth_label)
        self.room_auth_layout.addSpacing(50)
        self.room_auth_layout.addWidget(self.room_name_auth)
        self.room_auth_layout.addWidget(self.room_pass_auth)
        self.room_auth_layout.addWidget(self.login)
        self.room_auth_layout.addWidget(self.Or)
        self.room_auth_layout.addWidget(self.orCreate)
        self.room_auth_layout.addSpacing(200)

        # THE LAYOUT THAT HOUSES ALL WIDGETS AND LAYOUTS OF THE ROOM AUTHENTICATION PAGE
        self.auth_layout = QHBoxLayout(self)
        self.auth_layout.setGeometry(QRect(50, 50, 900, 300))
        self.auth_layout.addLayout(self.room_auth_layout)
        self.auth_layout.addWidget(self.image)

        # ROOM CREATION WIDGET
        self.create = QWidget(self)
        self.create.setLayout(self.room_create_layout)
        self.create.setObjectName('create_room_layout')

        # CHAT ROOM WIDGET
        self.chat_room = QWidget(self)
        self.chat_room.setLayout(self.chat_layout)
        self.chat_room.setObjectName('chat_room')

        # ROOM AUTHENTICATION WIDGET
        self.auth = QWidget(self)
        self.auth.setLayout(self.auth_layout)
        self.auth.setObjectName('create_room_layout')

        # THE WIDGET THAT STORES ALL THE PAGE WIDGETS IN STACKS
        self.display = QStackedWidget(self)
        self.display.setObjectName('display')
        self.display.addWidget(self.create)
        self.display.addWidget(self.chat_room)
        self.display.addWidget(self.auth)
        self.display.setCurrentWidget(self.auth)
        self.display.setGeometry(0,0, 1000, 400)
        self.display.show()

        self.gettingMessages()

    # THE FUNCTION THAT SENDS MESSAGE TO API
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

    # THE FUNCTION THAT GETS STORED MESSAGES FROM THE API
    def gettingMessages(self):
        data = requests.get('http://127.0.0.1:8000/api/messages')
        for i in data.json()['data']:
            self.messageDisplay.append(f'{i['author']}:   {i['body']}\n')

    # HANDLES SENDING ROOM DETAILS OF ROOMS TO BE CREATED TO THE API
    def createRoom(self):
        if self.room_name != '' and self.room_pass != '':
            requests.post('http://127.0.0.1:8000/api/rooms', data={'room_name': self.room_name.text(), 'room_pass': self.room_pass.text()})
        self.room_name.clear()
        self.room_pass.clear()

    def roomAuth(self):
        if self.room_name_auth != '' and self.room_pass_auth != '':
            room = requests.get('http://127.0.0.1:8000/api/rooms', data={'room_name': self.room_name_auth.text(), 'room_pass': self.room_pass_auth.text()})
            if room:
                self.display.setCurrentWidget(self.chat_room)
                self.roomTitle.setText(f'Welcome to {self.room_name_auth.text()} Chat Room,')

    def returnToLogin(self):
        self.display.setCurrentWidget(self.auth)

    def returnToCreate(self):
        self.display.setCurrentWidget(self.create)

app = QApplication(sys.argv)
app.setStyleSheet(ChatApp.style)
window = ChatApp()
window.show()
sys.exit(app.exec_())