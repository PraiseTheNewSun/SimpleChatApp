**ChatApp**

This is a solo project aimed at ehancing chat experience and security

**Key Features:** <br/>
1. Creating Chatrooms <br/>
2. Logging into chatrooms <br/>
3. Accessing chat room messages <br/>
4. Provision of passcode to ensure chat room security <br/>

`import sys`<br/>
`import requests`<br/>
`from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLineEdit, QTextEdit, QListWidget`<br/>
`from PyQt5.QtCore import QRect, QSize`<br/>
`from PyQt5.QtGui import QPixmap`<br/>

The code above imports the necessary classes for the application

`class ChatApp(QMainWindow):`

The code above creates a class instance that inherits from `QMainWindow` class. It just creates a window for our app and initializes the user interface
