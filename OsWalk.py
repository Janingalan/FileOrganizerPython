import os
import shutil

path = "/Users/johneltonaningalan/Desktop/MonitorFolder"                                #You can change it to any different folder like Downloads or Documents

l = os.listdir(path)
for entry in os.scandir(path):
        if entry.is_dir():                              #ignores all the sub directories that is inside the directories itself
            continue
        else:
            if entry.name == '.DS_Store':
                continue                                #ignores .DS_Store lingering on the directory
            print(f"File name {entry.name} and the extension is {os.path.splitext(entry)[1]}")             #identifying the file name and the file extension    
            ext = os.path.splitext(entry)[1]            #file extension identifier
            print(ext)
            
            new_path = path + "/" + ext                 #creating new path
            print(new_path)
            isFile = os.path.isdir(new_path)                    #checking if the directory already exist
            print(isFile)

            if isFile == False:
                    os.mkdir(new_path)                                  #If path does't exist make a new path
                    print(new_path)
                    print("New Directory was created")
                    print(entry.name)
                    original = path +"/" + entry.name
                    print(original)
                    shutil.move(original, new_path + "/" + entry.name)    #Moving the file into its new destination
                    
                    

            else:
                    print("Directory already exist there fore it shall be moved")                       #If file already exist no need to create a new directory
                    print(entry.name)
                    original = path +"/" + entry.name
                    print(original)
                    shutil.move(original, new_path + "/" + entry.name)                                          #Moving the files to its new destination
                    continue           
            
#Does't need to organize any oh the folders thats already made. 
            

        


