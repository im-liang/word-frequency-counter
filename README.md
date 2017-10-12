# Word Frequency Counter

Find the most common occurring words, and the sentences where they are in.

### Prerequisites

I use homebrew to install the packages

Install Python

```
brew install python
```

#### Install dependencies

```
pip install pypdf2
```

### Run the Application

```
python app.py <dir-name>/<file-name>
```

### Directory Layout

```
app.py         -> main application module
support.py     -> support module for extracting content
const.py       -> constants
english_stopwords.txt -> stopwords provided by https://github.com/Alir3z4/stop-words/blob/master/english.txt

```
