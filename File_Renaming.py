import os
location = os.getcwd()
name='mp3'
for path,dir_names,file in os.walk(location):
    for f in file:
       if f not in "File_Renaming.py":
           #print(f)
            split = os.path.splitext(f)
            old_fl = os.path.join(path,f)
            nw_fl=os.path.join(path,f'{split[0]}.{name}')
            os.rename(old_fl,nw_fl)



