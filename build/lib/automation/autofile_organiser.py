#automation tool for auto file organizer
import os
import shutil
path_to_organize = input("Enter the file")

file_types = {
   "Images":[".jpg",".png",".jpeg",".gif",".bmp"],
   "Documents":[".pdf",".doc",".docx",".ppt",".pptx"],
   "Videos":[".mp4",".mov",".avi",".wmv"],
   "Archives":[".zip",".tar",".tar.gz",".tar.bz"],
   "Music":[".mp3",".m4a",".flac"]
}
#loop through my path where I need to organise and list them
for filename in os.listdir(path_to_organize):
   print(filename)

   file_path = os.path.join(path_to_organize, filename)
   print(file_path)
   #no need to use folders(skip folder)
   if os.path.isdir(file_path):
       continue
   moved = False

   for folder, extensions in file_types.items():

       if filename.lower().endswith(tuple(extensions)):

           folder_path = os.path.join(path_to_organize, folder)

           # if there is no folder, then create
           if not os.path.exists(folder_path):
               os.makedirs(folder_path)

           # move the files to the folder
           shutil.move(file_path, folder_path)
           moved = True
           break
       if not moved:
           others_path = os.path.join(path_to_organize, "others_files")
           if not os.path.exists(others_path):
               os.makedirs(others_path)
               shutil.move(file_path, others_path)
           else:
               print(f"{filename} already exist, skipping")

   print("files moved successfully")

