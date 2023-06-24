import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, QLabel


class My_view(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet('font-size: 30px;')
        self.setWindowTitle('Converter')

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Converter')

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.proj = QComboBox()
        self.seq = QComboBox()
        self.shot = QComboBox()
        self.task = QComboBox()
        hbox.addWidget(self.proj)
        hbox.addWidget(self.seq)
        hbox.addWidget(self.shot)
        hbox.addWidget(self.task)

        vbox.addLayout(hbox)

        self.openButton = QPushButton("Open")
        self.uploadButton = QPushButton("Convert / Upload")
        self.upload_path = QLabel()
        self.label_path = QLabel()
        vbox.addWidget(self.openButton)
        vbox.addWidget(self.uploadButton)
        vbox.addWidget(self.upload_path)
        self.upload_path.setText('패스입니다')
        vbox.addWidget(self.label_path)
        self.label_path.setText('경로입니다')
        
        self.openButton.clicked.connect(self.open_info)
        self.uploadButton.clicked.connect(self.upload_info)

        self.setLayout(vbox)

        self.show()
        
    def open_info(self):
        print("The button to locate the directory.")
        
    def upload_info(self):
        print("This is a button that executes converting and uploading.")
        

def main():
    app = QApplication(sys.argv)
    view = My_view()
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()