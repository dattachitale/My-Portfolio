import sys
import json
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
from PySide2.QtCore import QRect
from PySide2.QtGui import *
from pynput import *

with open('list.json', 'r') as list_file:
    data = json.load(list_file)

class My_Main_Dialog(QtWidgets.QWidget):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)
        self.setMinimumHeight(400)
        self.setMinimumWidth(500)
        self.create_widgets()
        self.create_layout()
        self.populate_states()


    def create_widgets(self):
        self.FirstName_lable = QtWidgets.QLabel('First Name')
        self.FirstName_lable.setMaximumWidth(60)
        self.first_name = QtWidgets.QLineEdit("")
        self.first_name.setMaximumWidth(150)
        self.first_name.setPlaceholderText("Enter Only String")
        self.regexp = QtCore.QRegExp("[a-z-A-Z]+")
        self.validator = QRegExpValidator(self.regexp)
        self.first_name.setValidator(self.validator)

        self.LastName_lable = QtWidgets.QLabel('Last Name')
        self.LastName_lable.setMaximumWidth(70)
        self.last_name = QtWidgets.QLineEdit("")
        self.last_name.setMaximumWidth(150)
        self.last_name.setPlaceholderText("Enter Only String")
        self.last_name.setValidator(self.validator)

        self.Lable_Gender = QtWidgets.QLabel("Gender")
        self.Lable_Gender.setMaximumWidth(40)
        self.Male_Gender = QtWidgets.QRadioButton("Male")
        self.Male_Gender.setMaximumWidth(60)
        self.Female_Gender = QtWidgets.QRadioButton("Female")

        #self.DOB_Lable = QtWidgets.QLabel("Your DOB")
        #self.DOB_Lable.setMaximumWidth(60)
        #self.DOB = QtWidgets.QCalendarWidget()
        #self.DOB.setMaximumWidth(100)
        #self.DOB.setMaximumHeight(100)

        self.Mobile_lable = QtWidgets.QLabel('Mobile Number')
        self.Mobile_lable.setMaximumWidth(80)
        self.Mobile_Number = QtWidgets.QLineEdit("")
        self.Mobile_Number.setMaximumWidth(150)
        self.Mobile_Number.setPlaceholderText("Enter Only Numbers")
        self.Mobile_regexp = QtCore.QRegExp("[0-9]+")
        self.validator = QRegExpValidator(self.Mobile_regexp)
        self.Mobile_Number.setValidator(self.validator)

        self.Email_lable = QtWidgets.QLabel('Email ID')
        self.Email_lable.setMaximumWidth(80)
        self.Email = QtWidgets.QLineEdit("")
        self.Email.setMaximumWidth(150)
        self.Email.setPlaceholderText("Enter Valid Mail id")
        self.Email_regexp = QtCore.QRegExp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.validator = QRegExpValidator(self.Email_regexp)
        self.Email.setValidator(self.validator)

        self.lable_State = QtWidgets.QLabel("Select State")
        self.lable_State.setMaximumWidth(70)
        self.State_cmb = QtWidgets.QComboBox()
        #self.State_cmb.setMaximumWidth(200)
        self.lable_Dist = QtWidgets.QLabel("Select District")
        self.lable_Dist.setMaximumWidth(90)
        self.Dist_cmb = QtWidgets.QComboBox()
        #self.Dist_cmb.setMaximumWidth(200)

        self.submit_button = QtWidgets.QPushButton('Submit')
        self.submit_button.setMaximumWidth(100)
        self.submit_button.setMaximumHeight(30)
        self.close_button = QtWidgets.QPushButton('Close')
        self.close_button.setMaximumWidth(100)
        self.close_button.setMaximumHeight(30)
        self.clear_button = QtWidgets.QPushButton("Clear Form")
        self.clear_button.setMaximumWidth(100)
        self.clear_button.setMaximumHeight(30)


    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        #main_layout.setAlignment(QtCore.Qt.AlignTop)
        hbox_1 = QtWidgets.QHBoxLayout()
        hbox_1.addWidget(self.FirstName_lable)
        hbox_1.addWidget(self.first_name, alignment=QtCore.Qt.AlignLeft)
        hbox_1.addWidget(self.LastName_lable, alignment=QtCore.Qt.AlignRight)
        hbox_1.addWidget(self.last_name)
        main_layout.addLayout(hbox_1)

        hbox_2 = QtWidgets.QHBoxLayout()
        hbox_2.addWidget(self.Lable_Gender)
        hbox_2.addWidget(self.Male_Gender)
        hbox_2.addWidget(self.Female_Gender)
        main_layout.addLayout(hbox_2)

        #hbox_3 = QtWidgets.QHBoxLayout()
        #hbox_3.addWidget(self.DOB_Lable)
        #hbox_3.addWidget(self.DOB)
        #main_layout.addLayout(hbox_3)

        hbox_4 = QtWidgets.QHBoxLayout()
        hbox_4.addWidget(self.Mobile_lable)
        hbox_4.addWidget(self.Mobile_Number, alignment=QtCore.Qt.AlignLeft)
        main_layout.addLayout(hbox_4)

        hbox_5 = QtWidgets.QHBoxLayout()
        hbox_5.addWidget(self.Email_lable)
        hbox_5.addWidget(self.Email, alignment=QtCore.Qt.AlignLeft)
        main_layout.addLayout(hbox_5)

        hbox_6 = QtWidgets.QHBoxLayout()
        hbox_6.addWidget(self.lable_State)
        hbox_6.addWidget(self.State_cmb)
        hbox_6.addWidget(self.lable_Dist, alignment=QtCore.Qt.AlignRight)
        hbox_6.addWidget(self.Dist_cmb)
        main_layout.addLayout(hbox_6)

        hbox_7 = QtWidgets.QHBoxLayout()
        hbox_7.addWidget(self.submit_button, alignment=QtCore.Qt.AlignBottom)
        hbox_7.addWidget(self.clear_button, alignment=QtCore.Qt.AlignBottom)
        hbox_7.addWidget(self.close_button, alignment=QtCore.Qt.AlignBottom)
        main_layout.addLayout(hbox_7)


        # Connections
        self.submit_button.clicked.connect(self.Submit_fun)
        self.close_button.clicked.connect(self.Close_fun)
        #self.cancel_button.clicked.connect(lambda: self.close())
        self.clear_button.clicked.connect(self.Clear_fun)
        self.State_cmb.currentIndexChanged.connect(self.populate_dict)
        #self.Email.returnPressed.connect(self.onPressed)



    def populate_states(self):
        states = [x for x in data]
        self.State_cmb.addItems(states)


    def populate_dict(self):
        self.Dist_cmb.clear()
        for k,v in data.items():
            if k == self.State_cmb.currentText():
                self.Dist_cmb.addItems(v)


    def Submit_fun(self):
        self.sms_box = QtWidgets.QMessageBox()
        self.sms_box.setText("Hello, You have successfully submitted your information, Good Day !!!")
        self.sms_box.setIcon(self.sms_box.Information)
        self.sms_box.exec_()



    def Close_fun(self):
        self.sms_box = QtWidgets.QMessageBox()
        self.sms_box.setText("Do you really want to close this form?")
        self.sms_box.setInformativeText("Information will not be saved.")
        self.sms_box.setIcon(self.sms_box.Critical)
        self.sms_box.setStandardButtons(self.sms_box.Yes | self.sms_box.No)
        self.sms_box.setDefaultButton(self.sms_box.No)
        self.press = self.sms_box.exec_()
        if self.press == self.sms_box.Yes:
            self.close()
        else:
            self.sms_box.close()


    def Clear_fun(self):
        self.sms_box = QtWidgets.QMessageBox()
        self.sms_box.setText("Do you really want to clear this form?")
        self.sms_box.setInformativeText("All Information entered will be erased.")
        self.sms_box.setIcon(self.sms_box.Warning)
        self.sms_box.setStandardButtons(self.sms_box.Yes | self.sms_box.No)
        self.sms_box.setDefaultButton(self.sms_box.No)
        self.press = self.sms_box.exec_()
        if self.press == self.sms_box.Yes:
            "ComboBox clear"
            self.Dist_cmb.clear()
            self.populate_dict()
            self.State_cmb.clear()
            self.populate_states()

            "LineEdit clear"
            self.last_name.clear()
            self.first_name.clear()
            self.Mobile_Number.clear()
            self.Email.clear()

            "Gender clear"
            self.Male_Gender.setAutoExclusive(False)
            self.Male_Gender.setChecked(False)
            self.Male_Gender.setAutoExclusive(True)
            self.Female_Gender.setAutoExclusive(False)
            self.Female_Gender.setChecked(False)
            self.Female_Gender.setAutoExclusive(True)
        else:
            self.sms_box.close()


    def onPressed(self):
        print("helloooooooooo")
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.showMessage('Please enter valid Email')

        #if event.type() == QtCore.QEvent.MouseButtonPress:
            #if event.button() == Qt.LeftButton:

            #else:pass
                #self.error_dialog.close()

app = QtWidgets.QApplication(sys.argv)
dialog = My_Main_Dialog('DATTA')
dialog.show()
sys.exit(app.exec_())