__author__ = 'jonathanbrodie'
from hzclient.codec import setcodec,proxycodec
from hzclient.clientmessage import ClientMessage


class SetProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title, "hz:impl:setService")
        self.connection.adjustCorrelationId(firstpack)
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,True)
        if response is not None:
            "Set proxy initialized"
        else:
            "Couldn't initalize"
    def AddAll(self,   valueList):
        msg=setcodec.SetAddAllCodec.encodeRequest( self.title, valueList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetAddAllCodec.decodeResponse(msg2)
    def Add(self,   value):
        msg=setcodec.SetAddCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetAddCodec.decodeResponse(msg2)
    def AddListener(self,   includeValue, eventhandler):
        msg=setcodec.SetAddListenerCodec.encodeRequest( self.title, includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=setcodec.SetAddListenerCodec.EventHandler(eventhandler)
        return setcodec.SetAddListenerCodec.decodeResponse(msg2)
    def Clear(self,  ):
        msg=setcodec.SetClearCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetClearCodec.decodeResponse(msg2)
    def CompareAndRemoveAll(self,   valueSet):
        msg=setcodec.SetCompareAndRemoveAllCodec.encodeRequest( self.title, valueSet)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetCompareAndRemoveAllCodec.decodeResponse(msg2)
    def CompareAndRetainAll(self,   valueSet):
        msg=setcodec.SetCompareAndRetainAllCodec.encodeRequest( self.title, valueSet)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetCompareAndRetainAllCodec.decodeResponse(msg2)
    def ContainsAll(self,   valueSet):
        msg=setcodec.SetContainsAllCodec.encodeRequest( self.title, valueSet)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetContainsAllCodec.decodeResponse(msg2)
    def Contains(self,   value):
        """
        Check if value is in the set
        :param value: value to check
        :return:
        """
        msg=setcodec.SetContainsCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        self.connection.adjustPartitionId(msg,value)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetContainsCodec.decodeResponse(msg2)
    def GetAll(self,  ):
        msg=setcodec.SetGetAllCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetGetAllCodec.decodeResponse(msg2)
    def IsEmpty(self,  ):
        """
        Determine if the set is empty
        :return: boolean for true or false
        """
        msg=setcodec.SetIsEmptyCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)

        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetIsEmptyCodec.decodeResponse(msg2)

    def Remove(self, value):
        """

        :param value: value to remove
        :return:
        """
        msg=setcodec.SetRemoveCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        self.connection.adjustPartitionId(msg,value)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetRemoveCodec.decodeResponse(msg2)
    def RemoveListener(self, registrationId):

        msg=setcodec.SetRemoveListenerCodec.encodeRequest( self.title, registrationId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetRemoveListenerCodec.decodeResponse(msg2)
    def Size(self,  ):
        """

        :return: size of set
        """
        msg=setcodec.SetSizeCodec.encodeRequest(self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return setcodec.SetSizeCodec.decodeResponse(msg2)