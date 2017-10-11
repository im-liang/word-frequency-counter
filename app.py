import sys
import support

def main(separator='\t'):
    content = support.convertFile(sys.argv[1])
    sentences = support.split2Centences(content)
    counter = {}
    for sentence in sentences:
        words = support.split2Word(sentence)
        for word in words:
            if word in counter:
                counter[word].append(sentence)
            else:
                counter[word] = [sentence]

    max_count = 0
    result = {}
    for word in counter:
        if (len(counter[word]) > max_count):
            result.clear()
            result[word] = counter[word]
            max_count = len(counter[word])
        elif (len(counter[word]) == max_count):
            result[word] = counter[word]

    print "{:<15} {:<20} {:<20}".format('Word','Frequency','Sentences')
    for current_word in result:
        print "{:<15} {:<20} {:<20}".format(current_word, max_count, result[current_word])


if __name__ == "__main__":
    main()
