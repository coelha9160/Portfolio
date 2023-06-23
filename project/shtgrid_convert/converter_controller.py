import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

from converter_view import My_view
from converter_model import Convert_model
from shotgrid_model import Shotgrid_model


class Converter_controller(My_view):
    def __init__(self):
        super().__init__()

        self.cm = Convert_model()
        self.sm = Shotgrid_model()

        self.path = None

        self.openButton.clicked.connect(self.open)
        self.uploadButton.clicked.connect(self.convert)
        self.update_project_combo()
        self.proj.currentTextChanged.connect(self.update_sequence_combo)
        self.seq.currentTextChanged.connect(self.update_shot_combo)
        self.shot.currentTextChanged.connect(self.update_task_combo)
        self.task.currentTextChanged.connect(self.update_label_text)

    def open(self):
        self.path = QFileDialog.getExistingDirectory(self, "select" )
        self.label_path.setText(self.path)
        
    def convert(self):
        self.cm.convert_seq_to_mov(self.path)

        self.upload_file()

    def update_project_combo(self):
        self.proj.clear()
        self.sm.project_info()

        for self.sm.project in self.sm.projects:
            self.proj.addItem(self.sm.project['name'])

    def update_sequence_combo(self, project_name):
        self.seq.clear()
        self.sm.sequence_info(project_name)

        for self.sm.sequence in self.sm.sequences:
            self.seq.addItem(self.sm.sequence['code'])

    def update_shot_combo(self, sequence_code):
        self.shot.clear()
        self.sm.shot_info(sequence_code)

        for self.sm.shot in self.sm.shots:
            self.shot.addItem(self.sm.shot['code'])

    def update_task_combo(self, entity_code):
        self.task.clear()
        self.sm.task_info(entity_code)

        for self.sm.task in self.sm.tasks:
            self.task.addItem(self.sm.task['content'])

    def update_label_text(self, text):
        self.upload_path.setText(f"경로 : {text}")

    def upload_file(self):
        project_name = self.proj.currentText()
        # print(project_name)
        entity_code = self.shot.currentText()
        # print(entity_code)
        task_content = self.task.currentText()
        # print(task_content)

        path = self.cm.output

        self.sm.shot_version(project_name, entity_code, task_content, path)


def main():
    app = QApplication(sys.argv)
    controller = Converter_controller()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
