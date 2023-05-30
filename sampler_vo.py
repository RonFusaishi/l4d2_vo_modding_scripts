import os
import random
import linecache
import shutil

######################
refer="fl_namvet"
sample_dir="bellic/generic"
sample_name="niko"
output="namvet"
######################


with open(refer) as f:
    ending=len(f.readlines())
    ending=ending+1

#file_list=os.path.join('metabank', actor)

counter=1
while counter != ending:
    sample_size=len(os.listdir(sample_dir)) - 1
    rng=random.randint(0, sample_size)
    #rng=random.randint(0, len(os.listdir(sample_dir)))
    file=linecache.getline(refer, counter)
    sample=os.path.join(sample_dir, sample_name+str(rng)+'.wav')
    shutil.copy(sample, os.path.join(output, file.strip()))
    counter += 1
