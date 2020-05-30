import os

def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def movefiles(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")    # to move files to folders
        # os.replace(file, "{foldername}/{file}")


if __name__ == "__main__":

    files = os.listdir('/home/flyboypk/PycharmProjects/FolderCleaner/')
    files.remove("main.py")

    CreateIfNotExist('Images')
    CreateIfNotExist('Docs')
    CreateIfNotExist('Media')
    CreateIfNotExist('Others')

    imgExists = [".png",".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExists ]

    docExists = [".txt",".docx",".doc",".pdf",".xls",".xlsx",".iso",".ova",".deb",".zip"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExists ]

    mediaExists = [".mp3",".mp4",".mkv",".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExists ]

    others = []
    for file in files:
        exists = os.path.splitext(file)[1].lower()
        if (exists not in mediaExists) and (exists not in docExists) and (exists not in imgExists) and os.path.isfile(file):
            others.append(file)

    movefiles("Images", images)
    movefiles("Docs", docs)
    movefiles("Media", medias)
    movefiles("Others", others)
