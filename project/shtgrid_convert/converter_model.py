import os
import subprocess


class Convert_model():
    def __int__(self):
        self.output = None

    def convert_seq_to_mov(self, input):
        file_name = os.path.split(input)
        # folder path
        pull_path = f"{input}/{file_name[1]}-%4d.jpg"
        self.output = f"{input}/output.mp4"
        frame_rate = 24
        cmd = f'ffmpeg -framerate {frame_rate} -i "{pull_path}" "{self.output}"'
        print(cmd)
        subprocess.run(cmd, shell=True)


def main():
    cm = Convert_model()
    cm.convert_seq_to_mov()


if __name__ == '__main__':
    main()
