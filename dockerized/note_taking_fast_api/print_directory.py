import os
import subprocess

def main(parent_path):
    path_list = []
    path_list.append(parent_path)
    ignored_dir = ['.git', 'venv', '__pycache__']

    file_paths = []

    while len(path_list) != 0:
        current_path = path_list.pop(0)

        for current in os.listdir(current_path):
            if os.path.isfile(f'{current_path}/{current}'):
                file_paths.append(f'{current_path}/{current}')
            else:
                if current not in ignored_dir:
                    path_list.append(f'{current_path}/{current}')
    
    print('files:')
    for i in file_paths:
        print(i.replace(parent_path, ''))

if __name__ == '__main__':
    pwd = 'pwd'
    result = subprocess.run(pwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    main(result.stdout.replace('\n', ''))