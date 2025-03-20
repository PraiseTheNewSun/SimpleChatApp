**ChatApp**

This application is for chatting. Rooms can be created with passcodes to improve chat security

`import sys`<br/>
`import requests`<br/>
`from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLineEdit, QTextEdit, QListWidget`<br/>
`from PyQt5.QtCore import QRect, QSize`<br/>
`from PyQt5.QtGui import QPixmap`<br/>

The code above imports the necessary classes for the application

`class ChatApp(QMainWindow):`

The code above creates a class instance that inherits from `QMainWindow` class. It just creates a window for our app
