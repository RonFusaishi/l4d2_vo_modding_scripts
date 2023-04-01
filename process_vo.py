import os
import sys
import linecache
import subprocess
import shutil
from distutils.dir_util import copy_tree


directory=sys.argv[1]
filelist=os.path.join('metabank', 'fl_'+directory)
durations=os.path.join('metabank', 'durg_'+directory)
samplerates=os.path.join('metabank', 'sr_'+directory)

#backup directory
try: 
    copy_tree(directory, directory+"_old")
except FileExistsError:
    print("please delete "+directory+"_old or rename it")
    sys.exit()

#work area
#workdir=r'custom\sound\player\survivor\voice\'+directory+'\'
#os.removedirs(workdir)
#os.makedirs(workdir)



#fixes duration
def shrink(time, input):
    subprocess.call(["ffmpeg", "-t", str(time), "-i", input, "o.wav"])
    os.replace('o.wav', input)

def extend(duration, time, input):
    difference=abs(duration-time)
    subprocess.call(["ffmpeg", "-i", input, "-af", "apad=pad_dur="+str(difference), "o.wav"])
    os.replace('o.wav', input)
#fixes samplerate
def sampling(samplerate, input):
    subprocess.call(["ffmpeg", "-i", input, "-ac", "1", "-ar", str(samplerate), "o.wav"])
    os.replace('o.wav', input)
#determines if file should be extended or cut
def determine(input, duration, uniform_duration, samplerate):
    if duration > uniform_duration:
        shrink(uniform_duration, input)
        sampling(samplerate, input)
    else:
        extend(duration, uniform_duration, input)
        sampling(samplerate, input)

#checks how many files in the metadata and uses that to determine when to stop while loop
with open(filelist) as f:
    ending=len(f.readlines())
    ending=ending+1


counter=1
while counter != ending:
    #File=directory+r"\"+linecache.getline(filelist, counter)
    File=os.path.join(directory, linecache.getline(filelist, counter))
    SRate=linecache.getline(samplerates, counter)
    Dur=float(linecache.getline(durations, counter))

    #get file duration
    with open('temp', 'w') as out:
        subprocess.call(["ffprobe", File.strip(), "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"], stdout=out)
    with open('temp', 'r') as out:
        duration=float(out.read())
    os.remove('temp')
    #####

    determine(File.strip(), duration, Dur, SRate.strip())
    counter += 1

# python equivalent to wc -l
#with open('compression.py') as f:
#   len(f.readlines())
