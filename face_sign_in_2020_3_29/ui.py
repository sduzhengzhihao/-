from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(925, 509)
        self.btn_show_signed = QtWidgets.QPushButton(Dialog)
        self.btn_show_signed.setGeometry(QtCore.QRect(720, 200, 161, 41))
        self.btn_show_signed.setObjectName("btn_show_signed")
        self.btn_start = QtWidgets.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(720, 60, 161, 41))
        self.btn_start.setObjectName("btn_start")
        self.btn_show_unsigned = QtWidgets.QPushButton(Dialog)
        self.btn_show_unsigned.setGeometry(QtCore.QRect(720, 270, 161, 41))
        self.btn_show_unsigned.setObjectName("btn_show_unsigned")
        self.btn_screenshot = QtWidgets.QPushButton(Dialog)
        self.btn_screenshot.setGeometry(QtCore.QRect(720, 340, 161, 41))
        self.btn_screenshot.setObjectName("btn_screenshot")
        self.btn_sign_form = QtWidgets.QPushButton(Dialog)
        self.btn_sign_form.setGeometry(QtCore.QRect(720, 410, 161, 41))
        self.btn_sign_form.setObjectName("btn_sign_form")
        self.btn_end = QtWidgets.QPushButton(Dialog)
        self.btn_end.setGeometry(QtCore.QRect(720, 130, 161, 41))
        self.btn_end.setObjectName("btn_end")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(19, 30, 881, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(890, 40, 20, 431))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(690, 40, 20, 431))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(19, 460, 881, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.qtxt_showname = QtWidgets.QTextBrowser(Dialog)
        self.qtxt_showname.setGeometry(QtCore.QRect(470, 100, 211, 351))
        self.qtxt_showname.setObjectName("qtxt_showname")
        self.qlabel_video = QtWidgets.QLabel(Dialog)
        self.qlabel_video.setGeometry(QtCore.QRect(40, 60, 391, 391))
        self.qlabel_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.qlabel_video.setObjectName("qlabel_video")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(10, 40, 20, 431))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.lcd_signedCount = QtWidgets.QLCDNumber(Dialog)
        self.lcd_signedCount.setGeometry(QtCore.QRect(593, 50, 81, 41))
        self.lcd_signedCount.setObjectName("lcd_signedCount")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 60, 101, 31))
        self.label.setObjectName("label")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(440, 40, 30, 430))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "学生签到"))
        self.btn_show_signed.setText(_translate("Dialog", "已签到人员"))
        self.btn_start.setText(_translate("Dialog", "开始签到"))
        self.btn_show_unsigned.setText(_translate("Dialog", "未签到人员"))
        self.btn_screenshot.setText(_translate("Dialog", "签到截图"))
        self.btn_sign_form.setText(_translate("Dialog", "学生注册"))
        self.btn_end.setText(_translate("Dialog", "结束签到"))
        # self.qlabel_video.setText(_translate("Dialog", ""))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">已签到人数: </span></p></body></html>"))

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)  
    widget=QtWidgets.QWidget()  
    dlgUI=Ui_Dialog()
    dlgUI.setupUi(widget)
    widget.show()  
    sys.exit(app.exec_())