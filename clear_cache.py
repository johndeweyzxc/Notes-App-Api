import shutil
import subprocess
import os

def is_pycache(current_path, current):
    if current == '__pycache__':
        shutil.rmtree(f'{current_path}/__pycache__')
        return f'{current_path}/__pycache__'
    else:
        return False

def main(parent_path):
    path_list = []
    path_list.append(parent_path)

    pycache_deleted = []

    while len(path_list) != 0:
        current_path = path_list.pop(0)
        for current in os.listdir(current_path):
            # Do not delete pycache at venv and .git repository
            if current == 'venv' or current == '.git':
                continue
            if os.path.isfile(f'{current_path}/{current}'):
                continue
            
            pycache = is_pycache(current_path, current)
            if not pycache:
                path_list.append(f'{current_path}/{current}')
            else:
                pycache_deleted.append(pycache)
    
    print('pycache deleted:')
    for i in pycache_deleted:
        print(i.replace(parent_path, ''))

if __name__ == '__main__':
    pwd = 'pwd'
    result = subprocess.run(pwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    main(result.stdout.replace('\n', ''))