import os

lst = os.listdir("input_texts")
way = "D:" + os.sep + "Downloads" + os.sep
for fl in lst:
    os.system("mystem.exe" + " -n -i" + " input_texts" + os.sep + fl + " output_texts" + os.sep + fl)

