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
from mpl_toolkits.mplot3d import Axes3D
from operator import itemgetter

TOPIC_PATH = 'topic-keys.txt'
SORTED_FOLLOWER_TOPIC_PATH = 'topic-follower-sorted.txt'
SORTED_FRIEND_TOPIC_PATH = 'topic-friend-sorted.txt'
TOPIC_PATTERN = "(\d*)\s*(0[.]\d*)\s(.*)\n"

user_metadata_matrix = numpy.load('user_metadata_matrix.npy')
user_topic_matrix = numpy.load('user_topic_matrix.npy')

normalized_user_topic_matrix = normalize(user_topic_matrix.T).T

weights,residue,rank,singulars = numpy.linalg.lstsq(normalized_user_topic_matrix,numpy.log10(user_metadata_matrix + 1))


scatterfy("Followers","Friends",user_metadata_matrix[:,0],user_metadata_matrix[:,1],xlog=True,ylog=True)

scatterfy("Followers Weight","Friends Weight",weights[:,0],weights[:,1])

histify("Followers Weights",weights[:,0])
histify("Friends Weights",weights[:,1])

sorted_follower = sort_and_save(weights[:,0], SORTED_FOLLOWER_TOPIC_PATH)
sorted_follower.reverse()
print sorted_follower[0:24]
follower_least25 = sorted_follower[len(sorted_follower)-24:len(sorted_follower)]
follower_least25.reverse()
print follower_least25

sorted_friend = sort_and_save(weights[:,1],SORTED_FRIEND_TOPIC_PATH)

#get sorted friend
sorted_friend = sorted(enumerate(weights[:,1]), key=itemgetter(1))
sorted_friend.reverse()
print sorted_friend[0:24]
friend_least25 = sorted_friend[len(sorted_friend)-24:len(sorted_friend)]
friend_least25.reverse()
print friend_least25

#scatterfy("Topic Weight","Followers",weights[:,0],ylog=True)
