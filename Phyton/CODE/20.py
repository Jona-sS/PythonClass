import glob

for filename in glob.glob(r"\Users\Jonas\Desktop\6.Semester\Phyton\CODE\*.py"):
    with open(filename, 'r') as file:
        content = file.read()
        if content.find('print') != -1:
            print(filename)