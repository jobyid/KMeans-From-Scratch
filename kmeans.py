import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
from matplotlib import style
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import sys
from operator import attrgetter


class KMeans:
    def __init__(self, clusters=2, tolerance=0.0001, k_plus_plus=False, max_iterations = 500,
                 verification_loops=1):
        self.k = clusters
        self.tolerance = tolerance
        self.k_plus = k_plus_plus
        self.mi = max_iterations
        self.vl = verification_loops
        self.centroids = {}
        self.classes = {}
        self.loops = []
        self.pred = []
        self.fitted = False

    def find_centroids(self, data):
        # Standard mode so randomly pick 5 centroids from the data
        # Use a sample of the data rather then full data to help accuracy and speed
        sample = data[(np.random.choice(data.shape[0], data.shape[0]//4, replace=False))]
        #loop though k to get centroids equal to clusters needed
        for i in range(self.k):
            self.centroids[i] = sample[i]
            # While looping makes the classes dict as well for use later
            self.classes[i] = []

    def find_centroids_plus_plus(self, data):
        # pick centroids that are evenly spread
        centroids = []
        sample = data[(np.random.choice(data.shape[0], data.shape[0] // 2, replace=False))]
        centroids.append(sample[0])
        sample = sample[1:]
        for c_id in range(self.k - 1):
            dist = []
            for i in range(sample.shape[0]):
                point = sample[i, :]
                dist_compare = sys.maxsize
                for j in range(len(centroids)):
                    temp_dist = np.linalg.norm(point - centroids[j])
                    dist_compare = min(dist_compare, temp_dist)
                    dist.append(dist_compare)
            dist = np.array(dist)
            next_centroid = sample[np.argmax(dist), :]
            centroids.append(next_centroid)
            for i in range(self.k):
                self.centroids[i] = centroids[i]
                # While looping makes the classes dict as well for use later
                self.classes[i] = []

    def find_point_distance(self, data):
        # Loop through the data to compare each point to the centroids
        for d in data:
            dist = [np.linalg.norm(d-self.centroids[c]) for c in self.centroids]
            classification = dist.index(min(dist))
            self.classes[classification].append(d)

    def recalculate_centroids(self):
        previous = dict(self.centroids)
        #average the cluster datapoints to re-calculate the centroids
        for cl in self.classes:
            self.centroids[cl] = np.average(self.classes[cl], axis = 0)
        isOptimal = False
        # loop through and update centroids
        for centroid in self.centroids:
            original_centroid = previous[centroid]
            curr = self.centroids[centroid]
        # check if in tolerance
        if np.sum((curr - original_centroid)/original_centroid * 100.0) > self.tolerance:
             isOptimal = False
        else:
            isOptimal = True
        return isOptimal

    def fit(self, data):
        self.fitted = True
        # loop through validation loops
        for x in range(self.vl):
            # make centroids
            if self.k_plus:
                self.find_centroids_plus_plus(data)
            else:
                self.find_centroids(data)
            #loop through the iterations moving centroids
            for it in range(self.mi):
                self.find_point_distance(data)
                isOptimal = self.recalculate_centroids()
                if isOptimal:
                    break
            self.find_error()

    def predict(self, data):
        # must be run after fit
        if self.fitted:
            # return and array of the predicted classifications to plot.
            best = self.loops[0]
            for l in self.loops:
                if l.es < best.es:
                    best = l
            print("best", best)
            clas = []
            for d in data:
                for cl in best.classes.keys():
                    for x in best.classes[cl]:
                        if (d == x).all():
                            clas.append(cl)
            self.pred = clas
            return clas
        else:
            raise Exception("Please run the fit() function before predicting")

    def plot_results(self, data, d1,d2, c1, c2):
        if self.fitted:
            if not self.pred:
                scr = self.predict(data)
            else:
                scr = self.pred
            plt.scatter(data[:, d1], data[:, d2],c=scr, s=50, cmap='viridis')
            for centroid in self.centroids:
                plt.scatter(self.centroids[centroid][c1], self.centroids[centroid][c2],  marker =
                "x", c='black', s=200, alpha=0.5)
            plt.show()
        else:
            raise Exception("Please run the fit() function before plotting")


    def find_error(self):
        # sum of the mean squared
        td = []
        for c in self.classes:
            # list of the distances from centroids
            distances = [np.linalg.norm(c-self.centroids[c]) for c in self.centroids]
            td += distances
        x = MeansLoops(sum(td),self.classes, self.centroids)
        self.loops.append(x)

    def fit_predict(self,data):
        self.fit(data)
        self.predict(data)
    def fit_plot(self,data, d1,d2,c1,c2):
        self.fit(data)
        self.plot_results(data,d1,d2,c1,c2)

class MeansLoops:
    def __init__(self,error_score, classes, centroids):
        self.es = error_score
        self.classes = classes
        self.cen = centroids
    def get_score(self):
        return self.es
