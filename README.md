# clase_customic
## selector de tema para aplicaciones con librerias qdarkstyle y qt-material

modo de uso:
importar la libreria:

from Funciones_Customic import clase_customic

tu app deberia llamarse qApp por ejemplo...

if __name__ == '__main__':
    qApp = QtWidgets.QApplication([])

y con algún menú o boton llamar a la ventana de customización:

def customize_window(self, checked):
   enigmaUI.centroenigmaUI = self.ui.geometry().center()
   self.w = clase_customic(self.ui)
   self.w.show()


  thanks to https://github.com/ColinDuquesnoy/QDarkStyleSheet
for install qdarkstyle libraries:
pip install qdarkstyle
pip install .
python setup.py install

  thanks to https://qt-material.readthedocs.io/en/latest/index.html
for install qt-material libraries:
pip install qt-material
