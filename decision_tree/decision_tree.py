## How to implement a basic decision tree
## using the famous iris data set

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

## convert iris data into dataframe
df_iris = load_iris(as_frame=True)
## print(list(df_iris))
## print(df_iris.data.head)
## print(df_iris.target.head)

## create training data set
## target or type as function of petal length and width
X_train = df_iris.data[["petal length (cm)", "petal width (cm)"]].values
## print(X_train.shape)
## print(X_train)
y_train = df_iris.target
## print(y_train.shape)
## print(y_train)

## create a tree classifier object that will store and process
## the training data set
tree_clf_object = DecisionTreeClassifier(max_depth=2, random_state=42)
## train the object
tree_clf_object.fit(X_train, y_train)

## Use Graphviz, an open source graphing software package,
## to visualize the tree
## The code below generates a dot file
from sklearn.tree import export_graphviz
export_graphviz(
    tree_clf_object,
    out_file="iris_dataset_tree.dot",
    feature_names = ["petal length (cm)", "petal width (cm)"],
    class_names= df_iris.target_names,
    rounded=True,
    filled=True
)
## execute the ff to visualize the resulting dot file
## see footnotes
## dot -Tng decision_tree/iris_dataset_tree.dot -o tree.png



## =============================================
## FOOTNOTES

## if dot command is missing, do this:
## brew install gprof2dot
## sudo pip install pydot

