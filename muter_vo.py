import os
import linecache
import sys
import shutil
actor=sys.argv[1]
null='null.wav'
refer=os.path.join('metabank', 'fl_'+actor)

try:
    os.makedirs(actor)
except FileExistsError:
    print("please delete or rename the folder called " + actor)
    sys.exit()

with open(refer) as f:
    ending=len(f.readlines())
    ending=ending+1


counter=1
while counter != ending:
    file=linecache.getline(refer, counter)
    output=os.path.join(actor, file.strip())
    shutil.copyfile(null, output)
    counter += 1
