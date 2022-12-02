import cmdb.configurationitem,cmdb.relationships

class PhysicalInterface(cmdb.configurationitem.CI):
	def __init__(self,UUID,enabled=False,media="Unspecified",HWaddress=""):
		super().__init__(UUID)
		self.enabled=enabled
		self.media=media
	def enable(self):
		self.enabled=True
	def disable(self):
		self.enabled=False
	def toggle(self):
		self.enabled !=self.enabled
class LogicalInterface(cmdb.configurationitem.CI):
	def __init__(self,UUID,enabled=False,L2protocol="Unspecified",L3protocol="Unspecified",L2address="Unspecified",L3address="Unspecified",mode="Unspecified"):
		super().__init__(UUID)
		self.enabled=enabled
		self.L2protocol=L2protocol
		self.L2address=L2address
		self.L3protocol=L3protocol
		self.L2protocol=L2protocol
		self.mode=mode
	def setL2(self,L2protocol,L2address):
		self.mode = "L2"
		self.L2protocol=L2protocol
		self.L2address=L2address
	def setL3(self,L3protocol,L3address):
		self.mode="L3"
		self.L3protocol=L3protocol
		self.L3address=L3address
	def enable(self):
		if (self.mode == "L3" and self.L3protocol=="IPv4" and self.L3address !="Unspecified") or (self.mode == "L2" and self.L3protocol=="Ethernet" and self.L2address !="Unspecified"):
			self.enabled=True
	def disable(self):
		self.enabled=False
	def toggle(self):
		if self.enabled==False:
			self.enable()
		else:
			self.enabled !=self.enabled
class Router(cmdb.configurationitem.CI):
	def __init__(self,UUID):
		super().__init__(UUID)
	
