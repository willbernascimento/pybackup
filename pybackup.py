import os
from datetime import date


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


def rsync_setup():
    dir_origin, backup_path = backup_setup()
    opt_sync = "-Cravzp"
    user_exclude = input("File extension to exclude (ex: '*.txt)': ")
    opt_exclude = ""
    if user_exclude == "":
        os.system("rsync {} {} {}".format(opt_sync, dir_origin, backup_path))
    else:
        user_exclude = user_exclude.replace(" ", ",")
        opt_exclude = user_exclude
        os.system("rsync {} --exclude={{{}}} {} {}".format(opt_sync, opt_exclude, dir_origin, backup_path))


if __name__ == '__main__':
    rsync_setup()

# user_exclude.replace(" ", "','")