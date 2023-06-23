import os
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = 'Cinnamoroll'
SCRIPT_KEY = 'nxfkrngveayutwq!ijeyscK7a'
sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


class Shotgrid_model():
    def project_info(self):
        self.project_id = []
        self.project_name = []
        project_filters = [["sg_status", "is", "Active"]]
        self.projects = sg.find("Project", project_filters, fields=['id', 'name'])

        for project in self.projects:
            # print(project['name'])
            self.project_id.append(project['id'])
            self.project_name.append(project['name'])
        # print(self.project_id)
        return self.project_name

    def sequence_info(self, project_name):
        self.sequence_id = []
        self.sequence_code = []
        seq_filters = [['project.Project.name', 'is', project_name]]
        self.sequences = sg.find("Sequence", seq_filters, fields=['id', 'code'])
        # pprint(self.sequences)

        for sequence in self.sequences:
            self.sequence_id.append(sequence['id'])
            self.sequence_code.append(sequence['code'])
        # print(self.sequence_code)
        return self.sequence_code

    def shot_info(self, sequence_code):
        self.shot_id = []
        self.shot_code = []
        shot_filters = [['sg_sequence.Sequence.code', 'is', sequence_code]]
        self.shots = sg.find("Shot", shot_filters, fields=['id', 'code'])
        # pprint(self.shots)

        for shot in self.shots:
            self.shot_id.append(shot['id'])
            self.shot_code.append(shot['code'])
        # print(self.shot_code)
        return self.shot_code

    def task_info(self, entity_code):
        self.task_content = []
        task_filters = [['entity.Shot.code', 'is', entity_code]]
        self.tasks = sg.find("Task", task_filters, fields=['id', 'content'])
        # pprint(self.tasks)

        for task in self.tasks:
            self.task_content.append(task['content'])
        # print(self.task_content)
        return self.task_content

    def shot_version(self, project_name, shot_name, task_name, path):
        project_id = [["name", "is", project_name]]
        project = sg.find_one("Project", project_id)
        # pprint(project)

        shot_id = [['project.Project.name', 'is', project_name],
                   ['code', 'is', shot_name]]
        shot = sg.find_one("Shot", shot_id)
        # pprint(shot)

        task_id = [["content", "is", task_name]]
        task = sg.find_one("Task", task_id)
        # pprint(task)

        data = {'project': {'type': 'Project', 'id': project['id']},
                'code': 'upload_version',
                'description': '영상 올라갑니다.',
                'sg_status_list': 'rev',
                'entity': {'type': 'Shot', 'id': shot['id']},
                'sg_task': {'type': 'Task', 'id': task['id']},
                'user': {'type': 'HumanUser', 'id': 88}}

        version_create = sg.create('Version', data)
        # pprint(version_create['id'])
        version_id = version_create['id']
        video_file_path = path
        upload_name = os.path.basename(video_file_path)
        sg.upload("Version", version_id, video_file_path, field_name="sg_uploaded_movie", display_name=upload_name)


if __name__ == '__main__':
    cm = Shotgrid_model()
    cm.project_info()
    # cm.sequence_info()
    # cm.shot_info()
    # cm.task_info()
    # cm.upload_info()
    # cm.shot_version()

