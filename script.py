import os

base_folder = 'day'

for i in range(1, 31):
    if i > 0 and i < 10:
        folder_name = f"{base_folder}{'0'}{i}"
        os.mkdir(folder_name)
    else:
        folder_name = f"{base_folder}{i}"
        os.mkdir(folder_name) 

    with open(os.path.join(folder_name, '.gitkeep'), 'w') as f:
        pass