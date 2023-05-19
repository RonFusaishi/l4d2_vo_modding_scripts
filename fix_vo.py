import os
import sys
import linecache
import subprocess
import shutil
from distutils.dir_util import copy_tree


directory=sys.argv[1]
filelist='fl_'+directory
samplerates='sr_'+directory

#backup directory
#try: 
#    copy_tree(directory, directory+"_old")
#except FileExistsError:
#    print("please delete "+directory+"_old or rename it")
#    sys.exit()

#work area
#workdir=r'custom\sound\player\survivor\voice\'+directory+'\'
#os.removedirs(workdir)
#os.makedirs(workdir)


#fixes samplerate
def sampling(samplerate, input):
    subprocess.call(["ffmpeg", "-i", input, "-ac", "1", "-ar", str(samplerate), "o.wav"])
    os.replace('o.wav', input)

#checks how many files in the metadata and uses that to determine when to stop while loop
with open(filelist) as f:
    ending=len(f.readlines())
    ending=ending+1


counter=1
while counter != ending:
    #File=directory+r"\"+linecache.getline(filelist, counter)
    File=os.path.join(directory, linecache.getline(filelist, counter))
    SRate=linecache.getline(samplerates, counter)

    sampling(SRate.strip(), File.strip())
    counter += 1

sys.exit()
