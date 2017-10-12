import sys
from os import listdir
from os.path import isfile, join, isdir, exists
from multiprocessing import Pool
import support
import const

def wordFrequency(fname):
    counter = {}
    content = support.convertFile(fname)
    sentences = support.split2Centences(content)
    for sentence in sentences:
        words = support.split2Word(sentence)
        for word in words:
            if word in counter:
                counter[word].append(sentence)
            else:
                counter[word] = [sentence]
    return counter


def mostFrequentWord(counter):
    max_count = 0
    result = {}
    if type(counter) is dict: # single file
        for word in counter:
            if (len(counter[word]) > max_count):
                result.clear()
                result[word] = counter[word]
                max_count = len(counter[word])
            elif (len(counter[word]) == max_count):
                result[word] = counter[word]
    else:
        for x in counter:
            for word in x:
                if (len(x[word]) > max_count):
                    result.clear()
                    result[word] = x[word]
                    max_count = len(x[word])
                elif (len(x[word]) == max_count):
                    result[word] = x[word]

    print "{:<15} {:<20} {:<20}".format('Word','Frequency','Sentences')
    for current_word in result:
        print "{:<15} {:<20} {:<20}".format(current_word, max_count, result[current_word])


def main():
    if isdir(sys.argv[1]):
        files = [sys.argv[1] +'/' + f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
        pool = Pool(len(files))
        counter = pool.map(wordFrequency, files)
        mostFrequentWord(counter)
    elif exists(sys.argv[1]):
        counter = wordFrequency(sys.argv[1])
        mostFrequentWord(counter)
    else:
        print const.INPUT_ERR_MSG
        return


if __name__ == "__main__":
    main()
