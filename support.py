import PyPDF2
import re
import const
import sys

def convertPDF2TXT(fname):
    """
    Convert pdf file to txt
    @param fname: file name
    @return: txt content
    """
    content = ''
    with open(fname, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        for i in range(0, read_pdf.getNumPages()):
            pageObj = read_pdf.getPage(i)
            content += pageObj.extractText()
    return content


def convertFile(fname):
    """
    convert various type of file to txt
    @param fname: file name
    @return: file content
    @raise IOError: if file cannot be read
    """
    if fname.lower().endswith('.pdf'):
        return convertPDF2TXT(fname)
    elif fname.lower().endswith('.txt'):
        f = open(fname, 'r')
        return f.read()
    else:
        print const.FILE_TYPE_ERR_MSG
        sys.exit()


def filterStopWords(words):
    """
    convert various type of file to txt
    @param words: list of words
    @return: words without stopwords
    """
    result = []
    with open(const.STOPWORDS_FILE, 'r') as stopwordsFile:
        lines = stopwordsFile.readlines()
        stopwords = [x.strip() for x in lines]
    for word in words:
        if word not in stopwords:
            result.append(word)
    return result


def split2Centences(content):
    """
    split text content into list of sentences
    @param content: text content
    @return: list of sentences
    """
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', content)


def split2Word(content):
    """
    split sentence into list of words and filter out stopwords
    @param content: sentence
    @return: list of words
    """
    sentence = content.lower()
    words = re.findall(r'\'?[A-Za-z]+(?:\'[A-Za-z]+)*', sentence)
    return filterStopWords(words)
