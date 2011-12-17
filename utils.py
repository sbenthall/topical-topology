from settings import *
import os
import simplejson as json
import time
from twitter import TwitterHTTPError
import numpy
import matplotlib.pyplot as plt
from pylab import axes,axis
import re
from operator import itemgetter

def load_snowball():
    if os.path.isfile("%s" % (SNOWBALL_PATH)):
        snowball_file = open("%s" % (SNOWBALL_PATH),'r')
        snowball = json.loads(snowball_file.read())
        return snowball
    else:
        print "error"


def get_followers_count(username):
    log_name = "%s%s.json"%(LOG_PATH,username) 
    if os.path.isfile(log_name):
        log = json.loads(open(log_name,'r').read())
        return log[0]['user']['followers_count']


def call_api(method,arguments,sleep_exp=1):
    def call_again():
        s = SLEEP ** sleep_exp
        print("Sleeping for %d at %s" % (s, time.strftime('%X %x')))
        time.sleep(s)
        return call_api(method,arguments,sleep_exp + 1)

    try:
        r = method(**arguments)
        return r
    except TwitterHTTPError as e:
        print(e) 
        code = e.e.code
        # responding to error codes
        # see https://dev.twitter.com/docs/error-codes-responses
        if code == 400: # Invalid request, or rate limited
            if SLEEP ** (sleep_exp - 1) > 3600:
                # have slept for over an hour, so not rate limited
                # something is wrong with request
                raise e
            else:
                return call_again()
        elif code == 401: # Unauthorized
            raise e
        elif code == 403: # Forbidden due to update limits
            raise e
        elif code == 404: # Resource not found
            raise e
        elif code == 406: # Invalid format for search request
            raise e
        elif code == 420: # Search or Trends API rate limited
            return call_again()
        elif code == 500: # 'Something is broken'
            raise e
        elif code == 502: # Twitter is down or being upgraded
            return call_again()
        elif code == 503:
            return call_again()
        else:
            raise e



def normalize(dist):
    return (dist.T / sum(dist.T).T).T

#this is a hack
EPSILON = 0.0000000000000001

def entropy(dist):
    nd = normalize(dist) + EPSILON
    return 0 - sum((nd * numpy.log(nd)).T).T

def histify(label, data, bins=50):
    n, bins, patches = plt.hist(data, bins)
    print(n)
    plt.title("%s Histogram" % label)
    plt.savefig("%s_histogram.png" % label.lower().replace(" ","_"), format='png')
    plt.clf()

def scatterfy(xlabel,ylabel,xdata,ydata,xlog=False,ylog=False,symbol='bo'):
    if xlog and ylog:
        axes(xscale='log',yscale='log')
    elif xlog:
        axes(xscale='log')
    elif ylog:
        axes(yscale='log')

    #axis([min(entropies), max(entropies), 0, max(followers)*1.1])
    plt.plot(xdata,ydata,symbol)
    plt.title('%s vs. %s' % (xlabel,ylabel))
    plt.savefig("%s_%s_plot.png" % (xlabel.lower().replace(" ","_"), ylabel.lower().replace(" ","_")), format='png')
    plt.clf()


TOPIC_PATH = 'topic-keys.txt'
TOPIC_PATTERN = "(\d*)\s*(0[.]\d*)\s(.*)\n"


def get_topic_dict():
    topics = open(TOPIC_PATH)
    topic_dict = dict()

    for line in topics.readlines():
        topic = re.findall(TOPIC_PATTERN, line)
        for index, value, terms in topic:
            topic_dict[index] = terms

    return topic_dict

def sort_and_save(data,file_name):
    topic_dict = get_topic_dict()

    sorted_data = sorted(enumerate(data), key=lambda x: -x[1])

    sorted_file = open(file_name, 'w')

    for index, topic in enumerate(sorted_data):
        print index, '\t', topic[0], '\t', topic_dict.get(str(topic[0]))
        sorted_file.write("%d\t%d\t%d\t%s\n" % (index, topic[0], topic[1], topic_dict.get(str(topic[0]))))

    return sorted_data
