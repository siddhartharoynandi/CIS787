from bloomfilter import BloomFilter
from random import shuffle

word_present = []
inFile = open("/Users/siddhartharoynandi/Desktop/listed_username_30.txt")
for line in inFile:
    word_present.append(line)

n = len(word_present)  # no of items to add
p = 0.05  # false positive probability

bloomf = BloomFilter(n, p)
#print("Size of bit array:{}".format(bloomf.size))
#print("False positive Probability:{}".format(bloomf.fp_prob))
#print("Number of hash functions:{}".format(bloomf.hash_count))

for item in word_present:
    bloomf.add(item)

word_tobe_tested = []
inFile = open("/Users/siddhartharoynandi/Desktop/listed_username_365.txt")
for line in inFile:
    word_tobe_tested.append(line)


shuffle(word_present)
shuffle(word_tobe_tested)

count = 0
count1 = 0

for word in word_tobe_tested:
    if bloomf.check(word):
        count1 = count1 + 1
        if word in word_present:
            #print("'{}' is probably present!".format(word))
            continue
        else:
            #print("'{}' is a false positive!".format(word))
            count = count + 1
    #else:
        #print("'{}' is definitely not present!".format(word))
f = open('/Users/siddhartharoynandi/Desktop/FM/bloomFilter.txt', 'w')
f.write('Number of hash functions: 5')
f.write('FPR : 0.1')
f.write("Number of hash functions:{}".format(bloomf.hash_count))
f.write('FPR : '+str(float(count/count1)))
f.close()

