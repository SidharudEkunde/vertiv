# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
#
#
# class LoginForm(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Login Form')
#         self.resize(500, 120)
#
#         layout = QGridLayout()
#
#         label_name = QLabel('<font size="4"> Username </font>')
#         self.lineEdit_username = QLineEdit()
#         self.lineEdit_username.setPlaceholderText('Please enter your username')
#         layout.addWidget(label_name, 0, 0)
#         layout.addWidget(self.lineEdit_username, 0, 1)
#
#         label_password = QLabel('<font size="4"> Password </font>')
#         self.lineEdit_password = QLineEdit()
#         self.lineEdit_password.setPlaceholderText('Please enter your password')
#         layout.addWidget(label_password, 1, 0)
#         layout.addWidget(self.lineEdit_password, 1, 1)
#
#         button_login = QPushButton('Login')
#         button_login.clicked.connect(self.check_password)
#         layout.addWidget(button_login, 2, 0, 1, 2)
#         layout.setRowMinimumHeight(2, 75)
#
#         self.setLayout(layout)
#
#     def check_password(self):
#         msg = QMessageBox()
#
#         if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
#             msg.setText('Success')
#             msg.exec_()
#             app.quit()
#         else:
#             msg.setText('Incorrect Password')
#             msg.exec_()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     form = LoginForm()
#     form.show()
#
#     sys.exit(app.exec_())


# # importing libraries
# from PyQt5.QtWidgets import *
# import sys
#
#
# # creating a class
# # that inherits the QDialog class
# class Window(QDialog):
#
#     # constructor
#     def __init__(self):
#         super(Window, self).__init__()
#
#         # setting window title
#         self.setWindowTitle("Python")
#
#         # setting geometry to the window
#         self.setGeometry(100, 100, 300, 400)
#
#         # creating a group box
#         self.formGroupBox = QGroupBox("Form 1")
#
#         # creating spin box to select age
#         self.ageSpinBar = QSpinBox()
#
#         # creating combo box to select degree
#         self.degreeComboBox = QComboBox()
#
#         # adding items to the combo box
#         self.degreeComboBox.addItems(["BTech", "MTech", "PhD"])
#
#         # creating a line edit
#         self.nameLineEdit = QLineEdit()
#
#         # calling the method that create the form
#         self.createForm()
#
#         # creating a dialog button for ok and cancel
#         self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
#
#         # adding action when form is accepted
#         self.buttonBox.accepted.connect(self.getInfo)
#
#         # adding action when form is rejected
#         self.buttonBox.rejected.connect(self.reject)
#
#         # creating a vertical layout
#         mainLayout = QVBoxLayout()
#
#         # adding form group box to the layout
#         mainLayout.addWidget(self.formGroupBox)
#
#         # adding button box to the layout
#         mainLayout.addWidget(self.buttonBox)
#
#         # setting lay out
#         self.setLayout(mainLayout)
#
#     # get info method called when form is accepted
#     def getInfo(self):
#         # printing the form information
#         print("Person Name : {0}".format(self.nameLineEdit.text()))
#         print("Degree : {0}".format(self.degreeComboBox.currentText()))
#         print("Age : {0}".format(self.ageSpinBar.text()))
#
#         # closing the window
#         self.close()
#
#     # creat form method
#     def createForm(self):
#         # creating a form layout
#         layout = QFormLayout()
#
#         # adding rows
#         # for name and adding input text
#         layout.addRow(QLabel("Name"), self.nameLineEdit)
#
#         # for degree and adding combo box
#         layout.addRow(QLabel("Degree"), self.degreeComboBox)
#
#         # for age and adding spin box
#         layout.addRow(QLabel("Age"), self.ageSpinBar)
#
#         # setting layout
#         self.formGroupBox.setLayout(layout)
#
#
# # main method
# if __name__ == '__main__':
#     # create pyqt5 app
#     app = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = Window()

# # showing the window
# window.show()
#
# # start the app
# sys.exit(app.exec())


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(600, 240)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 50)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()

    sys.exit(app.exec_())
