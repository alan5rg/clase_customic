#alan.rg.10.05.2022.v.1.2
'''
thanks to https://github.com/ColinDuquesnoy/QDarkStyleSheet
for install qdarkstyle libraries:
pip install qdarkstyle
pip install .
python setup.py install
'''
#alan.rg.13.02.2023.v.1.3.1
'''
add qt_material stylesheet as RickyStyles and RickyThemes :)
QtCore.QSettings('Enigma','theme')
14.02.2023.se soluciona el aplicar tema guardado al salir
16.02.2023.se agregan claves a extructura extra

thanks to https://qt-material.readthedocs.io/en/latest/index.html
for install qt-material libraries:
pip install qt-material
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor, QWindow
import qdarkstyle  # noqa: E402
from qdarkstyle.dark.palette import DarkPalette  # noqa: E402
from qdarkstyle.light.palette import LightPalette  # noqa: E402

import os, sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, center, Qt, QThread
from PyQt5 import QtCore, QtGui, QtWidgets

from qt_material import apply_stylesheet

class clase_customic(QWidget):
        #clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        def __init__(self, parent=None):
                super().__init__(parent)
                self.parent=parent
              
                self.setWindowTitle("CHWCT (Change Window Colours Theme) v.1.3.1")
                
                # this will hide the title bar
                #self.setWindowFlag(Qt.FramelessWindowHint)
                #self.setWindowFlags(Qt.WindowCloseButtonHint)
                self.setWindowFlags(Qt.WindowMaximizeButtonHint| Qt.Window)
                #self.setWindowFlags(Qt.WindowMinimizeButtonHint)
                self.setFixedSize(540, 480)
                self.left = 0
                self.top = 0
                self.move(self.left,self.top)
                
                self.get_theme_settings()
                self.set_theme_settings()
                #botones
                self.botonDark = QPushButton('Q&Dark Stile', self)
                self.botonDark.setFixedSize(150,70)
                self.botonDark.setCursor(Qt.PointingHandCursor)
                self.botonDark.clicked.connect(self.QDarkStile)
                self.botonLight = QPushButton('Q&Light Stile', self)
                self.botonLight.setFixedSize(150,70)
                self.botonLight.setCursor(Qt.PointingHandCursor)
                self.botonLight.clicked.connect(self.QLightStile)
                self.botonOriginal = QPushButton('&Original Stile', self)
                self.botonOriginal.setFixedSize(150,70)
                self.botonOriginal.setCursor(Qt.PointingHandCursor)
                self.botonOriginal.clicked.connect(self.OriginalStile)
                self.botonGuardar = QPushButton('&Guardar Colores', self)
                self.botonGuardar.setFixedSize(160,40)
                self.botonGuardar.setCursor(Qt.PointingHandCursor)
                self.botonGuardar.clicked.connect(self.guardar)
                self.botonAcerca = QPushButton('&Acerca de...', self)
                self.botonAcerca.setFixedSize(150,30)
                self.botonAcerca.setCursor(Qt.PointingHandCursor)
                self.botonAcerca.clicked.connect(self.acercade)
                self.botonDonar = QPushButton('Donar', self)
                self.botonDonar.setFixedSize(150,30)
                self.botonDonar.setCursor(Qt.PointingHandCursor)
                self.botonDonar.clicked.connect(self.donar)
                self.botonSalir = QPushButton('&Salir', self)
                self.botonSalir.setFixedSize(150,30)
                self.botonSalir.setCursor(Qt.PointingHandCursor)
                self.botonSalir.clicked.connect(self.Salir)
                #combobox de estilos
                self.cbStyles = QComboBox()
                self.cbStyles.addItems(['',
                'dark_amber.xml',
                'dark_blue.xml',
                'dark_cyan.xml',
                'dark_lightgreen.xml',
                'dark_matrixgreen.xml',
                'dark_pink.xml',
                'dark_purple.xml',
                'dark_red.xml',
                'dark_teal.xml',
                'dark_yellow.xml',
                'light_amber.xml',
                'light_blue.xml',
                'light_cyan.xml',
                'light_cyan_500.xml',
                'light_lightgreen.xml',
                'light_pink.xml',
                'light_purple.xml',
                'light_red.xml',
                'light_teal.xml',
                'light_yellow.xml'])
                self.cbStyles.setFixedWidth(200)
                self.cbStyles.setFixedHeight(30)
                self.cbStyles.setCursor(Qt.PointingHandCursor)
                self.cbStyles.currentIndexChanged.connect(self.selectionchange)
                #grupos
                GroupSelcor = QGroupBox('Selección de Esquema de Colores (Theme)')
                GroupSelcor.setFixedHeight (130)
                GroupSelcor.setStyleSheet('QGroupBox:title {'
                 'subcontrol-origin: margin;'
                 'subcontrol-position: top center;'
                 'padding-left: 10px;'
                 'padding-right: 10px; }')
                GroupRickyStyle = QGroupBox('Selección de Estilos RickyStyles')
                GroupRickyStyle.setFixedHeight (100)
                GroupRickyStyle.setStyleSheet('QGroupBox:title {'
                 'subcontrol-origin: margin;'
                 'subcontrol-position: top center;'
                 'padding-left: 10px;'
                 'padding-right: 10px; }')
                GroupGuardar = QGroupBox('Guardar')
                GroupGuardar.setFixedHeight (100)
                GroupGuardar.setStyleSheet('QGroupBox:title {'
                 'subcontrol-origin: margin;'
                 'subcontrol-position: top center;'
                 'padding-left: 10px;'
                 'padding-right: 10px; }')
                GroupInfo = QGroupBox('Info y Otros')                
                GroupInfo.setFixedHeight (100)
                GroupInfo.setStyleSheet('QGroupBox:title {'
                 'subcontrol-origin: margin;'
                 'subcontrol-position: top center;'
                 'padding-left: 10px;'
                 'padding-right: 10px; }')
                # Layout de los botones y combobox
                layThemes = QHBoxLayout(self)
                layThemes.addWidget(self.botonDark,alignment=Qt.AlignLeft)
                layThemes.addWidget(self.botonLight,alignment=Qt.AlignCenter)
                layThemes.addWidget(self.botonOriginal,alignment=Qt.AlignRight)
                GroupSelcor.setLayout(layThemes)
                layStyles = QHBoxLayout(self)
                layStyles.addWidget(self.cbStyles, alignment=Qt.AlignCenter)
                GroupRickyStyle.setLayout(layStyles)
                layGuardar = QVBoxLayout(self)
                layGuardar.addWidget(self.botonGuardar, alignment=Qt.AlignCenter)
                GroupGuardar.setLayout(layGuardar)
                layOtros = QHBoxLayout(self)
                layOtros.addWidget(self.botonAcerca, alignment=Qt.AlignLeft)
                layOtros.addWidget(self.botonDonar, alignment=Qt.AlignCenter)
                layOtros.addWidget(self.botonSalir, alignment=Qt.AlignRight)
                GroupInfo.setLayout(layOtros)
                # Layout de grupos
                mainLay = QVBoxLayout(self)
                mainLay.addWidget(GroupSelcor)
                mainLay.addSpacing(5)
                mainLay.addWidget(GroupRickyStyle)
                mainLay.addSpacing(5)
                mainLay.addWidget(GroupGuardar)
                mainLay.addSpacing(5)
                mainLay.addWidget(GroupInfo)

                self.show()

        def QDarkStile(self):
                style = qdarkstyle.load_stylesheet(palette=DarkPalette)
                qApp.setStyleSheet(style)
                clase_customic.qdarkmode = True
                clase_customic.originalmode = False
                clase_customic.rickystyle = False
                print('Current Select "Qdark" theme: darkmode:', clase_customic.qdarkmode, ', originalmode:', clase_customic.originalmode, ', rickystyle:', clase_customic.rickystyle, 'rickytheme:', clase_customic.rickytheme)

        def QLightStile(self):
                style = qdarkstyle.load_stylesheet(palette=LightPalette)
                qApp.setStyleSheet(style)
                clase_customic.originalmode = False
                clase_customic.qdarkmode = False
                clase_customic.rickystyle = False
                print('Current Select "Qlight" theme: darkmode:', clase_customic.qdarkmode, ', originalmode:', clase_customic.originalmode, ', rickystyle:', clase_customic.rickystyle, 'rickytheme:', clase_customic.rickytheme)
        
        def OriginalStile(self):
                qApp.setStyleSheet("")
                qApp.setStyle('Fusion')
                clase_customic.originalmode = True
                clase_customic.qdarkmode = False
                clase_customic.rickystyle = False
                print('Current Select "Original" theme: darkmode:', clase_customic.qdarkmode, ', originalmode:', clase_customic.originalmode, ', rickystyle:', clase_customic.rickystyle, 'rickytheme:', clase_customic.rickytheme)

        def selectionchange(self,i):
                clase_customic.originalmode = False
                clase_customic.qdarkmode = False                
                clase_customic.rickystyle = True
                clase_customic.rickytheme = self.cbStyles.currentText()
                '''
                #for debug only
                print ("Items in the list are :")

                for count in range(self.cbStyles.count()):
                        print (count, ": ",self.cbStyles.itemText(count))
                '''
                print ("Current index",i,"selection changed ",self.cbStyles.currentText())
                print('Current Select "RyckyStyle" theme: darkmode:', clase_customic.qdarkmode, ', originalmode:', clase_customic.originalmode, ', rickystyle:', clase_customic.rickystyle, 'rickytheme:', clase_customic.rickytheme)

                extra = {
                # Button colors
                #'danger': '#dc3545',
                #'warning': '#ffc107',
                #'success': '#17a2b8',
                
                # Font
                'density_scale': '-5',
                'font_family': 'roboto',
                'font_size': '12px',
                'line_height': '12px',
                'font_style': 'bold',
                'text-transform':'None',

                # environ
                'pyside6': False,
                'linux': True,
                }

                #apply_stylesheet(qApp, self.cbStyles.currentText(), invert_secondary=False, extra=extra)
                #apply_stylesheet(qApp, self.cbStyles.currentText(), invert_secondary=False)
                apply_stylesheet(qApp, self.cbStyles.currentText(), invert_secondary=True, extra=extra)
                #apply_stylesheet(qApp, self.cbStyles.currentText(), invert_secondary=self.cbInvertSec.currentText())

        def acercade(self):
                QMessageBox.about(self, "Acerca de...", """CHWCT (Change Window Colours Theme) v.1.3.1 is a proyect by Alan R.G.Systemas for customing a Lucas and Lisandro DataBases from Meva
                                
                 Copyright 2021-2023 Alan R.G.Systemas
                 This software is released under a BSD style license.
                 This software comes with no warranties
                 expressed or implied.
                 """)

        def donar(self):
                QMessageBox.information(self, "Donar...", """                    Ayude al software libre!!!                          
                
                 Apoye a los programadores
                 enviando su donación al alias:
                 buzos.hay.domar.mp
                 """)

        def guardar(self):
                dialog = DialogGuard(self)
                dialog.show()
        
        def Salir(self):
                self.set_theme_settings()
                #self.close()
                self.hide()

        #data theme get and save 10.05.2022 Alan.rg.
        def get_theme_settings(self):
                self.settings_theme = QtCore.QSettings('Enigma','theme')
                self.temp = self.settings_theme.value('esquema')
                print("get_theme_settings read:", self.temp) 

                try:
                        clase_customic.qdarkmode = bool(self.temp['confqdarkmode'] )
                        clase_customic.originalmode = bool(self.temp['conforiginalmode'] )
                        clase_customic.rickystyle = bool(self.temp['confrickystyle'] )#add for rickystyles
                        clase_customic.rickytheme = str(self.temp['confrickytheme'] )#add for rickystyles

                except:
                        self.connector = {}
                        self.connector['confqdarkmode'] = False
                        self.connector['conforiginalmode'] = True
                        self.connector['confrickystyle'] = False  #add for rickystyles
                        self.connector['confrickytheme'] = '' #add for rickystyles
                        clase_customic.qdarkmode=bool(self.connector['confqdarkmode'] )
                        clase_customic.originalmode=bool(self.connector['conforiginalmode'] )
                        clase_customic.rickystyle=bool(self.connector['confrickystyle'] ) #add for rickystyles
                        clase_customic.rickytheme=str(self.connector['confrickytheme'] ) #add for rickystyles

                else:
                        self.connector = self.temp

                self.settings_theme.setValue('esquema', self.connector)
                print("get_theme_settings saved:", self.connector)

        def save_theme_settings(self):
                self.settings_theme = QtCore.QSettings('Enigma','theme')
                self.aux = self.settings_theme.value('esquema') 
                self.connector = self.aux
                self.connector['confqdarkmode'] = clase_customic.qdarkmode
                self.connector['conforiginalmode'] = clase_customic.originalmode
                self.connector['confrickystyle'] = clase_customic.rickystyle  #add for rickystyles
                self.connector['confrickytheme'] = clase_customic.rickytheme #add for rickystyles
                self.settings_theme.setValue('esquema', self.connector)
                print("save_theme_settings saved:", self.connector)
        
        #alan.rg.add 10.02.2023 for set the read theme saved in reg
        def set_theme_settings(self):
                settings_theme = QtCore.QSettings('Enigma','theme')
                readDict_theme = settings_theme.value('esquema') 
    
                try:
                    qdarkmode = bool(readDict_theme['confqdarkmode'] )
                    originalmode = bool(readDict_theme['conforiginalmode'] )
                    rickystyle = bool(readDict_theme['confrickystyle'] )
                    rickytheme = str(readDict_theme['confrickytheme'] )
                    print('Found Main personal setting theme: darkmode:', qdarkmode, ', originalmode:', originalmode, ', rickystyle:', rickystyle, 'rickytheme:', rickytheme)
 
                except:
                        qApp.setStyle('Fusion')
                        dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
                        print('Main current setting theme: "Original" , dont read personal setting')

                else:
                        if rickystyle :
                                extra = {
                                # Button colors
                                #'danger': '#dc3545',
                                #'warning': '#ffc107',
                                #'success': '#17a2b8',
                                # Font
                                'density_scale': '-5',
                                'font_family': 'roboto',
                                'font_size': '12px',
                                'line_height': '12px',
                                'font_style': 'bold',
                                'text-transform':'None',

                                # environ
                                'pyside6': False,
                                'linux': True,
                                }
                                apply_stylesheet(qApp, rickytheme, invert_secondary=True, extra=extra)
                                print('Set Main current personal setting "RickyStyle" theme: darkmode:', qdarkmode, ', originalmode:', originalmode, ', rickystyle:', rickystyle, 'rickytheme:', rickytheme)

                        elif originalmode :
                                qApp.setStyle('Fusion')
                                dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
                                print('Set Main current personal setting "Original" theme: darkmode:', qdarkmode, ', originalmode:', originalmode, ', rickystyle:', rickystyle, 'rickytheme:', rickytheme)
                
                        elif qdarkmode :
                                style = qdarkstyle.load_stylesheet(palette=DarkPalette)
                                qApp.setStyleSheet(style)
                                print('Set Main current setting "QDark" theme: darkmode:', qdarkmode, ', originalmode:', originalmode, ', rickystyle:', rickystyle, 'rickytheme:', rickytheme)
                
                        elif ~qdarkmode:
                                style = qdarkstyle.load_stylesheet(palette=LightPalette)
                                qApp.setStyleSheet(style)
                                print('Set Main current setting "QLight" theme: darkmode:', qdarkmode, ', originalmode:', originalmode, ', rickystyle:', rickystyle, 'rickytheme:', rickytheme)
                
                        else:
                                qApp.setStyle('Fusion')
                                dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
                                print('Anywere Set Main current setting "Original" theme: darkmode:', qdarkmode, ', originalmode:', originalmode, ', rickystyle:', rickystyle, 'rickytheme:', rickytheme)
        #alan.rg.add 10.02.2023 for set the read theme saved in reg

class DialogGuard(QDialog):
        def __init__(self, *args, **kwargs):
                super(DialogGuard, self).__init__(*args, **kwargs)
                self.setWindowTitle("Guardar Colores?")
                self.setFixedSize(250, 70)                
                self.botonSi = QPushButton('&Si', self)
                self.botonSi.setFixedSize(90,30)
                self.botonSi.clicked.connect(self.clickeoSi)
                self.botonNo = QPushButton('&No', self)
                self.botonNo.setFixedSize(90,30)
                self.botonNo.clicked.connect(self.clickeoNo)
                lay = QHBoxLayout(self)
                lay.addWidget(self.botonSi)
                lay.addWidget(self.botonNo)

        def clickeoSi(self):
                # Antes de Guardar variables darkmode y originalmode en el entorno del usuario confirmar si el usuario esta seguro
                dialog = DialogSeguro(self)
                dialog.show()
                self.hide()
                #self.close()
                
        def clickeoNo(self):
                self.hide()
                #self.close()

class DialogSeguro(QDialog):
        def __init__(self, *args, **kwargs):
                super(DialogSeguro, self).__init__(*args, **kwargs)
                self.setWindowTitle("Seguro que está seguro?")
                self.setFixedSize(250, 70)
                self.botonSeguroSi = QPushButton('&Si', self)
                self.botonSeguroSi.setFixedSize(90,30)
                self.botonSeguroSi.clicked.connect(self.clickeoSeguroQueSi)
                self.botonSeguroNo = QPushButton('&No', self)
                self.botonSeguroNo.setFixedSize(90,30)
                self.botonSeguroNo.clicked.connect(self.clickeoSeguroNoEstoy)
                lay = QHBoxLayout(self)
                lay.addWidget(self.botonSeguroSi)
                lay.addWidget(self.botonSeguroNo)      

        def clickeoSeguroQueSi(self):
                # Guardar variables darkmode y originalmode en el entorno del usuario
                print('Current Saved theme: darkmode:', clase_customic.qdarkmode, ', originalmode:', clase_customic.originalmode)                
                clase_customic.save_theme_settings(self)
                self.guardadohastalasbolas()
                self.hide()
                #self.close()
                
        def clickeoSeguroNoEstoy(self):
                self.hide()
                #self.close()

        def guardadohastalasbolas(self):
                QMessageBox.warning(self, "Importante", """
                 Usted acaba de guardar  
                 la configuracion vigente  
                 de forma exitosa!
                                         """)


if __name__ == '__main__':
        import sys
        qApp = QtWidgets.QApplication([])
        #app.setStyle('Fusion')    # <-----
        #dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        
        #w = clase_customic()
        #w.show()
        ex = clase_customic()
        sys.exit(qApp.exec_())
