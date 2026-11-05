import os 
import shutil

INITIAL_DIR = 'data'
FINAL_DIR = 'final'

os.makedirs(f'./{FINAL_DIR}/images', exist_ok=True)
os.makedirs(f'./{FINAL_DIR}/labels', exist_ok=True)

def get_labels():
    ids = []
    for root, dirs, files in os.walk(f'./{INITIAL_DIR}/labels'):
        for file in files:
            name = file.split('.')[0]
            where = f'./{INITIAL_DIR}/labels/{file}'
            destiny = f'./{FINAL_DIR}/labels/{file}'

            ids.append(name)
            shutil.copyfile(where, destiny)
 
    return ids

OK_images_JSN = get_labels()

def do_final_dataset():
    for root, dirs, files in os.walk(f'./{INITIAL_DIR}/images'):

        for file in files:
            name = file.split('.')[0]

            if name in OK_images_JSN:
                where = f'./{INITIAL_DIR}/images/{file}'
                destiny = f'./{FINAL_DIR}/images/{file}'
                shutil.copyfile(where, destiny)

do_final_dataset()
