#
#   Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
#   A Sample Implementation (see footnotes for details)
#   Author : Gilbert M. Oca

## For this demonstration, we will use the moons data set.
## See footnotes for details.
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=1000, noise=0.05, random_state=42)

## Let's see how the moons data set with 1000 samples looks like.
## uncomment lines below to see the plot
from matplotlib import pyplot as plt
# plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo")
# plt.plot(X[:, 0][y==1], X[:, 1][y==1], "b^")
# plt.show()

## Let's train a DBSCAN object to group these moons data points.
## eps = maximum distance between two data points
## min_samples = minimum number of samples within a group so that
## one of the points within that group will be considered its cluster center.
## This cluster center is also called core point. Based on relative distances,
## all points in one neighborhood can all be considered as core points.
from sklearn.cluster import DBSCAN
dbscan_obj = DBSCAN(eps=0.30, min_samples=6)
dbscan_obj.fit(X)
## DBSCAN has now labeled each of the 1000 samples
## based on our hyperparameters:
# print(dbscan_obj.labels_)
## if you decrease eps, you'll observe -1 labels which
## means they are considered outliers

## What if we have new test data points?
## How can we use the trained dbscan object to
## predict which cluster a test data point
## belongs to?
from sklearn.neighbors import KNeighborsClassifier
kn_clf = KNeighborsClassifier(n_neighbors=60)
## print(dbscan_obj.components_)          # X[x1, x2]
## print(dbscan_obj.core_sample_indices_) # y
## print(dbscan_obj.labels_)
kn_clf.fit(dbscan_obj.components_,
           dbscan_obj.labels_[dbscan_obj.core_sample_indices_])

## Now that we have a trained object, let's create three test data
## and have our trained object predict its labels
import numpy as np
X_test = np.array([[-0.6,0.9],[1.6,-0.3],[1.6,0.9]])
print(kn_clf.predict(X_test))
## to print accuracy of prediction for individual test instance:
#print(kn_clf.predict_proba(X_test))

## Plot of Decision Boundary
from matplotlib.colors import ListedColormap
# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
from sklearn.inspection import DecisionBoundaryDisplay
feature_1, feature_2 = np.meshgrid(
    np.linspace(X[:, 0].min(), X[:, 0].max(), 100),
    np.linspace(X[:, 1].min(), X[:, 1].max(), 100)
)
grid = np.vstack([feature_1.ravel(), feature_2.ravel()]).T
y_pred = np.reshape(kn_clf.predict(grid), feature_1.shape)
# display = DecisionBoundaryDisplay(
#     xx0=feature_1,
#     xx1=feature_2,
#     response=y_pred,
# )
plt.pcolormesh(feature_1, feature_2, y_pred, cmap=cmap_light)
plt.scatter(
    X[:, 0], X[:, 1], c=y
)
plt.scatter(
    X_test[:, 0], X_test[:, 1], marker="x", c="r", edgecolor="black"
)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Decision boundary between two clusters of moon dataset"
          "\n (z values are predicted using DBSCAN)")
plt.show()




## =============================================
## FOOTNOTES

## DBSCAN is an unsupervised learning algorithm
## that treats clusters as continuous regions of
## high density and these clusters are seperated
## by low density regions.
## In unsupervised learning, data are not labeled.
## Hence, it is the job of DBSCAN to group similar
## data points without the use of labels.

## make_moons data set is a set of points that
## looks like two disjunctive clusters shaped
## like cresent moon. Two differentiate data points
## from each moon, they are sometimes labeled
## 0 for upper cresent and 1 for lower cresent.