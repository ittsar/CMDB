#CMDB is Configuration Management Data Base
import uuid
import ipaddress
#import usaddress
#import phonenumbers
import json
#import LatLon

def newUUID():
	myUUID = uuid.uuid4()
	return(myUUID)

class Relationships():
	def __init__(self):
		self.relationships=[]
	def addRelationship(self,relationship):
		self.relationships.append(relationship)
	def dumpcontents(self):
		data=str(self.__class__) +"\r\n"
		for i in self.relationships:
			data=data+"\t"+i.dumpcontents()
		return(data)



class Relationship():
	pass

class Parental(Relationship):
	def __init__(self,parent,child,kind):
		self.parent=parent
		self.child=child
		self.kind=kind #insideof,downstream,belongsto
	def dumpcontents(self):
		data=str(self.__class__) +"\r\n"
		data=data+"\t"+self.parent.identify()
		data=data+"\t"+self.child.identify()
		return(data)

class Dependency(Relationship):
	def __init__(self,consumer,provider):
		self.consumer=consumer
		self.provider=provider
	def dumpcontents(self):
		data=str(self.__class__) +"\r\n"
		data=data+"\t"+self.consumer.identify()
		data=data+"\t"+self.provider.identify()
		return(data)

class Peer(Relationship):
	def __init__(self,peers,kind=""):
		self.peers=peers
		self.kind=kind #relatedto,physicallyconnectedto,logicallyconnectedto
	def dumpcontents(self):
		data=str(self.__class__) +"\r\n"
		for i in self.peers:
			data=data+"\t"+i.identify()
		return(data)




#Parent > Child
#Child < Parent
#Peer <> Peer
		
#Router > Network Bridge > MAC Address Table > Entry
#Router > Network Bridge > Logical Interface
#Router Physical Interface > Logical Interface > VLAN ID tag
#Router > VRF > Route Table > Route
#Router > Physical Interface <> Physical Interface < Router
