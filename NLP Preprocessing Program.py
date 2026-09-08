import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


text = """
Natural Language Processing is a branch of
Artificial Intelligence that deals with human language.
"""


# Tokenization

words = word_tokenize(text)

print("Tokens:")
print(words)


# Stop word removal

stop_words = set(stopwords.words("english"))

filtered = []

for word in words:

    if word.isalpha() and word.lower() not in stop_words:

        filtered.append(word.lower())


print("\nAfter Stop Word Removal:")
print(filtered)


# Stemming

stemmer = PorterStemmer()

stemmed = []

for word in filtered:

    stemmed.append(
        stemmer.stem(word)
    )


print("\nStemmed Words:")
print(stemmed)


# Lemmatization

lemmatizer = WordNetLemmatizer()

lemmatized = []

for word in filtered:

    lemmatized.append(
        lemmatizer.lemmatize(word)
    )


print("\nLemmatized Words:")
print(lemmatized)
