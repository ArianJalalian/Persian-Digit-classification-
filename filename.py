import os

folder_path = 'C:/Users/HP/OneDrive/Desktop/Work/ML/Final Project/images'
prefixes = [str(i) for i in range(10)]

file_list = os.listdir(folder_path)

for i, prefix in enumerate(prefixes):
    for j in range(20):
        if (i * 20 + j) < len(file_list):
            old_file_name = file_list[i * 20 + j]
            new_file_name = f'{prefix}_{j+1}.jpg'
            
            old_file_path = os.path.join(folder_path, old_file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            
            os.rename(old_file_path, new_file_path)
