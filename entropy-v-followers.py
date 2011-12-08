import re
from settings import *
from utils import *
from pprint import pprint as pp
import numpy
from numpy import array,zeros,ones,dot
from math import log
import matplotlib.pyplot as pyplot
import os
import simplejson as json
from pylab import axes, axis


user_metadata_matrix = numpy.load('user_metadata_matrix.npy')
user_topic_matrix = numpy.load('user_topic_matrix.npy')


def main():

    entropies = entropy(user_topic_matrix)

    print(entropies)

    # the histogram of the data
    histify("Entropy",entropies)

    followers = user_metadata_matrix[:,0]
    print(followers)
    n, bins, patches = pyplot.hist(followers,50)
    pyplot.title("Followers Histogram")
    pyplot.savefig("followers_histogram.png", format='png')

    axes(yscale='log')
    #should make the axis scale change with the _variance_ of data
    axis([min(entropies), max(entropies), 0, max(followers)*1.1])
    pyplot.plot(entropies,followers,'bo')
    pyplot.title('Entropy vs. Followers')
    pyplot.savefig("entropy_followers_plot.png", format='png')

if __name__ == "__main__":
    main()
