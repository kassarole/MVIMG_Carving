# Written by Kevin Rode
import os, exiftool
for file in os.listdir(os.getcwd()):
    try:
        with exiftool.ExifTool() as et:
            offset = et.get_tag('MicroVideoOffset', file)
        if offset != None and offset != '' :
            print(offset)
            size = os.path.getsize(file)
            print(offset)
            offset = int(size)-int(offset)
            with open(file, "rb") as infile:
                infile.seek(int(offset))
                data = infile.read()
            with open(file+".mp4", "wb") as outfile:
                outfile.write(data)
        else:
            pass
    except ValueError:
        pass
