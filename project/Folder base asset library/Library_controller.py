import sys
from Library_model import Model
from stylesheet import Stylesheet
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets, QtGui, QtCore


class Library(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = Model("C:\\Users\\user\\Desktop\\GIT\\Portfolio\\project\\Folder base asset library\\base folder")
        self.model.search()
        self.ss = Stylesheet()

        self.setWindowTitle("Library")
        self.setGeometry(350, 200, 1280, 720)

        self.my_button = QtWidgets.QPushButton('Library', self)
        self.my_button.setFixedSize(150, 100)
        self.my_button.move(550, 310)
        self.ss.style1(self.my_button)
        self.my_button.clicked.connect(self.my_button_clicked)

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.resizeEvent = self.handleResize
        self.my_button_clicked()

    def my_button_clicked(self):
        screen_width = self.width()
        max_columns = max(1, screen_width // 300)

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        row = 0
        col = 0

        for path, url, filename in zip(self.model.list_path, self.model.list_blender_path, self.model.file_name):
            pixmap = QtGui.QPixmap(path)
            label = QtWidgets.QLabel()
            label.setPixmap(pixmap.scaledToWidth(250, QtCore.Qt.SmoothTransformation))
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.mousePressEvent = lambda event, url=url: self.open_image(url)
            self.ss.style2(label)
            layout.addWidget(label, row, col)

            file_label = QtWidgets.QLabel(filename)
            self.ss.style3(file_label)
            file_label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(file_label, row + 1, col)

            col += 1
            if col == max_columns:
                row += 2
                col = 0

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        self.setCentralWidget(scroll_area)

    def open_image(self, url):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(url))

    def handleResize(self, event):
        layout = self.centralWidget().widget().layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
        self.my_button_clicked()


def main():
    app = QtWidgets.QApplication()
    myapp = Library()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()