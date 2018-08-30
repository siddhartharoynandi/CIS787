import string
import re

import operator
from sklearn.cluster import KMeans
import numpy as np

LSW = ['<br','/><br','a',"able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","after","afterwards","again","against","ah","all","almost","alone","along","already","also","although","always","am","among","amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","are","aren","arent","arise","around","as","aside","ask","asking","at","auth","available","away","awfully","b","back","be","became","because","become","becomes","becoming","been","before","beforehand","begin","beginning","beginnings","begins","behind","being","believe","below","beside","besides","between","beyond","biol","both","brief","briefly","but","by","c","ca","came","can","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","could","couldn't","d","date","did","didn't","different","do","does","doesn't","doing","done","don't","down","downwards","due","during","e","each","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","et-al","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","few","ff","fifth","first","five","fix","followed","following","follows","for","former","formerly","forth","found","four","from","further","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","had","happens","hardly","has","hasn't","have","haven't","having","he","hed","hence","her","here","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","hid","him","himself","his","hither","home","how","howbeit","however","hundred","i","id","ie","if","i'll","im","immediate","immediately","importance","important","in","inc","indeed","index","information","instead","into","invention","inward","is","isn't","it","itd","it'll","its","itself","i've","j","just","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","m","made","mainly","make","makes","many","may","maybe","me","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","now","nowhere","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","omitted","on","once","one","ones","only","onto","or","ord","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","s","said","same","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","she","shed","she'll","shes","should","shouldn't","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","so","some","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","such","sufficiently","suggest","sup","sure","t","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that've",'the',"their","theirs","them","themselves","then","thence","there","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","these","they","theyd","they'll","theyre","they've","think","this","those","thou","though","thoughh","thousand","throug","through","throughout","thru","thus","til","tip","to","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","under","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","very","via","viz","vol","vols","vs","w","want","wants","was","wasnt","way","we","wed","welcome","we'll","went","were","werent","we've","what","whatever","what'll","whats","when","whence","whenever","where","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","while","whim","whither","who","whod","whoever","whole","who'll","whom","whomever","whos","whose","why","widely","willing","wish","with","within","without","wont","words","world","would","wouldnt","www","x","y","yes","yet","you","youd","you'll","your","youre","yours","yourself","yourselves","you've","z","zero"]
#LSW = ['a','the']

def getProcessedList():
    dictionary_words = {}
    cleaned_reviews = []
    #punctuation = string.punctuation
    #punctuation1 = punctuation.replace('\'', '')
    inFile = open("/Users/siddhartharoynandi/Desktop/finefoods.txt")
    for line in inFile:
        if 'review/text:' in line:
            s = line[12:].replace('.',' ').lower()
            s2 = s.replace(',','')
            s1 = s2.replace('\xd5',"'")
            #s1 = line[12:].lower()
            #review = "".join(l for l in s1 if l not in punctuation1)
            review = s1.replace('/>', '')
            review = review.split() # list of words in the review
            #print('1: '+ str(review))

            # remove stopwords from review
            #review.remove('i')
            for _word in reversed(review):
                #print(_word)
                #print(index)
                if _word in LSW:
                    index = review.index(_word)
                    #print ('Before deleting the word '+str(_word))
                    review.remove(_word)
                    #print('After Removal' + str(review))

            cleaned_reviews.append(review)
            #print('2' + str(review))


            for _word in review:
                if _word in dictionary_words:
                    dictionary_words[_word] += 1
                else:
                    dictionary_words[_word] = 1

    sorted_word_freq = sorted(dictionary_words.items(), key=operator.itemgetter(1), reverse=True)[:500]
    #print(sorted_word_freq)
    f = open('/Users/siddhartharoynandi/Desktop/top500Freq.txt', 'w')
    f.write(str(sorted_word_freq).strip('[').strip(']'))
    f.close()

    sorted_word = [v[0] for v in sorted_word_freq] # top 500 occuring words

    #print(sorted_word)

    #print(cleaned_reviews)


    # below will be generating the vector matrix

    return sorted_word,cleaned_reviews,dictionary_words

def generate_vector(top500,cleaned_revs):

    mymatrix = []
    for review in cleaned_revs:
        initial_dict = {x: 0 for x in top500}

        for _word in review:
            if _word in initial_dict:
                initial_dict[_word] += 1
        #mylist.append(initial_dict)
        tmp = [v for k,v in initial_dict.items()]
        mymatrix.append(tmp)
    return mymatrix

if __name__ == '__main__':
    top_words,reviews,dict_words = getProcessedList()
    matr = generate_vector(top_words,reviews)
    #ls = ['AA','BB','CC']
    #print(matr)
    X = np.array(matr)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
    centroids = kmeans.cluster_centers_
    print(centroids)
    #for j in range(10):
        #d = kmeans.transform(X)[:, j]
        #ind = np.argsort(d)[::-1][:2]
    #print X[ind]
    f1 = open('/Users/siddhartharoynandi/Desktop/top5clusterwords.txt', 'w')


    for items in centroids:
        a = {}
        items = list(items)
        for i in range(5):
                a[top_words[items.index(max(items))]] = max(items)
                items[items.index(max(items))] = 0
        #print a
        f1.write(str(a))
    f1.close()
    exit()

