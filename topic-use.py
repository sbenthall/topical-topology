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
from operator import itemgetter


SORTED_USAGE_TOPIC_PATH = "topic-usage-sorted.txt"

user_metadata_matrix = numpy.load('user_metadata_matrix.npy')
user_topic_matrix = numpy.load('user_topic_matrix.npy')

topic_usage = sum(normalize(user_topic_matrix))

histify("Topic Usage",topic_usage)

sort_and_save(topic_usage,SORTED_USAGE_TOPIC_PATH)
