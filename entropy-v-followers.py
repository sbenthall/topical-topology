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

    histify("Followers",user_metadata_matrix[:,0])

    scatterfy("Entropy","Followers",entropies,user_metadata_matrix[:,0],ylog=True)

if __name__ == "__main__":
    main()
