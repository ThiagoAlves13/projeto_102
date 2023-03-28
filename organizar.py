import os
import shutil

from_dir ="C:/Games/PRO_1-1_C102_AtividadeDoAluno1-main/PRO_1-1_C102_AtividadeDoAluno1-main"
to_dir ="E:/THIAGO/Área de Trabalho/fotos_aula102"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    #if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
    if extension in['.txt','.pdf','.doc','.docx']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "arquivo_texto"
        path3 = to_dir + '/' + "arquivo_texto" + '/' + file_name

        if os.path.exists(path2):
           print("movendo...")
           shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movendo...")
            shutil.move(path1,path3)