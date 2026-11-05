import shutil
import os

TO_SEPARATE = 'data'

os.makedirs(f'./{TO_SEPARATE}/FRONT', exist_ok=True)
os.makedirs(f'./{TO_SEPARATE}/DIAG', exist_ok=True)
os.makedirs(f'./{TO_SEPARATE}/SIDE', exist_ok=True)

def separate():
    for root, dirs, files in os.walk(f'./{TO_SEPARATE}/images'):

        for file in files:

            if 'Diag' in file:
                where = f'./{TO_SEPARATE}/images/{file}'
                destiny = f'./{TO_SEPARATE}/DIAG/{file}'
                shutil.copyfile(where, destiny)

            if 'Front' in file:
                where = f'./{TO_SEPARATE}/images/{file}'
                destiny = f'./{TO_SEPARATE}/FRONT/{file}'
                shutil.copyfile(where, destiny)

            if 'Side' in file:
                where = f'./{TO_SEPARATE}/images/{file}'
                destiny = f'./{TO_SEPARATE}/SIDE/{file}'
                shutil.copyfile(where, destiny)

    # os.rmdir(f'./{TO_SEPARATE}/images')

separate()
