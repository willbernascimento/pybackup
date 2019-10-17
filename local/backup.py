import sys
import os 

local_dir = input("Diretório local: ")

if os.path.exists(local_dir):
    print("diretorio local existe")
else:
    print("inserir diretório localexistente")

remot_dir = input("Diretório remoto: ")

if os.path.exists(remot_dir):
    print("remoto existe")
else:
    print("remoto não existe, tente novamente")


os.system("rsync - Cravzp {} {}".format(local_dir, remot_dir))
