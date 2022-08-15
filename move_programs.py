import shutil
import os
import glob

src = "D:/Downloads/"
dest = "F:/Programs/"
extentsions = ["exe", "msi"]
programs = []

for e in extentsions:
    for file in glob.glob(src + "*." + e):
        programs.append(file)
        print(file)

for program in programs:
    filename = os.path.basename(program)
    program_dst = dest + filename
    print(f"moving {filename}")
    shutil.move(program, program_dst)
