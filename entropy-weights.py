import re
from settings import *
from utils import *
from pprint import pprint as pp
import numpy
from numpy import array,zeros,ones,dot
from math import log
import matplotlib.pyplot as plt
import os
import simplejson as json
from pylab import axes, axis

SORTED_ENTROPY_TOPIC_PATH = "topic-entropy-sorted.txt"

user_metadata_matrix = numpy.load('user_metadata_matrix.npy')
user_topic_matrix = numpy.load('user_topic_matrix.npy')

user_entropies = entropy(user_topic_matrix)

weights,residue,rank,singulars = numpy.linalg.lstsq(normalize(user_topic_matrix),user_entropies)

topic_usage = sum(normalize(user_topic_matrix))

histify("Entropy Weights",weights)

scatterfy("Entropy Weight","Usage",weights,topic_usage,xlog=True,ylog=True,symbol="ro")

sort_and_save(weights,SORTED_ENTROPY_TOPIC_PATH)
