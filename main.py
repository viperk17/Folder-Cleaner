import os


def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def movefiles(foldername, file):
    for file in files:
        os.replace(file, f"{foldername}/{file}")    # to move files to folders

files = os.listdir('/home/flyboypk/Downloads')
# files.remove("main.py")

CreateIfNotExist('Images')
CreateIfNotExist('Docs')

imgExists = [".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExists ]

docExists = [".txt",".docx",".doc",".pdf",".xls",".xlsx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExists ]


movefiles("Images", images)
movefiles("Docs", docs)
