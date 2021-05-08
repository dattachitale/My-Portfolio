import sys
import re
import subprocess
from subprocess import *
import os
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
from PySide2.QtGui import *

class My_Main_Dialog(QtWidgets.QWidget):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)
        #self.setMinimumHeight(300)
        #self.setMinimumWidth(400)
        self.setFixedSize(400,330)
        self.setWindowIcon(QIcon("Main_Logo.ico"))
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.Main_Menu = QtWidgets.QMenuBar()
        self.File_Menu = self.Main_Menu.addMenu('&File')
        self.View_Menu = self.Main_Menu.addMenu('&View')
        self.Console_Menu = self.Main_Menu.addMenu('&Console')
        self.Tool_Menu = self.Main_Menu.addMenu('&Tool')
        self.Help_Menu = self.Main_Menu.addMenu('&Help')
                            # File_Menu
        self.Set_name = self.File_Menu.addAction('Set your console &name')
        self.File_Menu.addSeparator()
        # self.Exit_app.setIcon(QIcon("exit.png"))
        self.Set_name.triggered.connect(self.set_name)
        self.Swich_app = self.File_Menu.addAction('&Switch to Home Menu')
        self.File_Menu.addSeparator()
        #self.Exit_app.setIcon(QIcon("exit.png"))
        self.Swich_app.triggered.connect(self.swich_app)
        self.Exit_app = self.File_Menu.addAction('&Exit')
        self.Exit_app.setIcon(QIcon("exit.png"))
        self.Exit_app.triggered.connect(self.exit_app)
                            #View_Menu
        self.Firmware = self.View_Menu.addAction("&Console Firmware Version")
        self.View_Menu.addSeparator()
        self.Firmware.triggered.connect(self.firmware_info)
        self.App_List = self.View_Menu.addAction("&Installed App List")
        self.View_Menu.addSeparator()
        self.App_List.triggered.connect(self.application_list)
        self.Console_List = self.View_Menu.addAction('&Registered Target List')
        self.View_Menu.addSeparator()
        self.Console_List.triggered.connect(self.console_list)
                            #Console_Menu
        self.Connect_Console = self.Console_Menu.addAction('&Connect')
        self.Connect_Console.setIcon(QIcon("connect.png"))
        self.Console_Menu.addSeparator()
        self.Connect_Console.triggered.connect(self.connect_console)
        self.Disconnect_Console = self.Console_Menu.addAction('&Disconnect')
        self.Disconnect_Console.setIcon(QIcon("disconnect.png"))
        self.Console_Menu.addSeparator()
        self.Disconnect_Console.triggered.connect(self.disconnect_console)
        self.Power_Off = self.Console_Menu.addAction('&Power off')
        self.Power_Off.setIcon(QIcon("stand-by.png"))
        self.Console_Menu.addSeparator()
        self.Power_Off.triggered.connect(self.power_off)
        self.Reboot = self.Console_Menu.addAction('&Reboot')
        self.Reboot.setIcon(QIcon("reboot.png"))
        self.Console_Menu.addSeparator()
        self.Reboot.triggered.connect(self.reboot)
                            #Help_Menu
        self.About = self.Help_Menu.addAction('&About')
        self.About.setIcon(QIcon("about.png"))
        self.Help_Menu.addSeparator()
        self.About.triggered.connect(self.about)
        self.Link_menu = self.Help_Menu.addMenu("&Links")
        self.Link_menu.setIcon(QIcon("link.png"))
        self.Home = QtWidgets.QAction("&Switch Home")
        self.Home.setIcon(QIcon("home.png"))
        self.Train_Doc = QtWidgets.QAction("&Training Documents")
        self.Train_Doc.setIcon(QIcon("Train_document.png"))
        self.NDI_Doc = QtWidgets.QAction("&NDI Documents")
        self.NDI_Doc.setIcon(QIcon("ndi_document.png"))
        self.Link_menu.addAction(self.Home)
        self.Link_menu.addSeparator()
        self.Document = self.Link_menu.addMenu("&Documents")
        self.Document.setIcon(QIcon("documents.png"))
        self.Home.triggered.connect(self.home_url)
        self.Document.addAction(self.Train_Doc)
        self.Document.addSeparator()
        self.Train_Doc.triggered.connect(self.training_doc_explorer)
        self.Document.addAction(self.NDI_Doc)
        self.NDI_Doc.triggered.connect(self.ndi_doc)


    def create_layout(self):
        self.Main_layout = QtWidgets.QVBoxLayout()
        self.Tab_Widget = QtWidgets.QTabWidget()
        self.Tab_Widget.addTab(Tab_Media(), "Media and Attachments")
        self.Tab_Widget.addTab(Tab_Applications(), "Manage Applications")
        self.Main_layout.addWidget(self.Tab_Widget)
        self.setLayout(self.Main_layout)
        self.Main_layout.setMenuBar(self.Main_Menu)


    '''***************** File Menu Functions' Declaration *****************'''
    '''Set name to console'''
    def set_name(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            self.Set_name_input = QtWidgets.QInputDialog()
            text, ok = self.Set_name_input.getText(self, 'Console Name', 'Make sure console is connected first. \n\nEnter name for your console:')
            self.Set_name_input.setOkButtonText("datta")
            if ok and text:
                comm = r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe set-name ' + text
                subprocess.Popen(comm)
                New_name = "<b>" + text + "</b>"
                sms_box = QtWidgets.QMessageBox()
                sms_box.setWindowTitle("Name set Information                                                                                                  ")
                sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
                sms_box.setText("Console Name has been set to: " +New_name)
                sms_box.setInformativeText("Please check <b>Target Name</b> column of Target Manager to reflect changes.")
                sms_box.setIcon(sms_box.Information)
                sms_box.exec_()


    '''Switch boot menu to Home'''
    def swich_app(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            self.sms_box = QtWidgets.QMessageBox()
            self.sms_box.setWindowTitle("Switch to Home Menu: ")
            self.sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            self.sms_box.setText('''Are you sure you want to use this option? If you click Yes, console will restart.''')
            self.sms_box.setInformativeText('''Please use this option only once (after you initialize console) to set console's Initial Boot Menu to Home Menu.''')
            self.sms_box.setDetailedText('''This option is used when you want to set console's Initial Boot Menu as "HOME MENU" (Usally after initialization)''')
            self.sms_box.setStandardButtons(self.sms_box.Yes | self.sms_box.No)
            self.sms_box.setDefaultButton(self.sms_box.No)
            self.sms_box.setIcon(self.sms_box.Warning)
            self.press = self.sms_box.exec_()

            if self.press == self.sms_box.Yes:
                subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\TargetShell.exe switch-menu --menu=homemenu --reset')
            else:
                self.sms_box.close()

    '''Exit the application'''
    def exit_app(self):
        self.close()


    '''***************** View Menu Functions' Declaration *****************'''
    '''Firmware Information'''
    def firmware_info(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            self.Console_Firmware = subprocess.check_output(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe firmware-version')
            self.Firm_Result = self.Console_Firmware.decode("latin1", 'ignore').split('\n')
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Firmware ")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText(self.Firm_Result[0])
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()

    '''get application list'''
    def application_list(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText(
                "Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            self.Aplications = subprocess.check_output(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe list-application')
            self.App_Result = self.Aplications.decode("latin1", 'ignore').split('\n')
            result = ""
            for i in range(2, len(self.App_Result) - 3):
                result = result + self.App_Result[i]
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Applications                                                                                         ")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>Installed applications are:</b>")
            sms_box.setInformativeText(result)
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()

    '''Get Console list'''
    def console_list(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText(
                "Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            self.Consoles = subprocess.check_output(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe list-target')
            self.Console_Result = self.Consoles.decode("latin1", 'ignore').split('\t')
            result = ""
            for i in range(0, len(self.Console_Result) - 1):
                result = result + self.Console_Result[i]
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Consoles ")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>Registered Consoles:</b> ")
            sms_box.setInformativeText(result)
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()


    '''***************** Console Menu Functions' Declaration *****************'''
    '''Connect console'''
    def connect_console(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("Switch console has been connected to Nintendo Target Manager")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
            #self.Connect_Console.setEnabled(False)
            #self.Disconnect_Console.setEnabled(True)

    '''Disconnect console'''
    def disconnect_console(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to disconnect</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe disconnect')
            sms_box = QtWidgets.QMessageBox()
            #self.sms_box.setParent(self)
            sms_box.setWindowTitle("Disconnection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("Switch kit has been disconnected from Nintendo Target Manager")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
            #self.Disconnect_Console.setEnabled(False)
            #self.Connect_Console.setEnabled(True)

    '''Turn off console'''
    def power_off(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to Power Off</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe power-off')
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Power Off Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("Powering Off console... Please sit tight.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()


    '''Restart console'''
    def reboot(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to Reboot</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe reset')
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Reboot Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("Rebooting console... Please sit tight.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()

    '''***************** Help Menu Functions' Declaration *****************'''
    '''Developed by'''
    def about(self):
        self.sms_box = QtWidgets.QMessageBox()
        pixmap = QPixmap(r'C:\Users\dchitale\Desktop\download.png')
        self.sms_box.setWindowTitle("About Information ")
        self.sms_box.isSizeGripEnabled()
        self.sms_box.setText("This app is developed by Datta")
        self.sms_box.setInformativeText("Switch Interface v1.0 <br> All rights reserved © 2021")
        self.sms_box.setIcon(self.sms_box.Information)
        self.sms_box.exec_()

    def home_url(self):
        QDesktopServices.openUrl(QtCore.QUrl('https://world.ubisoft.org/job/quality_control/nzone/nzone.html'))

    def training_doc_explorer(self):
        os.startfile(r'\\ubisoft.org\punstudio\QC\Public\Platform New\Console Docs\NINTENDO NX\Switch_Training')

    def ndi_doc(self):
        QDesktopServices.openUrl(QtCore.QUrl('file:///D:/NintendoSDK/NintendoSDK_10_4_0/NintendoSDK/Documents/Package/contents/title.html'))


    '''***************** First tab "Media and attachment" class *****************'''
class Tab_Media(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
                            #Create Screenshot groupbox
        self.Media_screenshot_grp_box = QtWidgets.QGroupBox("Screenshot Section")
        self.Media_screenshot_grp_box.setMaximumHeight(70)
                            #Create Copy groupbox
        self.Media_copy_grp_box = QtWidgets.QGroupBox("Copy Album Section")
        self.Media_copy_grp_box.setMaximumHeight(70)
                            #Create Delete groupbox
        self.Media_delete_grp_box = QtWidgets.QGroupBox("Delete Album Section")
        self.Media_delete_grp_box.setMaximumHeight(70)

        '''*********************** create widgets for all three groupboxes ***********************'''
                    #create and add widgets for Screenshot groupbox
        self.Screenshot_lable = QtWidgets.QLabel("Take a screenshot directly")
        self.Screenshot_button = QtWidgets.QPushButton(" Screenshot")
        self.Screenshot_button.setStyleSheet('font:bold')
        self.Screenshot_button.setIcon(QIcon("screenshot.png"))
        self.Screenshot_button.setMaximumWidth(100)
                    # add above widgets to screenshot_grp_box
        self.V_screenshot_grp_box = QtWidgets.QHBoxLayout()
        #self.V_screenshot_grp_box.setAlignment(QtCore.Qt.AlignCenter)
        self.V_screenshot_grp_box.addWidget(self.Screenshot_lable)
        self.V_screenshot_grp_box.addWidget(self.Screenshot_button)
                    # set screenshot_grp_box's layout
        self.Media_screenshot_grp_box.setLayout(self.V_screenshot_grp_box)

                    #create and add widgets for Copy groupbox
        self.Copy_lable = QtWidgets.QLabel("Copy all attachments from console to PC")
        self.Copy_button = QtWidgets.QPushButton(" Copy Album")
        self.Copy_button.setStyleSheet('font:bold')
        self.Copy_button.setIcon(QIcon("copy.png"))
        self.Copy_button.setMaximumWidth(100)
                    # add above widgets to screenshot_grp_box
        self.V_copy_grp_box = QtWidgets.QHBoxLayout()
        self.V_copy_grp_box.addWidget(self.Copy_lable)
        self.V_copy_grp_box.addWidget(self.Copy_button)
                    # set Copy_grp_box's layout
        self.Media_copy_grp_box.setLayout(self.V_copy_grp_box)

                    # create and add widgets for Delete groupbox
        self.Delete_lable = QtWidgets.QLabel("Delete all attachments from console album")
        self.Delete_button = QtWidgets.QPushButton("Delete Album")
        self.Delete_button.setStyleSheet('font:bold')
        self.Delete_button.setIcon(QIcon("trash.png"))
        self.Delete_button.setMaximumWidth(100)
                    # add above widgets to screenshot_grp_box
        self.V_delete_grp_box = QtWidgets.QHBoxLayout()
        self.V_delete_grp_box.addWidget(self.Delete_lable)
        self.V_delete_grp_box.addWidget(self.Delete_button)
                    # set Copy_grp_box's layout
        self.Media_delete_grp_box.setLayout(self.V_delete_grp_box)
        '''*********************** creating done here ***********************'''

        '''*********************** add all above to main layout ***********************'''
        self.Main_layout = QtWidgets.QVBoxLayout()
        #self.Main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.Main_layout.addWidget(self.Media_screenshot_grp_box)
        self.Main_layout.addWidget(self.Media_copy_grp_box)
        self.Main_layout.addWidget(self.Media_delete_grp_box)
        self.setLayout(self.Main_layout)


                            #Connections
        self.Screenshot_button.clicked.connect(self.take_screenshot)
        self.Delete_button.clicked.connect(self.delete_all_attachments)
        self.Copy_button.clicked.connect(self.copy_all_attachments)

    '''***************** Button Connections' Functions Declaration *****************'''
    def take_screenshot(self):
        if not os.path.exists(r'D:\Album'):
            os.makedirs(r'D:\Album')
        subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe take-screenshot --directory="D:\Album"')
        os.startfile(r'D:\Album')

    def delete_all_attachments(self):
        self.sms_box = QtWidgets.QMessageBox()
        self.sms_box.setWindowTitle("Confirmation ")
        self.sms_box.setText("Are you sure you want to delete all attachments from console?")
        self.sms_box.setStandardButtons(self.sms_box.Yes | self.sms_box.No)
        self.sms_box.setIcon(self.sms_box.Warning)
        self.press = self.sms_box.exec_()
        if self.press == self.sms_box.Yes:
            subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\RunOnTarget.exe --suppress-auto-kill D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\TargetTools\NX-NXFP2-a64\DevMenuCommand\Release\DevMenuCommand.nsp -- album clean --storage builtin')
            self.sms_box = QtWidgets.QMessageBox()
            self.sms_box.setWindowTitle("Delete information")
            self.sms_box.setText("All the attachments have been deleted")
            self.sms_box.setIcon(self.sms_box.Information)
            self.sms_box.exec_()
        else:
            self.sms_box.close()

    def copy_all_attachments(self):
        subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\RunOnTarget.exe --suppress-auto-kill D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\TargetTools\NX-NXFP2-a64\DevMenuCommand\Release\DevMenuCommand.nsp -- album download --storage builtin --directory D:\Album')
        self.sms_box = QtWidgets.QMessageBox()
        self.sms_box.setWindowTitle("Download information")
        self.sms_box.setText("Downloading Album completed.")
        self.sms_box.setIcon(self.sms_box.Information)
        self.sms_box.setStandardButtons(self.sms_box.Open)
        self.sms_box.exec_()
        os.startfile(r'D:\Album')



'''***************** Second tab "Manage Applications" class *****************'''
class Tab_Applications(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
                            #Create App's first groupbox
        self.App_first_grp_box = QtWidgets.QGroupBox("Application Launcher")
        self.App_first_grp_box.setMaximumHeight(70)
                            #Create App's second groupbox
        self.App_second_grp_box = QtWidgets.QGroupBox("Application Terminator")
        self.App_second_grp_box.setMaximumHeight(70)
                            #Create App's third groupbox
        self.App_third_grp_box = QtWidgets.QGroupBox("Application Uninstaller")
        self.App_third_grp_box.setMaximumHeight(70)
                            # Create App's 4th groupbox
        self.App_fourth_grp_box = QtWidgets.QGroupBox("Application Installer")
        self.App_fourth_grp_box.setMaximumHeight(70)


        '''*********************** create widgets for all three groupboxes ***********************'''
                    #create and add widgets for App's first groupbox
        self.Launch_lable = QtWidgets.QLabel("Launch an installed Application")
        self.Launch_button = QtWidgets.QPushButton("Launch")
        self.Launch_button.setIcon(QIcon("launch.png"))
        self.Launch_button.setStyleSheet('font:bold')
        #self.Screenshot_button.setIcon(QIcon("screenshot.png"))
        self.Launch_button.setMaximumWidth(83)
                    # add above widgets to App's first_grp_box
        self.V1_App_first_grp_box = QtWidgets.QHBoxLayout()
        self.V1_App_first_grp_box.addWidget(self.Launch_lable)
        self.V1_App_first_grp_box.addWidget(self.Launch_button)
                    # set App's first_grp_box's layout
        self.App_first_grp_box.setLayout(self.V1_App_first_grp_box)

                    #create and add widgets for App's second groupbox
        self.Terminate_lable = QtWidgets.QLabel("Terminate the running Application only")
        self.Terminate_button = QtWidgets.QPushButton("Terminate")
        self.Terminate_button.setIcon(QIcon("terminate.png"))
        self.Terminate_button.setStyleSheet('font:bold')
        #self.Terminate_button.setIcon(QIcon("copy.png"))
        self.Terminate_button.setMaximumWidth(83)
                    # add above widgets to App's second groupbox
        self.V_Terminate_grp_box = QtWidgets.QHBoxLayout()
        self.V_Terminate_grp_box.addWidget(self.Terminate_lable)
        self.V_Terminate_grp_box.addWidget(self.Terminate_button)
                    # set App's second groupbox's layout
        self.App_second_grp_box.setLayout(self.V_Terminate_grp_box)

                    # create and add widgets for App's third groupbox
        self.Uninstall_lable = QtWidgets.QLabel("Uninstall the selected Application")
        self.Uninstall_button = QtWidgets.QPushButton("Uninstall")
        self.Uninstall_button.setIcon(QIcon("uninstall.png"))
        self.Uninstall_button.setStyleSheet('font:bold')
        #self.Uninstall_button.setIcon(QIcon("trash.png"))
        self.Uninstall_button.setMaximumWidth(83)
                    # add above widgets to App's third groupbox
        self.V_uninstall_grp_box = QtWidgets.QHBoxLayout()
        self.V_uninstall_grp_box.addWidget(self.Uninstall_lable)
        self.V_uninstall_grp_box.addWidget(self.Uninstall_button)
                    # set App's third groupbox's layout
        self.App_third_grp_box.setLayout(self.V_uninstall_grp_box)


                    # create and add widgets for App's fourth groupbox
        self.Install_lable = QtWidgets.QLabel("Install the selected Application")
        self.Install_button = QtWidgets.QPushButton("Install")
        self.Install_button.setIcon(QIcon("uninstall.png"))
        self.Install_button.setStyleSheet('font:bold')
                    # self.Uninstall_button.setIcon(QIcon("trash.png"))
        self.Install_button.setMaximumWidth(83)
                 # add above widgets to App's third groupbox
        self.V_Install_grp_box = QtWidgets.QHBoxLayout()
        self.V_Install_grp_box.addWidget(self.Install_lable)
        self.V_Install_grp_box.addWidget(self.Install_button)
                # set App's third groupbox's layout
        self.App_fourth_grp_box.setLayout(self.V_Install_grp_box)

        '''*********************** creating done here ***********************'''

        '''*********************** add all above to main layout ***********************'''
        self.Main_layout = QtWidgets.QVBoxLayout()
        #self.Main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.Main_layout.addWidget(self.App_first_grp_box)
        self.Main_layout.addWidget(self.App_second_grp_box)
        self.Main_layout.addWidget(self.App_third_grp_box)
        self.Main_layout.addWidget(self.App_fourth_grp_box)
        self.setLayout(self.Main_layout)


                            #Connections
        self.Launch_button.clicked.connect(self.launch_app)
        self.Terminate_button.clicked.connect(self.terminate_app)
        self.Uninstall_button.clicked.connect(self.uninstall_app)
        self.Install_button.clicked.connect(self.install_app)

    def launch_app(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found and Failed to launch application</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()

        else:
            res = subprocess.check_output(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe list-application')
            cmd_result = res.decode("latin1", 'ignore').split('\n')
            result = []
            for i in range(2, len(cmd_result)-3):
                result.append(cmd_result[i])
# if no applications are installed - list is empty
            if len(result) == 0:
                self.sms_box = QtWidgets.QMessageBox()
                self.sms_box.setWindowTitle("App Information")
                self.sms_box.setText("There are no Games or Applications installed on the console!!!")
                self.sms_box.setInformativeText("Please install a Game/Application first in order to launch it.")
                self.sms_box.setIcon(self.sms_box.Information)
                self.sms_box.exec_()
#Else populate list to QinputDialog and launch selected applicaion
            else:
                self.input_dialogue = QtWidgets.QInputDialog()
                text, ok = self.input_dialogue.getItem(self, "Application selection","Select an application to launch:", result, 0, False)
                if ok:
                    comm = r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe launch-application '+text
                    subprocess.Popen(comm)
                else:
                    self.input_dialogue.close()

        #self.Launch_button.setEnabled(False)

    def terminate_app(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found and Failed to terminate application</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()

        else:
            subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe terminate')
            self.Launch_button.setEnabled(True)

    def uninstall_app(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found and Failed to uninstall application</b>")
            sms_box.setInformativeText("Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            res = subprocess.check_output(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe list-application')
            cmd_result = res.decode("latin1", 'ignore').split('\n')
            result = []
            for i in range(2, len(cmd_result) - 3):
                if cmd_result [i] == '0x0100000000002065            1.0.0  DevMenu Application  \r':
                    continue
                result.append(cmd_result[i])
        #print(result)
# if the applications are not installed (exclude DevMenu - risk to uninstall it)- list is empty
            if len(result) == 0:
                self.sms_box = QtWidgets.QMessageBox()
                self.sms_box.setWindowTitle("App Information")
                #self.sms_box.setStyleSheet('font:bold')
                self.sms_box.setText("No Games or Applications installed on the console!!!")
                self.sms_box.setInformativeText("Please install a Game/Application on console first.")
                self.sms_box.setIcon(self.sms_box.Information)
                self.sms_box.exec_()
#Else populate list to QinputDialog and launch selected applicaion
            else:
                self.input_dialogue = QtWidgets.QInputDialog()
                text, ok = self.input_dialogue.getItem(self, "Application selection", "Select an application to uninstall:",result, 0, False)
                if ok:
                    comm = r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe uninstall-application ' + text
                    subprocess.Popen(comm)
                else:
                    self.input_dialogue.close()

    def install_app(self):
        Alive_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe check-alive --any')
        Connection_out = subprocess.Popen(r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe connect')
        if Alive_out.wait() != 0 or Connection_out.wait() != 0:
            sms_box = QtWidgets.QMessageBox()
            sms_box.setWindowTitle("Connection Information")
            sms_box.setWindowIcon(QIcon("Main_Logo.ico"))
            sms_box.setText("<b>No Target found or Failed to connect</b>")
            sms_box.setInformativeText(
                "Please connect/reconnect console to PC using Type C cable or wake it up from sleep mode.")
            sms_box.setIcon(sms_box.Information)
            sms_box.exec_()
        else:
            File_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open nsp build file', r"C:\\", 'Nsp file(*.nsp)')

            #Exit = None
            comm = r'D:\NintendoSDK\NintendoSDK_10_4_0\NintendoSDK\Tools\CommandLineTools\ControlTarget.exe install-application ' + File_name[0]
            Installation_progress = subprocess.Popen(comm, stdout=subprocess.PIPE, universal_newlines=True)

            print("Datta")
            while Installation_progress.poll() is None:
                print("datta")
                #line = Installation_progress.stdout.readline()
                #print(line.strip())
                #if "Exit" in line:
                    #Exit = True
            #till Installation_result.wait() ! = 0
            '''---------------- progress bar'''








app = QtWidgets.QApplication(sys.argv)
dialog = My_Main_Dialog('Switch Interface')
dialog.show()
sys.exit(app.exec_())

