import os

for (path, dir, files) in os.walk("letter_templates"):
    print(path)
    print(files)
    print(f'{path}/{files}')
    for file in zip(path, files):
        print(file)
