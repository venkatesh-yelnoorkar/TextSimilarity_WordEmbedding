
#l = ['hello my name is john', 'i like eating', 'i am going to a place called rajveik']
#l = ['secure lending: level 1 assets', 'margin lending backed by non level 1 collateral']
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def pp(l = []):
    tokenized_list = []
    sub_stop_filter_list = []
    lemmatized_list = []
    sub_lemmatized_list = []

    regexptokenizer = RegexpTokenizer(r'\w+')

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()


    for i in range(0, len(l)):
        #tokenized_list.append(word_tokenize(l[i]))
        tokenized_list.append(regexptokenizer.tokenize(l[i]))
        sub_stop_filter_list = [w for w in tokenized_list[i] if w not in stop_words]
        sub_lemmatized_list = [lemmatizer.lemmatize(w) for w in sub_stop_filter_list]
        lemmatized_list.append(sub_lemmatized_list)
        
    return lemmatized_list
