import os

base_folder = 'day'

for i in range(1, 31):
    folder_name = f"{base_folder}{i}"
    os.mkdir(folder_name)

    with open(os.path.join(folder_name, '.gitkeep'), 'w') as f:
        pass