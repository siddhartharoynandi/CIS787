from os import listdir
from os.path import isfile, join
import jenkins_cffi as jenkins
import mmh3
import numpy as np
import glob, os
import gzip

if __name__ == '__main__':
    #onlyfiles = [f for f in listdir('/Users/siddhartharoynandi/Desktop/FM/') if isfile(join('/Users/siddhartharoynandi/Desktop/FM/', f))]
    filenames = []
    trail_zero = []
    os.chdir("/Users/siddhartharoynandi/Desktop/FM")
    n = 64
    x = None
    for file in glob.glob("*.gz"):
        filenames.append(file)
    print filenames
    for i in filenames:
        file = gzip.open('/Users/siddhartharoynandi/Desktop/FM/'+i,'r')
        #print file
        for line in file:
            if line.startswith('Q'):
                x = line[1:].strip('\n')
                x = x.strip('\t')
                x = x.replace('\\','')
                ############ Creating the BitMap Array for the Q element of size 64 ################
                bitmap_array = np.zeros((n), dtype=np.int)
                ############## After Hashing Generating hashkey's binary equilvalant ##########
                ix = list(bin(jenkins.hashlittle(str(x)))[2:])
                #iy = list(bin(mmh3.hash(str(x),signed=False))[2:])
                #print ix
                length_bin = len(ix)
                len_bitmap = 64
                v = len_bitmap - length_bin
                ############## Populating 1 in BitMap Array #################
                for j, i in enumerate(ix):
                    if i == '1':
                        bitmap_array[v + j] = 1
                b = list(bitmap_array)
                #print b
                ############## Counting Trailing Zeroes for each element in BitMap #############
                trail_zero.append(b[::-1].index(1))
                #print bitmap_array
    #print trail_zero
    max_zero = max(trail_zero)
    distinct_jenkins = 2 ** max_zero
    distinct_murmur = 2 ** (max_zero-1)
    #print max_zero
    f = open('/Users/siddhartharoynandi/Desktop/FM/countDistinctWords.txt', 'w')
    f.write('Number of Distinct Words in MemeTracker using Jenkins Hash: '+str(distinct_jenkins)+'\n')
    f.write('Number of Distinct Words in MemeTracker using Murmur Hash: ' + str(distinct_murmur)+'\n')
    f.write('Average number of distinct elements: '+str((distinct_jenkins+distinct_murmur)/2))
    f.close()
    exit(0)

