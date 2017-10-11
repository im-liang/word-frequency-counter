import PyPDF2
import re
import const

def convertPDF2TXT(fname):
    """
    Convert pdf file to txt
    @param fname: file name
    @return: txt content
    """
    content = ''
    with open(fname, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for page in pages:
            content += page.extractText()
    return content

# def convertHTML2TXT(file):



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


def filterStopWords(words):
    result = []
    with open(const.STOPWORDS_FILE, 'r') as stopwordsFile:
        lines = stopwordsFile.readlines()
        stopwords = [x.strip() for x in lines]
    for word in words:
        if word not in stopwords:
            result.append(word)
    return result


def split2Centences(content):
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', content)


def split2Word(content):
    sentence = content.lower()
    words = re.findall(r'\'?[A-Za-z]+(?:\'[A-Za-z]+)*', sentence)
    return filterStopWords(words)
