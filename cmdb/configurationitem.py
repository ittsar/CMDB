import cmdb.relationships

class CI():
	#CI is configuration item
	def __init__(self,UUID):
		self.UUID = UUID
		return(self)
	def addPeer(self,peer,relationships):
		newRelationship = cmdb.relationships.Peer([self,peer])
		relationships.addRelationship(newRelationship)
	def addChild(self,child,relationships):
		newRelationship = cmdb.relationships.Parental(self,child)
		relationships.addRelationship(newRelationship)		
	def addParent(self,parent,relationships):
		newRelationship = cmdb.relationships.Parental(parent,self)
		relationships.addRelationship(newRelationship)
	def addDependencyProvider(self,provider,relationships):
		newRelationship = cmdb.relationships.Dependency(self,provider)
		relationships.addRelationship(newRelationship)		
	def addDependencyConsumer(self,consumer,relationships):
		newRelationship = cmdb.relationships.Dependency(consumer,self)
		relationships.addRelationship(newRelationship)
	def identify(self):
		return(str(self.__class__) +"\t"+ str(vars(self))+"\r\n")



class CIs():
	def __init__(self):
		self.CIs=[]
	def addCI(self,newCI):
		self.CIs.append(newCI)
	#def dumpcontents(self):
	#	for i in self.CIs:
	#		i.dumpcontents()
