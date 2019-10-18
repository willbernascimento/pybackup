
import os
from datetime import date


def main():
    rsync_setup()


def backup_setup():
    while True:
        dir_origin = input("Enter a origin path: ")
        if not os.path.exists(dir_origin):
            print("Enter a valid origin path.")
            continue
        break

    while True:
        dir_destine = input("Enter a destine path: ")
        if not os.path.exists(dir_destine):
            print("Destine path does not exists. Enter a valid path:")
            continue
        break

    backup_name = input("Enter a backup name (if empty default is \"backup\"): ")
    backup_date = date.today().strftime("%d-%m-%Y")

    if backup_name == "":
        backup_name = 'backup'
    backup_name = backup_name + "-" + backup_date
    backup_path = os.path.join(dir_destine, backup_name)
    return dir_origin, backup_path

    # print("Path origin: {}\n"
    #       "Path destino: {}\n"
    #       "Nome backup: {}\n"
    #       "Path backup: {}".format(dir_origin, dir_destine, backup_name, backup_path))


def rsync_setup():
    opt_sync = "-Cravzp"
    opt_exclude = "*.txt"
    dir_origin, backup_path = backup_setup()
    os.system("rsync {} --exclude {} {} {}".format(opt_sync, opt_exclude, dir_origin, backup_path))


if __name__ == '__main__':
    main()
