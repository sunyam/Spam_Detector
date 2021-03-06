import os
import random
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation

# Loading the email-dataset
# Input: @path- Path to the dataset directory
def load_dataset(path):
    # Loading spam-emails:
    path1 = path + '/spam'
    for email in os.listdir(path1)[1:]:
        f = open(path1+os.sep+email, 'r')
        content = f.read()
        entire_email_dataset.append((content, "spam"))
        f.close()
    
    print "Done reading " + str(len(entire_email_dataset)) + " spam emails."

    # Loading ham-emails (ham is non-spam):
    path2 = path + '/ham'
    for email in os.listdir(path2)[1:]:
        f = open(path2+os.sep+email, 'r')
        content = f.read()
        entire_email_dataset.append((content, "ham"))

    print "Done reading all " + str(len(entire_email_dataset)) + " emails."

# Pre-processing text
# Input: @text- Raw text that needs to be processed
#        @custom_stopwords- Additional LIST of stopwords that the user wants to add to the standard stopwordList
# Returns: @clean_text- Processed list of words
def cleanUp(text, custom_stopwords=[]):
    # Initialising Lemmatizer object
    lemm = WordNetLemmatizer()
    
    # Collecting all my stopwords
    my_stopwords = stopwords.words('english') + list(punctuation) + custom_stopwords
    
    clean_text = ''
    for word in word_tokenize(unicode(text, errors='ignore')):
        w = lemm.lemmatize(word.lower())
        if w not in my_stopwords and len(w)>2:
            clean_text += w + ' '
    
    # Because the last character is a redundant whitespace, return [:-1]
    return clean_text[:-1]

entire_email_dataset = []
def main():
    # Load dataset
    path = '/Users/sunyambagga/GitHub/Spam_Detector/dataset'
    load_dataset(path)

    clean_emails_with_labels = []
    
    for (email, label) in entire_email_dataset:
        clean_email = cleanUp(email, ['subject'])
        clean_emails_with_labels.append((clean_email, label))

    # Right now, we have 3000 spam-emails in the list, followed by 6000 ham-emails
    # Shuffling:
    random.shuffle(clean_emails_with_labels)

    return clean_emails_with_labels