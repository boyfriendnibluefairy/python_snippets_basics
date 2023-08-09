##
## Voting Classifier - applies very different
## training algorithms to make predictions.
## Each algorithm will have an output that tells
## which class a test instance belongs to. The class
## that gets the most votes is the ensemble's prediction.
## This majority-vote classifier is called a
## hard voting classifier
##

## Let's try voting classifier on moons data set
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=600, noise=0.30, random_state=42)

## Let's split the moons data set into training
## data set and test data set, test_size defaults to 0.25
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

## We will use three diverse classifiers for our
## voting classifier, they are
##  1) Logistic Regression
##  2) RandomForestClassifier
##  3) Support Vector Machine
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

voting_classifier = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(random_state=42)),
        ("rfc", RandomForestClassifier(random_state=42)),
        ("svc", SVC(random_state=42))
    ]
)
## Let's train our Voting Classifier object using our training
## data set
voting_classifier.fit(X_train, y_train)

## We can now test our trained Voting Classifier object using
## our test data set. But before that, let's see the accuracy
## of individual classifiers. Accuracy is given by score() function.
## named_estimators_ outputs a dictionary of the cloned estimators
print("")
print("individual classifier scores: ")
for classifier_name, classifier in voting_classifier.named_estimators_.items():
    print(classifier_name, "=", classifier.score(X_test,y_test))
## Let's print the overall accuracy of the voting classifier object:
print("voting classifier score:")
str = f"{voting_classifier.score(X_test,y_test)}"
print(str)
print("")
## Most of the time, voting classifier outperforms individual classifiers.
## But for n_samples = 600 or higher, radom forest outperforms the rest


## When predict() method is called, voting classifier object performs
## hard voting and displays the class that was predicted by all or most
## of the classifiers
str = voting_classifier.predict(X_test[:1])
print("voting classifer prediction = ", str)
## display individual votes:
str = [clf.predict(X_test[:1]) for clf in voting_classifier.estimators_]
print("individual votes: ",str)
## This means that 2 out of 3 classifiers predicted that X_test belongs to
## class 1 of y_test whatever that is.

