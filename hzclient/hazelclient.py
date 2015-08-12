__author__ = 'Jonathan Brodie'

from hzclient.proxy.topicproxy import TopicProxy
from hzclient.proxy.proxy import ALongProxy
from hzclient.proxy.mapproxy import MapProxy


from hzclient.connectmanager import ConnectionManager


class HazelcastClient(object):
    def __init__(self):
        self.connection=ConnectionManager()


    def getAtomicLong(self,title):
        mylong=ALongProxy(title,self.connection)
        return mylong

    def getTopic(self,title):
        mylong=TopicProxy(title,self.connection)
        return mylong

    def getMap(self,title):
        mylong=MapProxy(title,self.connection)
        return mylong


