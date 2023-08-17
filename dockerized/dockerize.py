import os
import subprocess

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def write_file(file_path, contents):
    with open(file_path, 'w') as f:
        f.write(contents) 

def main(parent_path):
    dockerized_path = f'{parent_path}/dockerized'
    if not os.path.exists(dockerized_path):
        os.mkdir(dockerized_path)

    ignored_dir = ['.git', 'venv', '__pycache__', 'dockerized']
    dir_paths = []

    # Loop the parent directory
    for node in os.listdir(parent_path):
        if node in ignored_dir:
            continue

        p_current = f'{parent_path}/{node}'
        p_dockerized_current = f'{dockerized_path}/{node}'

        if os.path.isdir(p_current):
            # Append the directory name to directory paths
            dir_paths.append(node)
        elif os.path.isfile(p_current):
            # Copy the file from parent directory to the dockerized directory
            content = read_file(p_current)
            write_file(p_dockerized_current, content)
    
    while len(dir_paths) != 0:
        path = dir_paths.pop(0)
        # Combine the parent path and the popped directory paths.
        current_dir_path = f'{parent_path}/{path}'

        for node in os.listdir(current_dir_path):
            if node in ignored_dir:
                continue
            
            # Path of the file or directory in parent path
            current_node = f'{current_dir_path}/{node}'

            # Path of the file and directory in dockerized path
            dockerized_current_path = f'{dockerized_path}/{path}'
            dockerized_current_node = f'{dockerized_path}/{path}/{node}'

            if os.path.isdir(current_node):
                # Concatenate path and the child of the path
                dir_paths.append(f'{path}/{node}')
                # Create the directory for dockerized path
                if not os.path.exists(dockerized_current_path):
                    os.mkdir(dockerized_current_path)
            elif os.path.isfile(current_node):
                # Copy the file from parent directory to the dockerized directory
                content = read_file(current_node)
                # Create the directory for dockerized path
                if not os.path.exists(dockerized_current_path):
                    os.mkdir(dockerized_current_path)
                write_file(dockerized_current_node, content)

if __name__ == '__main__':
    pwd = 'pwd'
    result = subprocess.run(pwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    main(result.stdout.replace('\n', ''))