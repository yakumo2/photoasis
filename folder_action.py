import json
import re
import os

def get_sorted_folders():
    # 读取文件夹信息并排序
    folders = get_folders_from_json()
    folders.sort(key=lambda x: int(x['id']), reverse=True)
    return folders

def get_folders_from_json():
    # 从 JSON 文件中读取文件夹信息
#    with open('folders.json', 'r') as f:
    folders = load_folders()
    return folders

def list_folders_to_json(path, output_file):
    # Load existing folders from JSON file
    existing_folders = load_folders()
    
    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            folder_id = extract_id(folder)
            # Check if folder_id already exists in existing_folders
            if not any(folder['id'] == folder_id for folder in existing_folders):
                existing_folders.append({'id': folder_id, 'path': folder, 'name': folder, 'display': False})
    with open(output_file, 'w') as f:
        json.dump(existing_folders, f, indent=4)  # 添加缩进
    print("Scanned folders")

# Helper function to load folders from JSON file
'''
def load_folders():
    with open('folders.json', 'r') as f:
        return json.load(f)
'''

def load_folders():
    if not os.path.exists('folders.json'):
        create_folders_json()
    with open('folders.json', 'r') as f:
        return json.load(f)

def create_folders_json():
    data = [{
        "id": 0,
        "path": "0_default",
        "name": "default",
        "display": False
    }]
    with open('folders.json', 'w') as f:
        json.dump(data, f, indent=4)




def extract_id(folder_name):
    # 使用正则表达式从文件夹名中提取数字作为ID
    match = re.search(r'\d+', folder_name)
    if match:
        return int(match.group())
    else:
        return 0

# Helper function to save folders to JSON file
def save_folders(folders):
    print("Current working directory:", os.getcwd())
    with open('folders.json', 'w') as f:
        json.dump(folders, f, indent=4)







