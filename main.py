import os
folder = './'
out_file = open("./lista_arquivos.txt", "w")
for path, subfolder, files in os.walk(folder):
    for file in files:
      out_file.write(os.path.join(path,file,"\n"))
      print(os.path.join(path,file))
        #print(os.path.join(path, file))
        #print(folder,file)
        #print(os.path.join(os.path.realpath(), arquivo))
out_file.close()
