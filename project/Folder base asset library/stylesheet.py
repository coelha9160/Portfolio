from PySide2 import QtGui


class Stylesheet():

    def style1(self, name):
        name.setStyleSheet("color: white;"
                                     "background-color: qlineargradient"
                                     "(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955,"
                                     "stop:0 rgba(10, 242, 251, 255),"
                                     "stop:1 rgba(224, 6, 159, 255));"
                                     "border-radius: 20px;")

    def style2(self, name):
        name.setStyleSheet("border-style: dashed;"
                            "border-width: 3px;"
                            "background-color: white;"
                            "border-radius: 10px")

    def style3(self, name):
        name.setFont(QtGui.QFont("궁서", 20))
        name.setStyleSheet("Color : pink;")
