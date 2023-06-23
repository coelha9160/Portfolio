import os

class Model:
    def __init__(self, dirname):
        self.dirname = dirname
        self.list_path = []
        self.list_blender_path = []
        self.file_name = []

    def search(self):
        try:
            filenames = os.listdir(self.dirname)
            for filename in filenames:
                full_filename = os.path.join(self.dirname, filename)
                if os.path.isdir(full_filename):
                    sub_search = Model(full_filename)
                    sub_search.search()
                    self.list_path.extend(sub_search.list_path)
                    self.list_blender_path.extend(sub_search.list_blender_path)
                    self.file_name.extend(sub_search.file_name)
                else:
                    ext = os.path.splitext(full_filename)[-1]
                    parent_folder = os.path.basename(self.dirname)
                    if ext == '.jpg' and parent_folder == os.path.splitext(filename)[0]:
                        self.list_path.append(full_filename)
                        self.file_name.append(parent_folder)
                    if ext == '.blend' and parent_folder == os.path.splitext(filename)[0]:
                        self.list_blender_path.append(full_filename)
        except PermissionError:
            pass


if __name__ == '__main__':
    model = Model("C:\\Users\\user\\Desktop\\GIT\\Portfolio\\project\\Folder base asset library\\base folder")
    model.search()
    print(model.list_path)
    print(model.list_blender_path)
    print(model.file_name)