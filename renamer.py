import os
gs_path = 'data/gunshots/'
ib_path = 'data/impact_beating/'

gs_files = os.listdir(gs_path)
ib_files = os.listdir(ib_path)

name_prefixes = {
    'gunshots': 'gs_',
    'impact_beating': 'ib_',
}

for index, file in enumerate(gs_files):
    os.rename(os.path.join(gs_path, file), os.path.join(
        gs_path, ''.join([name_prefixes.get('gunshots') + str(index+1), '.jpg'])))

for index, file in enumerate(ib_files):
    os.rename(os.path.join(ib_path, file), os.path.join(
        ib_path, ''.join([name_prefixes.get('impact_beating') + str(index+1), '.jpg'])))