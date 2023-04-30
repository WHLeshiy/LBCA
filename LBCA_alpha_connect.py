from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from shifrovanie import rasshifr, shifr

Form, Window = uic.loadUiType("LBCA_alpha.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()



def connecntion_slider_spinbox():
    form.horizontalSlider.valueChanged.connect(form.spinBox.setValue)
    form.spinBox.valueChanged.connect(form.horizontalSlider.setValue)


def decrypting():
    form.textEdit_2.setText(rasshifr(form.textEdit_1.toPlainText(), form.spinBox.value()))


def encrypting():
    form.textEdit_2.setText(shifr(form.textEdit_1.toPlainText(), form.spinBox.value()))




def checked_shifr_btn():
    encrypting()
    form.spinBox.valueChanged.connect(encrypting)
    form.textEdit_1.textChanged.connect(encrypting)
    form.shrsh_txt.setText('Зашифрованный текст')


def checked_rassh_btn():
    decrypting()
    form.spinBox.valueChanged.connect(decrypting)
    form.textEdit_1.textChanged.connect(decrypting)
    form.shrsh_txt.setText('Дешифрованный текст')



form.btn_rashifr.clicked.connect(checked_rassh_btn)
form.btn_zashifr.clicked.connect(checked_shifr_btn)




def exit_mainmenu():
    form.stackedWidget.setCurrentIndex(0)
    form.comboBox_3.setCurrentIndex(0)
    form.tabWidget.setCurrentIndex(0)
    form.textEdit_1.clear()
    form.spinBox.setValue(0)


form.exit_btn.clicked.connect(exit_mainmenu)

app.exec()
