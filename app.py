print("hello, world")

import cmdb.configurationitem,cmdb.relationships,cmdb.networkcomponents
from pprint import pprint

RelationshipsMaster = cmdb.relationships.Relationships()
CIsMaster = cmdb.configurationitem.CIs()

MyRouter = cmdb.networkcomponents.Router(cmdb.relationships.newUUID())
CIsMaster.addCI(MyRouter)
nic0 = cmdb.networkcomponents.PhysicalInterface(**{"UUID":cmdb.relationships.newUUID(),"enabled":True,"media":"Ethernet","HWaddress":"D3:A0:B3:A5:71:35"})
CIsMaster.addCI(nic0)
eth0 = cmdb.networkcomponents.LogicalInterface(**{"UUID":cmdb.relationships.newUUID(),"enabled":False,"mode":"L2","L2address":"D3:A0:B3:A5:71:35"})
CIsMaster.addCI(eth0)

NewRelationship = cmdb.relationships.Parental(**{"parent":MyRouter,"child":nic0,"kind":"insideof"})
RelationshipsMaster.addRelationship(NewRelationship)

NewRelationship = cmdb.relationships.Parental(**{"parent":nic0,"child":eth0,"kind":"belongsto"})
RelationshipsMaster.addRelationship(NewRelationship)

print(RelationshipsMaster.dumpcontents())

eth0.enable()

print(RelationshipsMaster.dumpcontents())

eth0.setL3(**{"L3protocol":"IPv4","L3address":"123.45.67.89/24"})
eth0.enable()

print(RelationshipsMaster.dumpcontents())

eth0.setL3(**{"L3protocol":"IPv4","L3address":"123.45.67.89/24"})
eth0.toggle()

print(RelationshipsMaster.dumpcontents())
