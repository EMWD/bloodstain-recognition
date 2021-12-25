import os
path = 'data/impact_beating/'
files = os.listdir(path)

name_prefixes = {
    'gunshots': 'gs_',
    'impact_beating': 'ib_',
}

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(
        path, ''.join(['ib_' + str(index+1), '.jpg'])))
