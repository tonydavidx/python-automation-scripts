""" A script to open random file from a directory """
import os
import random

video_folder = r"G:/videos/Educational"


def open_file(file_name):
    try:
        os.startfile(file_name)
    except Exception as e:
        print("error")


def main(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    random_video = random.choice(files)
    open_file(random_video)


if __name__ == "__main__":
    main(video_folder)
