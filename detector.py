# Importing our custom pre-processing module
from pre_process_emails import main

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

emails_and_labels = main()

# We need to pass email-text only to the CountVectorizer
emails = []
labels = []

for (email, label) in emails_and_labels:
    emails.append(email)
    labels.append(label)

print "Number of emails: ", len(emails)
print "Labels: ", len(labels)

# Split 11000 emails to train and test sets of 8000 & 3000
x_train = emails[:8000]
x_test = emails[8000:]
y_train = labels[:8000]
y_test = labels[8000:]

vectorizer = CountVectorizer(min_df=1)

# Fit to our training data
X = vectorizer.fit_transform(x_train)

print X.shape
print len(y_train)

##### Multinomial Naive Bayes #####
nb_detector = MultinomialNB()
nb_detector.fit(X, y_train)

X_test = vectorizer.transform(x_test)

y_pred = nb_detector.predict(X_test)

# Calculate Accuracy:
print "Accuracy: ", accuracy_score(y_test, y_pred)

print "\n\nSome random testing: "

test = [u'article powerits online trading platform please find attached article european electricity report september 2001 kind regard sarimah black', u'need help marriage hello vlgr professi nal per dose vlgr soft per dose generc vlgr per dose clls per dose clls soft per dose sinneth wrongeth soul hate love death son let depart thine eye keep sound wisdom discretion say hated instruction heart despised reproof house righteous much treasure revenue wicked trouble better little righteousness great revenue without right']

x_te = vectorizer.transform(test)
print detector.predict(x_te)
# Should print ['ham','spam']

# Using SVM:
print "\n\nSupport Vector Machines: "

from sklearn import svm

svm_detector = svm.SVC(C=10000)

svm_detector.fit(X, y_train)

y_svm_pred = svm_detector.predict(X_test)

print "SVM Accuracy: ", accuracy_score(y_test, y_svm_pred)
